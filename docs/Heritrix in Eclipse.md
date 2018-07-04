# Heritrix in Eclipse

# Heritrix 3.x in Eclipse on Ubuntu

Specifically Ubuntu 11.04, but should work for other versions from the
general time period (10.10, 11.10, ...).

N.B. There are other ways to do this, for example using additional
eclipse plugins for maven or git, but this is one way that is known to
work.

## 1. get software (java, eclipse, git, maven)

    sudo apt-get install sun-java6-jdk eclipse git maven2
    sudo update-java-alternatives --set java-6-sun  
    sudo update-java-alternatives --list

## 2. start eclipse, so it initializes your workspace, by default in ~/workspace

## 3. clone git repository

    cd ~/workspace
    git clone git://github.com/internetarchive/heritrix3.git

## 4. get dependency jars with maven

    cd ~/workspace/heritrix3
    mvn -Dmaven.test.skip=true install

## 5. import eclipse project

In eclipse: File / Import... / Existing Projects Into Workspace ...
choose ~/workspace/heritrix3

## 6. set up M2\_REPO variable in Eclipse

    Select Project > Properties > Java Build path > 
    Select Libraries tab > Add variable > Configure variables > New
      Name: M2_REPO
      Path: /home/{username}/.m2/repository

## 7. create new Debug Configuration

-   Run / Debug Configurations...
-   double-click Java Applications to create a new one
-   choose Main class org.archive.crawler.Heritrix
-   Arguments tab
    -   Program arguments: -a PASSWORD -l
        dist/src/main/conf/logging.properties
    -   VM arguments: -Dheritrix.development

## Attachments:

![](images/icons/bullet_blue.gif){width="8" height="8"}
[Screenshot.png](attachments/458853/12714188.png) (image/png)  
![](images/icons/bullet_blue.gif){width="8" height="8"}
[Screenshot-1.png](attachments/458853/12714189.png) (image/png)  
