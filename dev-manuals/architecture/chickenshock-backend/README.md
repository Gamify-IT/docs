# Architecture of Chickenshock-backend

Project: <https://github.com/Gamify-IT/chickenshock-backend> \
Classes: <https://github.com/Gamify-IT/chickenshock-backend/tree/main/src>

## Purpose

This backend saves relevant Chickenshock game data.

## General code structure

This backend has the following package structure
- `data`: Contains the data objects and DTOs
- `controllers`: Containers the server routes
- `services`: Contains the business logic
- `clients`: Contains the b2b (backend-2-backend) communication methods
- `repositories`: Contains the database repositories


## Starting the service

See the [README](https://github.com/Gamify-IT/chickenshock-backend#readme).

## What to look at

_Everything_

## What to ignore

_NA_

## Known Design Flaws

- no known design flaws at the moment

## Known Bugs

An up-to-date list of open bugs can be found at <https://github.com/orgs/Gamify-IT/projects/6/views/11> by searching for Chickenshock-backend.

## Tests

In general, the following things are tested for Chickenshock-backend:
- Everything is tested with unit tests