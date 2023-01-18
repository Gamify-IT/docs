# Keycloak: standard login (`u.keycloak-01`)


Version: V1.0, 25.09.2022 \
Author: Leon Layer

## Description

Standard login with user email and password.

## Precondition

No user is logged in. If the user was logged in, he has logged out so that he is no longer logged in via the cookies in the browser.

## Postcondition

The user is logged in and redirected to the start page where he can start or edit an "overworld" course.

## Typical procedure

1. Open the landing-page
2. Go to login
3. Fill in correct username or correct email and correct password 
4. Choose sign in

## Alternative procedures

3.1. An incorrect username, email, or password is entered - The user is not redirected and is notified that their input was incorrect

## Criticality

High

## Linkages

- [Incorect login (`u.keycloak-2`)](u-keycloak-02-incorect-login.md)
- [Logout (`u.keycloak-3`)](u-keycloak-03-logout.md)