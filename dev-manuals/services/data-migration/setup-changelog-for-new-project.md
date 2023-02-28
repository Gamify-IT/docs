# Setup database migration for a new Spring project

1. Download the [Liquibase CLI](https://www.liquibase.com/download)
2. Run a configured local instance of your project (so the database should be filled)
3. Define the path you would like to use for your root changelog, i.e. `CHANGELOG_FILE`=`src/main/resources/db/changelog-root.xml` and fill it with the content

```xml
<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog
   xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xmlns:pro="http://www.liquibase.org/xml/ns/pro"
   xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
      http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-4.1.xsd
      http://www.liquibase.org/xml/ns/pro
      http://www.liquibase.org/xml/ns/pro/liquibase-pro-4.1.xsd">
<includeAll path="db/changelog/"/><!-- Automatically queries all files in this directory in semantic versioning order -->
</databaseChangeLog> 
```
Add the following to your `application.properties`:
```properties
spring.liquibase.change-log=classpath:db/changelog-root.xml
```
Add the file `liquibase.properties` in the project root folder:
```properties
####     _     _             _ _
##      | |   (_)           (_) |
##      | |    _  __ _ _   _ _| |__   __ _ ___  ___
##      | |   | |/ _` | | | | | '_ \ / _` / __|/ _ \
##      | |___| | (_| | |_| | | |_) | (_| \__ \  __/
##      \_____/_|\__, |\__,_|_|_.__/ \__,_|___/\___|
##                  | |
##                  |_|
##
##      The liquibase.properties file stores properties which do not change often,
##      such as database connection information. Properties stored here save time
##      and reduce risk of mistyped command line arguments.
##      Learn more: https://docs.liquibase.com/concepts/connections/creating-config-properties.html
####
####
##   Note about relative and absolute paths:
##      The liquibase.properties file requires paths for some properties.
##      The classpath is the path/to/resources (ex. src/main/resources).
##      The changeLogFile path is relative to the classpath.
##      The url H2 example below is relative to 'pwd' resource.
####
# Enter the path for your changelog file.
changeLogFile=src/main/resources/db/changelog/changelog-root.xml

#### Enter the Target database 'url' information  ####
liquibase.command.url=jdbc:postgresql://localhost:5432/postgres

# Enter the username for your Target database.
#liquibase.command.username:

# Enter the password for your Target database.
#liquibase.command.password:

#### Enter the Source Database 'referenceUrl' information ####
## The source database is the baseline or reference against which your target database is compared for diff/diffchangelog commands.

# Enter URL for the source database
#liquibase.command.referenceUrl: jdbc:h2:tcp://localhost:9090/mem:integration

# Enter the username for your source database
#liquibase.command.referenceUsername:

# Enter the password for your source database
#liquibase.command.referencePassword:

# Logging Configuration
# logLevel controls the amount of logging information generated. If not set, the default logLevel is INFO.
# Valid values, from least amount of logging to most, are:
#   OFF, ERROR, WARN, INFO, DEBUG, TRACE, ALL
# If you are having problems, setting the logLevel to DEBUG and re-running the command can be helpful.
# logLevel: DEBUG

# The logFile property controls where logging messages are sent. If this is not set, then logging messages are
# displayed on the console. If this is set, then messages will be sent to a file with the given name.
# logFile: liquibase.log


#### Liquibase Pro Key Information ####
# Learn more, contact support, or get or renew a Pro Key at https://www.liquibase.com/trial
# liquibase.licenseKey:

#### Liquibase Hub Information ####
# Liquibase Hub is a free secure SaaS portal providing status reporting, monitoring & insights
# into your Liquibase database release automation.
# https://hub.liquibase.com

## Add your free Hub API key here
# liquibase.hub.apikey:
# liquibase.hub.mode:all




##  Get documentation at docs.liquibase.com       ##
##  Get certified courses at learn.liquibase.com  ##
##  Get support at liquibase.com/support         ##
```
Finally, execute
```sh
liquibase generateChangeLog --username=$DATABASE_USER --password=$DATABASE_USER_PASSWORD
```
in the project root directory.
