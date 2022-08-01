# Structure of test plans

Contains all test plans of all our services, and the test plan template.

## Folder structure

The test plans belong to their corresponding folder.  
For example, a test plan created for the Moorhuhn frontend:

```bash
test-plans/moorhuhn-frontend/plans
```

As soon as a tester has tested a feature according to a test plan, it has to be placed in the `logs` subfolder of that service.

## Naming convention

Test plan filenames should have the following structure:

```bash
$ACTION-$SERVICE.md
```
So, for example
```bash
highscore-moorhuhn-frontend.md
```

where `$ACTION` is the name of the feature the test plan covers.

Test log filename format is
```bash
$DATE-$TESTER-$ACTION-$SERVICE.md
```
So, for example
```bash
2022-08-01-michael_linder-highscore-moorhuhn-frontend.md
```
