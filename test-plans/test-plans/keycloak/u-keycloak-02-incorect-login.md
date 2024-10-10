# Keycloak: incorect login (`u.keycloak-02`)


Version: V1.0, 25.09.2022 \
Author: Leon Layer

## Description

Login fails because of wrong login data.

## Precondition

No user is logged in. If the user was logged in, he has logged out so that he is no longer logged in via the cookies in the browser.

## Postcondition

The user is not redirected and sees a message that his input was not correct.

## Typical procedure

1. Open the landing-page
2. Go to login
3. Fill in incorrect username or incorrect email and or incorrect password. (at least one is wrong)
4. Choose sign in

## Alternative procedures


## Criticality

High

## Linkages

- [Standard login (`u.keycloak-1`)](u-keycloak-01-standard-login.md)
- [Logout (`u.keycloak-3`)](u-keycloak-03-logout.md)
