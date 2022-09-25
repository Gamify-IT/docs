# Keycloak: user roles consideration change (`u.keycloak-08`)


Version: V1.0, 25.09.2022 \
Author: Leon Layer

## Description

If a user has been assigned the role of lecturer, that means that he can access the configurations of the overworld. After logging in, this user can call up the lecture interface on his start page to edit the course. This means that the lecturer interface is not displayed to a user without a lecturer role. If you change the role of this user to a lecturer, the lecturer interface is displayed.

## Precondition

A user without lecturer status is logged in. The user is not offered the option to open the lecturer interface on the start page.

## Postcondition

The user sees the lecturer interface.

## Typical procedure

1. The role of the logged-in user is changed in the Keylok admin console.
2. The logged in user waits until the role change is processed by the server.
3. The user reloads the home page
4. The user navigates to the start page.
5. The user chooses lecturer interface

## Alternative procedures


## Criticality

Medium

## Linkages

- [Create course (`u.lecturer-interface-2`)](u-lecturer-interface-02-create-course.md)
- [Show specific course (`u.lecturer-interface-3`)](u-lecturer-interface-03-show-specific-course.md)
