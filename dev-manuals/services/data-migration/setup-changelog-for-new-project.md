# Setup database migration for a new Spring project

1. Download the [Liquibase CLI](https://www.liquibase.com/download)
2. Run a configured local instance of your project (so the database should be filled)
3. Create all directories until `src/main/resources/db/changelog/`
4. Define the path you would like to use for your root changelog. We use `src/main/resources/db/changelog-root.xml`. Fill it with the content
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
  <!-- Automatically queries all files in this directory in lexical order -->
  <includeAll path="db/changelog/"/>
</databaseChangeLog>
```
5. Add the following to your `application.properties`:
```properties
spring.liquibase.change-log=classpath:db/changelog-root.xml
```
6. Add the liquibase dependency to the `pom.xml`:
```xml
<properties>
…
	<liquibase.version>4.19.0</liquibase.version>
</properties>
…
<dependency>
	<groupId>org.liquibase</groupId>
	<artifactId>liquibase-core</artifactId>
	<version>${liquibase.version}</version>
</dependency>
```
7. execute
```sh
liquibase generateChangeLog --username=$DATABASE_USER --password=$DATABASE_USER_PASSWORD --url jdbc:postgresql://localhost:5432/postgres --changeLogFile src/main/resources/db/changelog/changelog-1.0.sql
```
in the project root directory. (Assuming you are on postgres, otherwise reuse the db URL inside your `application.properties`)
