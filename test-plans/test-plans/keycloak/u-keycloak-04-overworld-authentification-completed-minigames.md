# Keycloak: Overworld authentification (`u.keycloak-04`)


Version: V1.0, 25.09.2022 \
Author: Leon Layer

## Description

When a player is logged in via keycloak his identity is used to load his score in the overworld. 
This means that when the user logs out and reloads the world after logging in again, already completed mini games keep their status as completed. 

## Precondition

A user is logged in and has already completed at least one mini-game.

## Postcondition

The user is logged in again and the completed minigames are still marked as completed in the overworld. 

## Typical procedure

1. User is logged in and sees the overworld from Precondition.
2. User logs out.
3. User deletes the cookies for the website and reloads the page.
4. User logs in and navigates to overworld from the Precondition.

## Alternative procedures


## Criticality

Medium

## Linkages

- [Standard login (`u.keycloak-1`)](u-keycloak-01-standard-login.md)
- [Incorect login (`u.keycloak-2`)](u-keycloak-02-incorect-login.md)
- [Overworld Authentification Unlocked Area (`u.keycloak-5`)](u-keycloak-05-overworld-authentification-unlocked-area.md)
