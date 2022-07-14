# Code Format
We use [Prettier](https://prettier.io/) (more exactly the [maven-plugin](https://github.com/HubSpot/prettier-maven-plugin)) for formatting Java Code.
Please include them as a dev dependency in frontend projects by adding this in the pom.xml:
```xml
<properties>
  ...
  <!-- By default just re-write code with prettier -->
  <plugin.prettier.goal>write</plugin.prettier.goal>
  ...
</properties>

<build>
  <plugins>
    ...
    <plugin>
      <groupId>com.hubspot.maven.plugins</groupId>
      <artifactId>prettier-maven-plugin</artifactId>
      <version>0.16</version>
      <configuration>
        <prettierJavaVersion>1.5.0</prettierJavaVersion>
        <printWidth>120</printWidth>
        <tabWidth>2</tabWidth>
        <useTabs>false</useTabs>
        <ignoreConfigFile>true</ignoreConfigFile>
        <ignoreEditorConfig>true</ignoreEditorConfig>
        <!-- Use <inputGlobs> to override the default input patterns -->
        <inputGlobs>
          <!-- These are the default patterns, you can omit <inputGlobs> entirely unless you want to override them -->
          <inputGlob>src/main/java/**/*.java</inputGlob>
          <inputGlob>src/test/java/**/*.java</inputGlob>
        </inputGlobs>
      </configuration>
      <executions>
        <execution>
          <phase>validate</phase>
          <goals>
            <goal>${plugin.prettier.goal}</goal>
          </goals>
        </execution>
      </executions>
    </plugin>
    ...
  </plugins>
</build>

```

To check if the code is in right format run `mvn prettier:check` (Can be also used in github workflows, to check if code is formatted).
To format the code run `mvn prettier:write`.