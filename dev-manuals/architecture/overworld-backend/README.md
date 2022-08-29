# Architecture of Overworld-backend

Project: https://github.com/Gamify-IT/overworld-backend \
Classes: https://github.com/Gamify-IT/overworld-backend/tree/main/src

## Purpose

This backend saves all the different configurations for the overworld 
and the player statistics for the configuration. 

## General code structure

`$STRUCTURE`,

This backend has the following package structure
- `data`: Contains the data objects and DTOs
- `controllers`: Containers the server routes
- `services`: Contains the business logic
- `clients`: Contains the b2b (backend-2-backend) communication methods
- `repositories`: Contains the database repositories

## Starting the service

See the [README](https://github.com/Gamify-IT/overworld-backend#readme).

## What to look at

_Everything_

## What to ignore

_NA_

## Known Design Flaws

- no known design flaws at the moment

## Known Bugs

An up-to-date list of open bugs can be found at <https://github.com/orgs/Gamify-IT/projects/6/views/11> by searching for `Overworld-backend`.

## Tests

In general, the following things are tested for Overworld-backend:
- Everything is tested with unit tests
