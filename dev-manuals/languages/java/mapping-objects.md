# Mapping Objects
Because we do not want to write big code to map a DTO to a sprint database object, we use a mapper. 
For this we use [Mapstruct](https://mapstruct.org/). 
Please include them as a dependency in the maven projects by adding this in the `pom.xml`:

```xml
<properties>
  ...
  <org.mapstruct.version>1.5.2.Final</org.mapstruct.version>
  ...
</properties>

<dependencies>
  ...
  <dependency>
    <groupId>org.mapstruct</groupId>
    <artifactId>mapstruct</artifactId>
    <version>${org.mapstruct.version}</version>
  </dependency>
  ...
</dependencies>
```

A nice and quick tutorial how to use with spring is can be found at <https://www.baeldung.com/mapstruct>.