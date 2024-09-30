# Lecturer-Interface: Import and Export minigame configuration (`u.lecturer-interface-28`)


Version: V1.0, 14.09.2022 \
Author: Max Kästner

## Description

Any minigame configuration can be exported and imported trough a configuration file.

## Precondition

At least one minigame is configured. The tester is located where the minigames can be configured.

## Postcondition

Another minigame was configured with the same configuration of the existing minigame.

## Typical procedure

1. Click the edit button of a minigame
2. A modal opens with the existing configuration
3. Press the export button
4. A configuration file was downloaded from the browser
5. Close the modal
6. Configure a minigame with the same game type
7. Click the edit button of the new minigame
8. Click import configuration
9. Select the previously downloaded file
10. The configuration is shown in the modal with a success message
11. Press the Ok button of the modal to save the configuration


## Alternative procedures

_N/A_

## Criticality

Medium

## Linkages

- [Change game of minigame spot (`u.lecturer-interface-12`)](u-lecturer-interface-12-change-game-of-minigame.md)
- [Edit minigame configuration of chickenshock (`u.lecturer-interface-13`)](u-lecturer-interface-13-edit-minigame-configuration-chickenshock.md)