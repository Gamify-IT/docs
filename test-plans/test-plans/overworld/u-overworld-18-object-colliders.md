# Overworld: Object colliders (`u.overworld-18`)

Version: V1.1, 2022-08-11, adapt to new template \
Author: Michael Linder, Florian Wüst

## Description

This use case verifies that the object colliders work as intended.  

## Precondition

Overworld is loaded

## Postcondition

The tester couldn't go behind objects where he is not supposed to get.  
The player model isn't visible when he stands behind an object that is larger than him.

## Typical procedure

1. The tester walks around and checks that all colliders on `houses` are correct
2. Same for `stones`
3. Same for `benches`
4. Same for `fences`
5. Same for `bushes`

## Alternative procedures

N/A

## Criticality

High

## Linkages

N/A
