# Plant-Growth-Simulation
This is a python simulation of growth &amp; spread of invasive species

The code uses an array of 100*100 python classes, representing the spread of dandelions across a 100 × 100 meter field over the course of a year, divided into 24 half-month intervals. 

The field is dispersed into a grid, and each cell is a class object containing 2 objects: seed and puffball representing different stages of dandelion growth.

The simulation starts with an initial puffball in the top-left corner of the field. Dandelion seeds spread from existing puffballs to nearby cells, subject to constraints on seed density. The simulation incorporates a growth mechanism where seeds mature and turn into puffballs after reaching a standard threshold of 75 days (1.5 months).

The model tracks the state of the dandelion spread at each interval, generating a heat map to visualize the distribution of dandelions.
