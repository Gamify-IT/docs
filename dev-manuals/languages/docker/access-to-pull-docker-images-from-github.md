# How to pull docker images from GitHub

1. Go to <https://github.com/settings/tokens> and get an existing access token (PAT). Alternatively, you can create a new one, but do not forget to include the `read:packages` permission.
1. Copy the token
1. Run `docker login ghcr.io -u $GITHUB_USERNAME -p "$COPIED_TOKEN"`
