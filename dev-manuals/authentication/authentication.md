# Authentication and user identification

When the user logs in, they receive a token.
The token is stored in a cookie which is sent alongside every request to any backend.

Every backend **must always** validate the token before processing any request.

## Data format

The cookie has the name `token` and contains a [JSON Web Token](https://jwt.io).

You can validate the token using one of the libraries listed here: https://jwt.io/libraries

When you parse the token, you receive the following data:
```json
{
  "id": "string",
  "name": "string"
}
```

- `id` uniquely identifies the user. All statistics and other information about a user should be associated with this value.
- `name` unique username. **Only for debugging.** Even though it is unique, users may be allowed to change it in the future.

## Identifying users

When a backend needs to store information related to a user, it **must** associate the data with the `id` from the token.
The `id` is guaranteed to be unique, and is the only permanent identifier for users.
