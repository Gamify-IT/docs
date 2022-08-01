# Test plans

Contains all test plans of all our services, and the test plan template.

## Folder structure

The test plans belong to their corresponding folder.  
For example, a test plan created for the Moorhuhn frontend:

```bash
test-plans/moorhuhn-frontend/plans
```

As soon as a tester has tested a feature according to a test plan, it has to be placed in the `executed` folder

## Naming convention

Test plan filenames should have the following structure:

```
name-service-backend/frontend.md
example:
highscore-moorhuhn-frontend.md
```

where `name` is the name of the feature the test plan covers

executed tests should be named

```
date-testername-name-service-backend/frontend.md
example:
2022-08-01-MichaelLinder-highscore-moorhuhn-frontend.md
```
