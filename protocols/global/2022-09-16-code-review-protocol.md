# Code Review Protocol 15.09.2022

- fairly good structure, documentation is mostly missing

# Hints E-Mail for the Code Review

- It would have been good to have mentioned starting points for where to start reading a repository
- The architecture overview would have been nice to get a quick overview

# Documentation

- Is often missing
- The architecture overview is missing
- Link to the docs is missing in the repos and their READMEs
- `dev-manuals/<architecture>` should also contain component diagrams or similar
- Structure of `README`s: First for users (what is it? What does it do? How do I start it?), then for developers (How is it structured?)

# Overworld Backend

- 2-space formatting not good
- Inline comments mean code is bad and should be refactored into submethods
- Use only `UUID`s instead of `int`s as ID
- `PlayerStatisticService`: no `instanceof`, line `168`: Magic number
- `MinigameTask`: overloaded constructor with `Optional` instead of `null`

# Chickenshock Backend

- Way too few documentation (i.e. in `DTO`s that could be used by clients to generate their own models)
- Preconditions were not checked
- `README` doesn't tell what it is and is only technical
- `GameResultService#saveGameResult` - still uses hardcoded course- and player IDs
- `JWTValidatorService`: indentantion is invalid, style errors such as missing `final`s, `get-` should be a query, not a command, `public` methods for `private` methods

# General positive feedback

- `Lombok` usage - omits language specifica
- `Slf4j` usage - omits `System.out.println()`
