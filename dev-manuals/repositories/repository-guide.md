# Repository Guide

## Repository name

All repositories must be named in kebab-case without capital letters.
Repository names **must not** include _Gamify-IT_ in their name.

## README name

READMEs must be named exactly the following: `README.md`

## Branch names

- bug fix: `bugfix/$bugname`
- feature: `feature/$featurename`
- documentation: `documentation/$documentationaction`
- maintenance: `maintenance/$maintenanceaction`

The part behind the specifying action should be written in kebab-case without uppercase letters.

## How to commit

Commit messages should be able to complete the following sentence: _If applied, this commit will_  
For example `If applied, this commit will update getting started documentation`.  
If something is unclear, you can read more about it [here](https://cbea.ms/git-commit/).  

## Issue Tags

1) The issue has to be **tagged** correctly, especially distinguishing between `bug`, `feature`, `documentation`, and `maintenance`.
    - `bug`: A bug in the program that was discovered.
    - `feature`: A new feature is requested and explained in detail.
    - `documentation`: An additional piece of documentation is requested.
    - `maintenance`: The issue relates to project maintenance and does not directly affect the program.
         - This includes especially refactorings and package upgrades.

## Pull Requests

1. At the end of the PR's description, the corresponding issue should be referenced in **one** of the following ways:
    - if the PR fixes a bug, the `Fixes` prefix shall be used. (e.g. Fixes #5)
    - if the PR closes another issue type, the `Closes` prefix shall be used. (e.g. Closes #5)
    - if more than one issue is closed by this PR, each `Fixes`/ `Closes` should be on a separate line.
2. If a PR is not ready to by merged by means of the author, he should tag the PR with the `WIP:` prefix.
3. Merging Requirements for a PR:
    - At least 2 approvals are required. This can be shortened to 1 approval if the PR changes less than 10 lines. GitHub only allows more than one reviewer if the repository is public
    - No pending requested changes
    - If the PR fixes issues, all such issues must be mentioned with `Fixes` or `Closes` in the PR description
    - No `WIP:` prefix
    - All **CI** jobs passed
4. A new contribution to the branch invalidates all preceding approvals.
5. `Force Pushes` should be avoided at all costs. Exceptions are:
    - Security relevant data was pushed and has to be removed from the history
    - Large files which should not remain in the repository were pushed
6. Every maintainer of the project is allowed to merge the PR **if all merge criteria in #3 are fulfilled**.

## Clean Code

1. Writing clean code shall always be prioritized before other targets, especially development speed.
2. Favor readability over consciseness, try to use appropriate identifiers instead of comments to document your code.
3. Add documentation where it is useful, avoid boilerplate comments.

## General Guidelines for Good Measures

1. Users should be referenced by their user names using an `@` and not by their real names or other aliases.
2. Jokes or non-constructive contributions are allowed as long as they don't hinder the development workflow and inhibit professional conduct.
3. The language used is English. Unless you are talking about something related to `i18n` or `l10n`, no other language will be accepted.
    - If you write a message in another language, you will be asked to translate it into English before any further communication can occur
