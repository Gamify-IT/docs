# General architecture

## Component Structure

![component diagram](diagrams/gamify-it-architecture.svg)

In general, _Gamify-IT_ can be split up into three main components: the _Overworld_, the _Lecturer Interface_, and the _Minigames_.  
Purpose:

- minigame: A small game to learn something by playing
- overworld: consists of areas you can walk around in, interact with your environment or start minigames
- lecturer interface: The allmighty configurator to configure what happens where in the overworld, or to set what is displayed in the minigames.

Every of these services has its own backend, except the lecturer interface whose backend is the overworld backend as well.

### Further aspects

For simplicities sake, the diagram above omits a few things:

- actually, the backends don't send the data without being asked but rather the frontends query the backends
- when a minigame completes, control is returned to the overworld
- when a minigame run is finished, the respective minigame backend lets the overworld backend know about that as well

## Typical User Procedure

![sequence diagram](diagrams/sequence-diagram.svg)

As you can see, the user first has to login, and is then forwarded to the overworld, where he can then at some point start a minigame and finish it.

## Alternative component diagram

The following is an alternative component diagram which is more formally correct, but also a lot harder to read:

![alternative component diagram](diagrams/component-diagram.svg)
