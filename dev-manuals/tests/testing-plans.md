# Testing  
## Testing strategy  
### How do we test?  
- Classical  
- Test driven  
- Test first  

### Test levels  
- Unit testing  
- Integration testing  
- System testing  
- Acceptance testing  

### Test methods  
- Smoke tests
- Performance tests  
- Fuzzy tests  
- Equivalence class testing  
- Requirements based  
- Regression tests  
- Black-/White/Grey-Box testing  

### Metrics  
What do we want to achieve?  
- code coverage of 75%  
- pass rate of 100%  

### Test automatisation  
- Unity games and frontends are tested before every merge in the main branch
- Unit tests are performed at every push(automated by CI-Server)  
- Integration tests are performed at every push(automated by CI-Server)  
- UI tests before every merge in the main branch  
- Architecture tests are performed when needed  

## Test tools  
### Frontend
Unit tests with **Jest** whenever possible.  
**Unity** games are tested manually.  

### Backend  
JHipster does a lot of stuff: [JHipster tests](https://www.jhipster.tech/running-tests/)  
- **Unit tests** using **JUnit 5** 
- **Integration tests** using **Spring Test Context framework**  
- **UI tests** with **Jest**  
- **Architecture tests** with **ArchUnit**  

Optionally, JHipster can also generates:
- **Performance tests** with **Gatling**
- **Behaviour-driven tests** with **Cucumber**  
- **Angular/React/Vue integration tests** with **Protractor**