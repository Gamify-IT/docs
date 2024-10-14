# Keycloak: lecturer interface not linked for non-lecturers (`u.keycloak-07`)


Version: V1.0, 25.09.2022 \
Author: Leon Layer

## Description

A user who is not a lecturer is logged in. They will not see a link to the lecturer interface.

## Precondition

The user stays logged in. 

## Postcondition

The possibility to open the lecturer interface is not displayed to the user.

## Typical procedure

1. Open the start-page (http://localhost/start)

## Alternative procedures


## Criticality

Medium

## Linkages

- [Create course (`u.lecturer-interface-2`)](../lecturer-interface/u-lecturer-interface-02-create-course.md)
- [Show specific course (`u.lecturer-interface-3`)](../lecturer-interface/u-lecturer-interface-03-show-specific-course.md)
