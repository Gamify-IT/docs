
# $CATEGORY: $ACTION (`$TESTCASE_ID in format "u.$(kebab-case $CATEGORY)-$NUMBER (from 1)"`)

Version: `v$X.$Y with $X >= 1, $Y >= 0`, `$NOW in YYYY-mm-dd`, `$CHANGE_DESCRIPTION like a git commit` \
Author: Authors of this file, comma-separated
(Delete this line in test cases!) Filename: `$(kebab-case u-$CATEGORY-$NUMBER-$ACTION).md`

## Description

Maximum of **3 concise** sentences about the realized function.

## Precondition

Precondition for starting the use case.

## Postcondition

Postcondition after the use case has ended.

## Typical procedure

1. Do `x`
2. Do `y`

## Alternative procedures

<!-- Do not show errors here, only intended alternatives in format -->
1.1. `condition` - do `x2` \
2.1. `condition 2` - do `y2`

## Criticality

Importance of the use case for the entire system
(High, Medium, Low)

## Linkages

<!-- To refer to another testcase, use -->

`- [$REFERENCED_ACTION (`$REFERENCED_ID`)]($PATH)`
