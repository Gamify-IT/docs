# Test data management

## Introduction

Since we have a lot of separate databases (at least one for each backend), we need to have an easy way to initialize them with test data.
For our [test plans](../test-plans/index.rst) it is also important that different sets of test data can be loaded into the databases.

We manage this test data in a dedicated repository called [test-data](https://github.com/Gamify-IT/test-data).

## Data format

The test data is stored as SQL files in the `test-data` repository. The files are named in the following way:

- For PostgreSQL databases: `postgres/<service>/<test-data-set>.sql`

By default, our [development docker-compose files](../../dev-manuals/languages/docker/docker-compose.md) will load the `default.sql` file, they [can be configured to load other data sets](https://github.com/Gamify-IT/test-data#container-usage).

## Creating a data set for a new service

When you want to add a data set for a new service, you can create a new directory in the `test-data` repository.
The directory name **must match** the name of the database container in the docker-compose files (omitting the `-db` postfix).

For example, if you have a database container called `overworld-db`, you can create a directory called `overworld` in the `postgres` directory.

To create the `.sql` file, just start your service, initialize it with the desired test data (e.g. via Postman), and run the following command:

```bash
# example command to export the overworld-db to a file named default.sql
docker exec overworld-db pg_dump --username postgres postgres > default.sql
```

Commit the file with a message like `Add default test data for overworld`.

## Updating a test data set

If you want to update an existing dataset (for example the `default.sql` file), first load the existing data set into the database.
You can do this by running your service with one of the [development docker-compose files](../../dev-manuals/languages/docker/docker-compose.md).

Make the desired updates (e.g. by sending requests to the service using Postman) and then export the data set using the following command:

```bash
# example command to export the overworld-db to a file named default.sql
docker exec overworld-db pg_dump --username postgres postgres > default.sql
```

Completely replace the contents of the existing `.sql` file with the newly exported data.

Commit the file with a message stating the changes you made (For example `Add more minigame spots to overworld/default.sql`).
