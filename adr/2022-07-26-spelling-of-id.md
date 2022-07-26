# How do we spell "ID" (and similar acronyms) in Code?

`ID` and all other acronyms are controversial identifiers for variables.  
We need an agreement on how to write it.  
The following pargraphs use only `ID` as example, but the result can be applied to every other acronym as well (`XML`, `HTTP`, `REST`, `RPC`, `JSON`, ...).

## Possible Solutions

1. `id` if there is no prefix, `-ID` otherwise (-> `lectureID`, `lectureDTO`, `LectureDTO`)
2. `id` if there is no prefix, `-Id` otherwise (class names included) (-> `lectureId`, `lectureDto`, `LectureDto`)
3. `id` if there is no prefix, `-Id` for variables, `-ID` for class names  (-> `lectureId`, `lectureDto`, `LectureDTO`)
4. `id` if there is no prefix, `-Id` for acronyms of a single word (i.e. `ID`), `-ID` for acronyms of multiple words (i.e. `XML`, `DTO`) (-> `lectureId`, `lectureDTO`, `LectureDTO`)

## Chosen Solution

- `id` if there is no prefix, `-Id` for variables, `-ID` for class names  (-> `lectureId`, `lectureDto`, `LectureDTO`)

## Pro 1)

- Correct spelling of acronyms

## Contra 2)

- Incorrect spelling of acronyms

## Pro 3)

- Conforms with the way many (Java) libraries handle it

## Contra 4)

- Confusing to enforce
