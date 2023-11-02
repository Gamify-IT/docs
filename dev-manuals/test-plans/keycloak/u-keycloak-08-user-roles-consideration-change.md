# Keycloak: user role change (`u.keycloak-08`)


Version: V1.0, 25.09.2022 \
Author: Leon Layer

## Description

A user who was previously not a lecturer is allowed to do all lecturer-only things once he is promoted to `lecturer`.  

## Precondition

A user without lecturer status is logged in. The user is on the start page. The user is not offered the option to open the lecturer interface.

## Postcondition

The user sees the lecturer interface.

## Typical procedure

1. The user gets the role `lecturer` through the Keyloak admin console.
2. The logged in user waits until the role change is processed by the server.
3. The user reloads the page
4. The user navigates to the start page.
5. The user chooses lecturer interface

## Alternative procedures


## Criticality

Medium

## Linkages

- [Create course (`u.lecturer-interface-2`)](../lecturer-interface/u-lecturer-interface-02-create-course.md)
- [Show specific course (`u.lecturer-interface-3`)](../lecturer-interface/u-lecturer-interface-03-show-specific-course.md)
