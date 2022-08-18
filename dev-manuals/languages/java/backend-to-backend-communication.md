# Backend-to-Backend communication in spring boot

For backend-to-backend communication we use [OpenFeign](https://spring.io/projects/spring-cloud-openfeign). 
To set up the feign client, you need to include the following dependencies in your `pom.xml`:

```xml
<properties>
    <spring-cloud.version>2021.0.3</spring-cloud.version>
</properties>
```

```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-openfeign</artifactId>
</dependency>
```

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-dependencies</artifactId>
            <version>${spring-cloud.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

To implement the feign client into a spring boot project, you have to perform the following steps 
(the example is based on communication from chickenshock-backend to overworld-backend):

Annotate  your `Application` or `Configuration` class with `@EnableFeignClients`. Preferably `Configuration`, if present.

```java
@SpringBootApplication
@EnableFeignClients
public class ChickenshockServiceApplication {
```

Add a `ResultClient`:

```java
package de.unistuttgart.chickenshockbackend.clients;

import de.unistuttgart.chickenshockbackend.data.OverworldResultDTO;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.PostMapping;

@FeignClient(value = "resultClient", url="${overworld.url}/internal")
public interface ResultClient {
    @PostMapping("/submit-game-pass")
    void submit(OverworldResultDTO resultDTO);
}
```

Import the client into your service:

```java
@Autowired
ResultClient resultClient;
```

And then call the method:

```java
OverworldResultDTO resultDTO = new OverworldResultDTO("CHICKENSHOCK", gameResultDTO.getConfigurationAsUUID(), 50, "1");
resultClient.submit(resultDTO);
```

To set the URL of the overworld backend you need to add the value to your `application.properties`:

```properties
overworld.url = http://localhost/overworld/api/v1
```

For this example to work, you also need to add the following class:

```java
package de.unistuttgart.chickenshockbackend.data;

import java.util.UUID;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class OverworldResultDTO {

    String game;
    UUID configurationId;
    long score;
    String userId;
}
```
