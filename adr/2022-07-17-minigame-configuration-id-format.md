# Formats minigame configuration ID

Currently, we have no clear format on how to create the configuration IDs.
The configuration IDs generated by the minigame backends will be sent to the overworld backend so that they know which configuration should be loaded when entering a specific minigame.

## Format-Restriction

All chars must be in base64, `_`, or `-`.
No other chars are allowed.

## Possible Solutions

1) UUID format (See [java.util.UUID](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/UUID.html))
2) Integer
3) Format World-Dungeon-Task, e.g. `w1-d3-t3` (current)

## Chosen Solution

## Pro Chosen Solution

1) easy to use, unique, adaptable
2) -
3) -

## Contra Chosen Solution

1) -
2) Same configuration IDs in different minigame backends
3) Not adaptable