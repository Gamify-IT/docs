# How to build Overworld Seminar

## Collider

Each sprite has a physics shape which defines its colider. Sprites without collider have a physics shape with three points that are all on top of each other.

## Grid Layers

```
ground
ground_decoration
wall
wall_decoration
objects
```

## Interactive objects

- Create prefabs for each interactive object

# Agends

- Boot Unity project
- Setup views
- - Scene/Game View
- - Tile Palette
- - - Switch between palettes
- - - Switch between layers
- - Inspector
- - Hierarchy
- - Project
- - Save view
- Drawing rules
- - Which tiles to use
- - What comes on what layee
- Drawing tools
- - Brushes
- - Shift click + Ctrl click
- Project rules
- - One branch
- - Frequent commits
- - Don't change tile palette to avoid merging issues
- How we work
- - Some impl. overworld
- - Some improve tilepalette
- - Some draw new/change sprites
- - Some impl. interactivity like npcs etc.
- - Some impl. a character
