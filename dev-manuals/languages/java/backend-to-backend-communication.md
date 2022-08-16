For backend to backend communication we use [OpenFeign](https://spring.io/projects/spring-cloud-openfeign). 
To set up the feign client, you need to include the following dependencies in the `pom.xml`.

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

To implement the feign client into a spring boot project,  
you have to do the following in your source code:

This is an example to send a minigame result from the chickenshock-backend to the overworld-backend.

Add `@EnableFeignClients` to your ServiceApplication file.

```java
@SpringBootApplication
@EnableFeignClients
public class ChickenshockServiceApplication {
```

Add an ResultClient like this:

```java
package de.unistuttgart.chickenshockbackend.clients;

import de.unistuttgart.chickenshockbackend.data.OverworldResultDTO;
import feign.Headers;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.PostMapping;

@FeignClient(value = "resultClient", url="${overworld.url}/internal")
public interface ResultClient {
    @PostMapping("/submit-game-pass")
    @Headers("Content-Type: application/json")
    void submit(OverworldResultDTO resultDTO);
}
```

Import the client in your service like this:

```java
@Autowired
ResultClient resultClient;
```

And then call the method like this:

```java
OverworldResultDTO resultDTO = new OverworldResultDTO("CHICKENSHOCK", gameResultDTO.getConfigurationAsUUID(), 50, "1");
resultClient.submit(resultDTO);
```

To set the url of the overworld backend you need to add this to you application.properties file.

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
