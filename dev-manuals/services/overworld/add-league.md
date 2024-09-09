# Add league 

## Overview

Over time, the number of games and worlds may increase, requiring the expansion of leagues therefore also the 
ranges between the leagues can change.


## How to add a league and/or change the ranges between the leagues

To add a league or change the range, you need to add it to the [overworld](https://github.com/Gamify-IT/overworld) and 
the [overworld backend](https://github.com/Gamify-IT/overworld-backend).

## Overworld Backend 

The league of a player is calculated directly in the PlayerStatisticData class of the overworld frontend. Currently we have 
four leagues ("Wanderer","Explorer","Pathfinder","Trailblazer").

So if there is a new league or the range changes one can easily change it in the calculateLeagueOfPlayer(..) method.