# Architecture of Overworld-backend

Project: <https://github.com/Gamify-IT/overworld-backend> \
Classes: <https://github.com/Gamify-IT/overworld-backend/tree/main/src/main/java>

## Purpose

This backend saves the different overworld configurations and general player statistics. 

## General code structure

This backend has the following package structure
- `data`: Contains the data objects and DTOs
- `controller`: Containers the server routes
- `service`: Contains the business logic
- `client`: Contains the b2b (backend-2-backend) communication methods
- `repositories`: Contains the database repositories

## Starting the service

See the [README](https://github.com/Gamify-IT/overworld-backend#readme).

## What to look at

_Everything_

## What to ignore

_NA_

## Known Design Flaws

- some API routes have suboptimal paths
- cloning only works for chickenshock and other minigames without a configuration id
- current unlocking order 
(unlocking the remaining dungeons first and then the next world) is disputed, 
might be changed in the future

## Known Bugs

An up-to-date list of open bugs can be found at <https://github.com/orgs/Gamify-IT/projects/6/views/11> by searching for `Overworld-backend`.

## Tests

In general, the following things are tested for Overworld-backend:
- Everything is tested with unit tests
