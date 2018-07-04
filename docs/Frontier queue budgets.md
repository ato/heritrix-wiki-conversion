# Frontier queue budgets

(This describes Heritrix 1.14.x behavior, but mostly applies to H2/H3 as
well.)

### Overview

The
[BdbFrontier](https://webarchive.jira.com/wiki/spaces/Heritrix/pages/4260/BdbFrontier) has
been extended with a series of settings which allow it to use a
"budgeting" process for allocating its attention to its internal queues
(and thus, the individual hosts which often map one-to-one to queues).

With these settings, it is possible to rotate queues into and out of
'active' status at regular intervals. (A queue that is 'active' is
eligible to supply URIs to ready worker threads.) The decision to
deactivate a queue is based on its current running 'activity balance'
being depleted; these balances are depleted more quickly by URIs that
are deemed to have a higher 'cost'. Thus, queues with more interesting
(less costly) URIs get more attention, while those with less interesting
(more costly) URIs get less attention.

An inactive queue goes to the back of a FIFO queue of all inactive
queues. Inactive queues are activated when necessary to provide work to
a ready worker thread (because all other 'active' queues are already
in-progress or in various kinds of 'snooze' temporary waits.) When
activated, a queue's running activity balance is replenished, and each
subsequent URI attempted off that queue decrements that balance. When
the balance goes non-positive, the queue is again deactivated, to give
other queues an opportunity to become active and receive thread
attention. (If there are no other inactive queues, a queue so
deactivated is immediately reactivated with a fresh running balance.)

An overall lifetime 'total budget' may be set for a queue. When total
expenditures on a queue (for all times it has been active) exceed this
budget, the queue is 'retired' -- placed to the side, permanently
inactive. Only operator intervention -- such as raising the 'total
budget' for that queue -- can recall a queue from retirement. However,
while retired, the queue retains all its pending URIs, and continues to
receive newly discovered URIs. So 'retirement' is a good place to hold a
queue while attempting to make operator decisions about what, if any,
effort will be spent continuing to visit it.

Any number of retired queues, with any number of retired queued URIs, do
not count as currently queued URIs, so will not stop a crawl from
finishing when all active/inactive queues are empty. Thus, in the
presence of retired queues, it is useful to use the 'pause-at-finish'
feature to avoid ending a crawl that has reached a finished state.
Instead, by pausing the crawl when all unretired queues are empty, the
operator can inspect the crawl's progress, including the retired queues,
and make a decision about further crawling, within the same context,
before truly ending the crawl.

### Configuration and Use

BdbFrontier has the following new settings:

-   **hold-queues**: if true, new queues start inactive -- allowing
    'site-first' and similar behaviors.
-   **balance-replenish-amount**: each queue activated will be given a
    session activity balance to draw against of this many units
-   **queue-total-budget**: maximum to spent on a queue; beyond this
    value, queue will be retired. Default of -1 means no maximum
-   **cost-policy**: a number of swappable options for what cost to
    assign each URI. The default ZeroCostAssignmentPolicy considers all
    URIs to have zero cost, and thus budgetting has no effect. (The
    activity balance never depletes; the total budget is never
    exceeded.) (The default should probably be
    UnitCostAssignmentPolicy.)

The balance-replenish-amount and queue-total-budget values may be set
globally, or overriden for specific domains. Queues take on the balance
and budget values of the URIs placed on them. (Beware: if using any
non-standard queue-assignment scheme, such as IP based, based on a fixed
number of buckets, or forcing certain URIs to certain queues, this may
lead to confusing behavior, as each varied URI changes the queue's
values.)

### Mid-crawl Adjustments

Setting a queue's effective balance-replenish amount to zero, or its
total budget to anything under its current total expenditure, will
quickly cause the queue to move to 'retired' status.

Note: changing any settings cause all retired queues to be moved to
inactive, so that in case the new replenish/budget numbers allow the
queue to become active, it will, (If its turn to become active comes up,
but it still meets retirement conditions, it will be re-retired before
any URIs are tried.)

### Reporting

Other notable features:

The Frontier report now includes per-queue expenditure information,
including total budget, total expenditure, current activation budget
remaining, and the latest-cost/average-cost of URIs seen. A queue whose
latest-cost seems high is into the higher-cost portion of its workload;
a queue whose average-cost is high has been spending a preponderance of
its time on more-costly URIs.

### Common Usage Scenarios

To have the BdbFrontier behave exactly as it did before budgetting
features were added, set 'hold-queues' to 'false' (so that all queues
begin active, in one big round-robin arrangment). Set 'cost-policy' to
ZeroCostAssignmentPolicy. (The settings of 'balance-replenish-amount'
and 'queue-total-budget' are irrelevant.) This approach is NOT
recommended; 'hold-queues' should be true to allow at least some intense
focus on a smaller set of queues at a time to minimize random disk IO. 

To use classic 'site-first' behavior, set 'hold-queues' to 'true' and
retain the ZeroCostAssignmentPolicy. (Or, if using a nonzero cost
policy, make the 'balance-replenish-amount' very large.) Queues will
begin inactive and only activate (start being crawled) when necessary to
keep worker threads busy. In general, only when older sites finish (or
slow to a rate making space for new queues) will new queues be
activated, achieving the desired effect of working one queue through to
completion before beginning others. However, there is a risk if early
queue(s) contain endless low-value/trap material, that other more
interesting queues will never be activated.

To introduce budgetted rotation of queues, so that once a certain amount
of progress is made on one queue, it is made inactive to allow some
progress to occur on other queues, change the 'cost-policy' to something
else. UnitCostAssignmentPolicy assigns all URIs a cost of 1, so every
attempt draws the activation budget (default size: 3000) down a little.
WagCostAssignmentPolicy includes some wild guesses about what URIs are
less interesting, and increases the cost of URIs with query-string
components, and which are identical to their 'via' except in their
query-string. This ensures such 'more costly' URIs are (within a single
queue) scheduled behind less costly URIs, and queues dominated by costly
URIs spend less time active. You can also adjust the
'balance-replenish-amount' to control how quickly queues are rotated out
of the active slots. (A degenerate value of '1' would approximate no
budgeting at all, round-robinning among all queues.)

To further cap the effort devoted to queues, you can set a
'queue-total-budget' value. Any queue whose total expenditures exceed
this budget become 'retired'. This is most useful in connection with the
'pause-on-finish' option, so that you get a chance to examine the
retired queues for interesting content before the crawl truly ends. By
changing the settings mid-crawl (during a pause), all retired queues
will be reevaluated for activation.
