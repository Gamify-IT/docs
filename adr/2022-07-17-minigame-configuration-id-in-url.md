# How to handle minigame configuration ID as URL route

Currently, we handle the handover of configuration IDs to the minigame frontend with a URL fragment. \
After discussion with some team members, this solution is no longer preferred.

## Possible Solutions

- insert the ID into the route
    - `/api/minigames/$MINIGAME/$ID/`
    - for example: `/api/minigames/bugfinder/$ID/`
- keep the old solution (URL fragent)
    - `/api/minigames/$MINIGAME#$ID`
- send an email to the user and he copies it into the frontend

## Chosen Solution

## Pro Solution
- `/api/minigames/$MINIGAME/$ID/`
    - easy to understand and use

## Contra Solution
- `/api/minigames/$MINIGAME/$ID/`
    - changes needed in implementations of the old format
- old solution
    - very bad
    - cannot use the fragment for section-linking anymore
    - URL fragment is normally optional but mandatory in our case
- email
    - bad user experience
