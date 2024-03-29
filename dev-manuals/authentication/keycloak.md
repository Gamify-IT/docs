# Keycloak

We are using [Keycloak](https://www.keycloak.org) for user and access management.

When the user logs in, they receive a token. \
The token is stored in a cookie which is sent alongside every request to any backend.

## Table of contents

<!-- TOC -->
* [Backend](#backend)
  * [Access Token](#access-token)
  * [Validation and User Info](#validation-and-user-info)
    * [Recommended: Authentication-validator](#recommended-authentication-validator)
    * [Via Keycloak API](#via-keycloak-api)
* [Frontend](#frontend)
* [Development with Keycloak](#development-with-keycloak)
<!-- TOC -->

## Backend

### Access Token

The access token is sent as a cookie called `access_token` alongside every request. \
Below you see how to (always) require it for example in `Java` with `Spring`:

```java
@RestController
class MyRestController {
    @GetMapping("/")
    public SomeDAO someRequestHandler(@CookieValue("access_token") String accessToken) {
        // do something with the accessToken
    }
}
```

Requests without an access token should be rejected with [401 (Unauthorized)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401).

### Validation and User Info

#### Recommended: Authentication-validator

We have written a spring service which validates jwt access tokens issued by keycloak.

- The developer manual can be found [here](./authentication-validator.md).
- The program code can be found [here](https://github.com/Gamify-IT/authentification-validator).

#### Via Keycloak API

You can use the access token to get the user's ID, username, roles and other data. \
The userinfo endpoint of keycloak provides this information.

Locally, the user info endpoint has the URI `http://localhost/keycloak/realms/Gamify-IT/protocol/openid-connect/userinfo`. \
Or, under our reverse proxy under the URI `/keycloak/realms/Gamify-IT/protocol/openid-connect/userinfo`. \
You should make this URI configurable in your implementation.

Send a request with the header `Authorization: Bearer <accessToken>` to this endpoint. \
You then receive a JSON response with the user's information, which looks as follows:

```json
{
  "sub": "77451ff3-79c4-4503-8e46-869c377b593a",
  "email_verified": false,
  "realm_access": {
    "roles": [
      "default-roles-gamify-it",
      "student",
      "offline_access",
      "uma_authorization"
    ]
  },
  "preferred_username": "max",
  "given_name": "",
  "family_name": ""
}
```

Here is a short explanation of the most important fields:

- `sub` is the user's ID. It is guaranteed to be unique. It is a string which may not be a UUID.
- `preferred_username` is the username.
- `realm_access.roles` contains the user's roles. For students, it includes `student` and for lecturers it includes `lecturer`.

## Frontend

Frontends do not need the user's ID. \
The username can be read directly from the `localStorage` in the browser, using the key `username`.

```typescript
const preferredUsername = localStorage.getItem("username");
```

## Development with Keycloak

Locally, you can access keycloak at <http://localhost/keycloak>.

If you want to change its configuration, use the admin credentials described here: <https://github.com/Gamify-IT/test-data/tree/main/postgres/keycloak>.
