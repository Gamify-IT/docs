# Overworld: Persistent Keybindings (`u.overworld-27`)

Version: v1.0, 2022-03-14, create test plan \
Author: Florian Wüst

## Description

This use case tests whether the keybinding changes are loaded and saved correctly in the backend.

## Precondition

The tester is logged in and at least the overworld and overworld backend are running.

## Postcondition

The changes to the keybindings are stored in the backend and are loaded at each start.

## Typical procedure

1. Start a course of your choice
2. Open the Keybindings Menu
3. Change a key to a valid different key
4. Close the Keybindings Menu
5. Go Back to the Course selection page
6. Start a course (it can be the same)
7. Check that the changed keybindings are loaded

## Alternative procedures

N/A

## Criticality

Medium

## Linkages

- [Change keybindings (`u.overworld-26`)](u-overworld-26-change-keybindings.md)
