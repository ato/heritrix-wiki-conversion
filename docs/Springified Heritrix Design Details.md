# Springified Heritrix Design Details

## Use of Spring Core Container / Inversion-of-Control

A crawl configuration is now a collection of beans, specified and
initialized/wired in the Spring style.

A Spring configuration file, named by convention 'crawler-beans.xml'
(instead of the usual Spring 'beans.xml') is the main way of specifying
a crawl. As such, it replaces the order.xml of Heritrix 1.X and the
global.sheet (and possibly other sheets) of Heritrix 2.0.

Using the Spring facilities for including other configuration files by
reference, the configuration can in fact be split over many files,
including standard boilerplate files reused across many crawls (where
they are identical).

The container, via a special customized Spring ApplicationContext
subclass, may be instantiated at any time, or many times (discarding
interim results) while composing the configuration. Thus it is important
components do not perform resource-intensive or destructive actions
during simple instantiation/initiation.

Instead, the Spring 'Lifecycle' interface tells components to 'start',
and that is when significant resources should be allocated/opened/held
(like large in-memory structures, BDB environments, disk files).

## Implementing Overrides

All overridable values will have Java standard (bean-like) accessors, of
their natural type.

A class with overridable values should implement the HasKeyedProperties
interface; this gives access to a map (of type KeyedProperties) which
holds all overridable bean values. Support for the HasKeyedProperties
interface is as simple as:

``` bash
    KeyedProperties kp = new KeyedProperties();
    public KeyedProperties getKeyedProperties() {
        return kp;
    }
```

A property that is overridable should be stored and retrieved from the
KeyedProperties; any initialization can take place in a static
initiatlizer block. For example:

``` bash

    {
        setMinDelayMs(3000);
    }
    public int getMinDelayMs() {
        return (Integer) kp.get("minDelayMs");
    }
    public void setMinDelayMs(int minDelay) {
        kp.put("minDelayMs",minDelay);
    }
```

A Sheet bean is declared in the configuration for any desired override.
It includes a mapping from property-path style string keys (eg.
beanName.property.property) to replacement values. An example Sheet:

``` bash
<bean id="eduSheet" class="org.archive.spring.Sheet">
  <property name="overrideProperties">
   <value>
    frontier.minDelayMs=10000
   </value>
  </property>
</bean>
```

The mappings from SURT prefixes to the sheet name to apply are similarly
a bean:

``` bash
<bean id="overrideMappings" class="org.archive.spring.SurtToSheetMap">
 <property name="map">
   <map>
    <entry key="http://(edu," value="eduSheet"/>
   </map>
  </property>
```

A HesKeyedProperies instance, or a property itself, does not,
inherently, know its full property-path name. (Indeed, it may have
multiple such names.) However, before a Sheet can be used, it must be
'primed'. Each path within it is interpreted with respect to the current
BeanFactory. Each path must resolve to a property of an instance which
implements HasKeyedProperties; the KeyeProperties instance is at the
time of priming informed of its property-path name.

Applying a Sheet means pushing it onto a ThreadLocal stack held in a
KeyedProperties static field. Instances of KeyedProperties consult this
stack of Sheets before returning their internal/default value.

A usual idiom for applying a Sheet would include paired push and pop
operations. For example:

``` bash
 try {
  KeyedProperties.pushOverridesMaps(sheet);
  // do stuff
 } finally {
  KeyedProperties .popOverridesMap(sheet);
 }
```

A Sheet will be auto-primed the first time it is pushed. Mismatched
push/pop will generate a SEVERE logging event; it's probably a serious
bug.

(Initially, only mappings from SURT prefixes to overrides will be
allowed, but this approach also leaves open the possibility that sets of
DecideRules could be used to determine whether an override Sheet should
be applied to a specific URI. Or, that custom code could apply an
override Sheet at any point in URI processing.)

## Assisting editing

Initial editing will be just a giant TEXTAREA in which the
crawler-beans.xml and supporting referenced files (included XML or
support files like a seeds source file) can be changed. We will provide
a few starter templates, and UI mechanisms for copying profiles as in
Heritrix 1.X and 2.0.

There are 3 levels of checking which assist in the creation of valid
configurations:

-   is the XML well-formed? (client-side javascript will check this when
    using the Web UI
-   can the container be instantiated? (failures to provide Spring
    'required' initial values/wiring will trigger Spring exceptions,
    which will be caught and reported to the operator until all are
    resolved)
-   after container instantiation, all beans will be given an
    opoortunity to run a self-validation on their internal state, with
    errors collected and reported to the operator. Attempting to 'start'
    a context with outstanding validation errors of this type will be
    prevented.

Before final release, we will provide directed modification of the
crawler-beans.xml (so that most simple configuration changes do not
require direct editting of XML). This will include:

-   input fields just on 'values'
-   alternate boilerplate configurations – a sort of clip library – that
    can dropped in instead of standard beans at the conventional names.
    (For example, a library of alternate 'scope' objects.)

The basic process of launching a new job will be roughly equivalent to
the 1.x or 2.0 process, and perhaps easier:

-   pick a suitable earlier template(profile/previous job) to start
-   see a simple, input-field-based form suitable for editing all
    primitive settings values
-   if you want to change implementing modules or add to existing
    lists/maps, you can select from a series of fragment templates
    appropriate for the relevant type, or use a reference to an
    already-existing bean. Once alternatives are in place, their
    primitive values or embedded modules can be adjusted the same way
-   if desired, switching to raw XML editting will be allowed, or
    including other canned XML config files by reference
-   a 'verify' button will allow instant checking all dependencies are
    set; if not, the exception raised will be shown as a hint of what
    needs adding/changing

Each 'sheet' is now a top-level bean (though it may still be in a
separate, included file). For compactness of editing a sheet with only a
handful of overrides (as most are), editing could be via an
auto-complete key field then type-specific value editor.

## In-crawl dynamic changes

During the crawl, individual beans inside the configuration will be
viewable and editable (except for specific fields marked as
unchangeable) in the web UI. HOWEVER, these changes will not
automatically be reflected in the starting configuration. We will work
to create a log of such changes, and clear documentation, so operators
understand the need to manually, separately change the starting
configuration, if desired.

(Ideally, mid-crawl edits via the web UI will retain the same interface
as pre-crawl configuration edits. Thus the process could be to change
the declared configuration (and thus also the files on disk), then
propagate those changes into the running crawler. However, this will not
be initially supported, and there may be kinds of edits where this is
impossible or unwise, in which case a reconfiguration may require a
checkpoint, an offline configuration edit, then resume-from-checkpoint
with the new configuration.)

In-crawl changes to module configuration that come outside the admin UI
(JMX, direct programmatic mutations, such as in extension code) are more
difficult to handle; we will only include warnings that such changes are
not automatically propagated to the persistent configuration of the
crawl.

## 1.14 to 2.2 Migration Tool

We intend to target 1.14 (last major 1.x release) as the source
configuration format, and 2.2 (skipping 2.0) as the target configuration
format, for an automated migration assistance tool.

Some previous notes on how such a tool might work are available at
[Conversion Tool From 1.x Settings
(plan)](Conversion%20Tool%20From%201.x%20Settings%20(plan)).

While total error-free conversion for all custom configurations may not
be a practical goal, we intend for the 1.14 default configuration to
migrate with no fatal problems to a equivalent 2.2 configuration. Any
errors requiring operator attention (options with unclear analogues in
2.2) should be highlighted by the tool.
