# Add achievements

## Overview

Achievements are a good way to motivate players to do certain things.  
So, if you want to reward players for completing some task or simply want to guide the player in a specific direction, consider adding an achievement for that.

At the moment, achievements can only be added globally.  
This means that if you unlocked an achievement in one course, you've unlocked it in all courses present on this server.

## How to add an achievement

To add an achievement, you need to add it to the [overworld](https://github.com/Gamify-IT/overworld) and the [overworld backend](https://github.com/Gamify-IT/overworld-backend).

### Overworld Backend

You have to do the following in the overworld backend:

1. Add the title of the new achievement to the `AchievementTitle` enum, located at `src\main\java\de\unistuttgart\overworldbackend\data\enums`  
![backend enum of possible achievements](assets/achievement-backend-title-enum.webp)
2. Add all category keyword to the `AchievementCategory` enum, located at `src\main\java\de\unistuttgart\overworldbackend\data\enums`, if the keywords are not yet present  
![Category enum](assets/achievement-backend-category-enum.webp)
3. Add the achievement (with the `title`, `description`, the `name of the the image` to show, the `categories` and a `number` to reach) to the list in the `updatePlayerStatisticAchievements` in the `AchievementService` located at `src/main/java/de/unistuttgart/overworldbackend/service/` and add it to the `achievementRepository`.  
![Achievement creation](assets/achievement-creation.webp)

### Overworld

If the achievement is tracked in the overworld, you need to additionally do the following:

1. Add the title of the new achievement to the `AchievementTitle` script located at `Assets/Scripts/AchievementSystem`.  
![frontend enum of possible achievements](assets/achievement-title-enum.webp)

## How to track progress of an achievement

### General

To update the progress of a player of the achievement, you need to send a `PUT` request to the overworld backend to `/players/{playerId}/achievements/{achievementTitle}` with an `AchievementStatisticDTO` body containing the progress.
You can find the `AchievementStatisticDTO` class in the backend under `src/main/java/de/unistuttgart/overworldbackend/data/`.

### Overworld

If the achievement is tracked in the overworld, you can use the `UpdateAchievement`and `IncreaseAchievementProgress` functions of the `GameManager` singleton instance.  
![Achievement Progress](assets/achievement-progressing.webp)
