# How to get access to pull docker images from GitHub

1. Goto [https://github.com/settings/tokens](https://github.com/settings/tokens) and get your created access token to pull docker images or create a new one.
1. Name it like you want, set the expiration date like you want.
1. check `read:packages`
1. Press `Generate Token`
1. Copy the token
1. Run `docker login ghcr.io -u GITHUB_USERNAME -p "COPIED_TOKEN"`
