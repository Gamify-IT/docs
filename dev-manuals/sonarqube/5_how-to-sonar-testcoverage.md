# How to sonar testcoverage

## Go
1) add <br> 
        `- run: go mod download` <br> 
        `- run: go generate` <br> 
        `- name: Unit Tests with Coverage` <br> 
        `run: go test -coverprofile=coverage.out ./...` <br> 
        to `sonarqube-build.yml`
---

## Spring Boot
1) add `run: mvn -B verify org.sonarsource.scanner.maven:sonar-maven-plugin:sonar -Dsonar.projectKey=chickenshock-backend -Dsonar.coverage.jacoco.xmlReportPaths=target/site/jacoco/jacoco.xml,target/site/jacoco-it/jacoco.xml,build/reports/jacoco/test/jacocoTestReport.xml` to `sonarqube-build.yml`
1) add <br>
            `<plugin>` <br>
				&nbsp;&nbsp;&nbsp;&nbsp;`<groupId>org.jacoco</groupId>` <br>
				&nbsp;&nbsp;&nbsp;&nbsp;`<artifactId>jacoco-maven-plugin</artifactId>` <br>
				&nbsp;&nbsp;&nbsp;&nbsp;`<version>0.8.7</version>` <br>
                &nbsp;&nbsp;&nbsp;&nbsp;`<executions>` <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`<execution>` <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`<goals>` <br>
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`<goal>prepare-agent</goal>` <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`</goals>` <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`</execution>` <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`<execution>` <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`<id>report</id>` <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`<phase>prepare-package</phase>` <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`<goals>` <br>
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`<goal>report</goal>` <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`</goals>` <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`</execution>` <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`<execution>` <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`<id>generate-code-coverage-report</id>` <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`<phase>test</phase>` <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`<goals>` <br>
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`<goal>report</goal>` <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`</goals>` <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`</execution>` <br>
                &nbsp;&nbsp;&nbsp;&nbsp;`</executions>` <br>
		    `</plugin>` <br>
    to `pom.xml`
1) to test database add 
<pre>
# Service containers to run with runner-job
    services:
      # Label used to access the service container
      postgres:
        # Docker Hub image
        image: postgres
        # Provide the password for postgres
        env:
          POSTGRES_PASSWORD: [DB_PW_HERE]
        # Set health checks to wait until postgres has started
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          # Maps tcp port 5432 on service container to the host
          - 5432:5432 
</pre>
between `runs-on: self-hosted` and `steps` to `sonarqube-build.yml`

## Vue
1) add <br>
        `- run: npm ci` <br>
        `- name: Unit Tests with Coverage` <br>
        `run: npm run test:unit -- --coverage --testResultsProcessor=jest-sonar-reporter` <br>
    to `sonarqube-build.yml`
1) create `jest.config.js` in top directory
1) add <br>
    `module.exports = {` <br>
        &nbsp;&nbsp;&nbsp;&nbsp;`preset: '@vue/cli-plugin-unit-jest/presets/typescript-and-babel',` <br>
    `};` <br>
    to `jest.config.js`
1) execute `vue add unit-jest`
1) type `y`
1) execute `npm install jest jest-sonar-reporter ts-jest @vue/cli-service @vue/cli-plugin-typescript @types/jest --save-dev`
1) file folder `/tests/unit/example.spec.ts`
1) add <br>
    `describe('Example', () => {` <br>
        &nbsp;&nbsp;&nbsp;&nbsp;`test('true is true', () => {` <br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`expect(true).toBeTruthy();` <br>
        &nbsp;&nbsp;&nbsp;&nbsp;`});` <br>
    `});` <br>
to `/tests/unit/example.spec.ts`
