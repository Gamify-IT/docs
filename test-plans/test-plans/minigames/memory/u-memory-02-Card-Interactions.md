# Memory: Card Interactions(`u.memory-2`)

Version: V1.0, 17.02.2023 
Author: Patrick Ng, Maximilian Wohlfarth

## Description

This use case verifies that the cards are markdown compatible, display pictures and can be enlarged.

## Precondition

Correct data is transfered into pairs for the memory game.
The data includes markdown and pictures.
Singleplayer game has been started.

## Postcondition

The cards are able to display markdown, pictures and can be enlarged for a detailed view.
Regardless where the cards are located (left box, summary box) the cards are correctly displayed.

## Typical procedure


1. Flip a card 
2. If the flipped card contains markdown look at it and try to enlarge it by clicking on the plus in the lower left corner.
3. Markdown should be correcly displayed even if its enlarged. Now close the detail view and look for its match.
4. If the flipped card contains a picture look at it and try to enlarge it by clicking on the plus in the lower left corner.
5. The picture should be correcly displayed even if its enlarged. Now close the detail view and look for its match.
6. Repeat the process till no card is left
7. Scroll through the summary and look at the markdown cards and picures. They should be correctly displayed.
8. Click on ones plus in the lower left corner and lookk at the enlarged view. If the enlargement of the card is correct, close it 
9. Repeat the process with all the other cards

## Alternative procedures

N/A

## Criticality

High

## Linkages
