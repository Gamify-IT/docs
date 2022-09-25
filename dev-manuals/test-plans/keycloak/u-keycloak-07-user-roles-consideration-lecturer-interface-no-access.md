# Keycloak: user roles consideration lecturer interface no access (`u.keycloak-07`)


Version: V1.0, 25.09.2022 \
Author: Leon Layer

## Description

A user without a lecturer role, is logged in. His role causes the lecturer interface to be not displayed on the start page.

## Precondition

A user without a lecturer role is logged in. 

## Postcondition

The possibility to open the lecturer interface is not displayed to the user.

## Typical procedure

1. Open the start-page (http://localhost/start)

## Alternative procedures


## Criticality

Medium

## Linkages

- [Create course (`u.lecturer-interface-2`)](u-lecturer-interface-02-create-course.md)
- [Show specific course (`u.lecturer-interface-3`)](u-lecturer-interface-03-show-specific-course.md)
