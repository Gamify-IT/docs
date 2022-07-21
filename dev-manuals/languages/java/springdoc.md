# Lombok
For documenting our spring REST-API we use [SpringDoc-OpenAPI](https://springdoc.org/).
Please include it as a dependency in maven projects by adding this in the `pom.xml`:

```xml
<properties>
  ...
  <org.springdoc.version>1.6.9</org.springdoc.version>
  ...
</properties>

<dependencies>
  ...
  <dependency>
		<groupId>org.springdoc</groupId>
		<artifactId>springdoc-openapi-ui</artifactId>
		<version>${org.springdoc.version}</version>
	</dependency>
  ...
</dependencies>

```
Also add the path of the page in `application.propteries`:

```properties
springdoc.swagger-ui.path=/swagger-ui
```