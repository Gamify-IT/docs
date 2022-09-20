# Docs

This repo contains all documentation for the minigame platform. Repos might contain further information but all
information in this repo should be kept up to date.

## Structure

All files in this repo should be written in English and _Markdown_.

It is structured in the following way:

### [`/adr`](adr)

Contains the _Architecture Decision Records_, so which general design decisions have been made, which options were
possible, which were chosen and why.

### [`/dev-manuals`](dev-manuals)

Contains the developer manuals for the given repo or technology, meaning everything a developer needs to know about the
specific topic to be able to collaborate.

### [`/ops-manuals`](ops-manuals/README.md)

Contains the operations manual for the given repo, so how the user can start the given service.

Contains the user manual for the given repo, so how the user can start the given service.

### [`/protocols`](protocols)

Contains protocols of meetings regarding the given repo/ concept for the given day. Filenames are in the
format `YYYY-mm-dd-protocol.md`.

## README Structure

The READMEs of all repos should follow the overall structure of the [template README](template-README.md).
Important to note here is that the `How to run` and `Development Setup` instructions can and should be copy-pasteable
into the respective user- and dev-manual.
