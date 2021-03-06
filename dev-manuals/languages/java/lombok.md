# Lombok
Because we do not want to write big domain classes with all their getters, setters, and constructors, we want to make the code more readable by using [Lombok](https://projectlombok.org/).
Please include them as a dependency in the maven projects by adding this in the `pom.xml`:

```xml
<properties>
  ...
  <lombok.version>1.18.24</lombok.version>
  ...
</properties>

<dependencies>
  ...
  <dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>${lombok.version}</version>
    <scope>provided</scope>
  </dependency>
  ...
</dependencies>

```