# RegexGame

_RegexGame_ is a minigame for the _Gamify-IT_ platform.

## About the game

The goal of _RegexGame_ is to find strings matching a given regex.

## Configuration

Property|Description|Possible Values|Recommended values
-|-|-|-
Riddle Time|How many seconds the player has to solve a given riddle. The timeout will accumulate over the rounds, so the configured time will be added to the countdown with every solved riddle.|Any positive integer|10-30
Amount of answers|How many answers the system should try to generate for each riddle.|any positive integer|2-5
Necessary rounds for completion|How many rounds the player has to solve for this game to be considered "complete", and thus marked as 100% in the overworld.|any positive integer|10-30
Regex Structures|Which regex structures will appear in this game. [See the list below](#regex-structures)|any combination with at least one structure|character sequence and 4 other structures

## regex structures

Source:
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Cheatsheet

Name|Example|Description
-|-|-
Single character|`a`|Matches the given single character literally
Character sequence|`ab`|Matches the given character sequence literally
Any single character|`.`|Matches any single character
Group|`(ab)`|
Character class|`[ab]`|Matches any of the enclosed characters
Inverted character class|`[^ab]`|Match any character except the enclosed characters
Disjunction|`(a\|b)`|Match any of the sequences seperated by `\|`
Any-amount quantifier|`*`|Match previous sequence zero or more times
At-least-one quantifier|`+`|Match previous sequence one or more times
Optional quantifier|`?`|Match previous sequence zero or one time
Absolute numeric quantifier|`a{n}`<br>`a{n,}`<br>`a{n,m}`|Match the previous sequence exactly `n` times<br>Match the previous sequence at least `n` times<br>Match the previous sequence between `n` and `m` times
