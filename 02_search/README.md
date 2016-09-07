# Week 2
Plan/notes for group lecture September 8th 2016
# Info
* [GitHub repository for this course](https://github.com/olehermanse/INF3490-AI_Machine_Learning)
    * Submit an issue if you find an error/mistake.
    * Or: Fix it yourself and make a pull request.
    * Or: E-mail me if you don't use github: [olehelg@uio.no](mailto:olehelg@uio.no)
* [Exercises and solutions](https://github.com/olehermanse/INF3490-AI_Machine_Learning/tree/master/material)

# Python intro
* Last week: printing, variables, lists, dicts, plotting, matrices,

## 'Simple' search algorithms
* Draw Hill Climber in 3D.
* Draw Greedy Search in 3D.
* (Python) [Exhaustive search in 2D.](./01_exhaustive.py)
* Draw Exhaustive Search in 3D.

## Gradient ascent
* Mathematics/formula focus - gradient(derivative) is required.
* (Python) [Gradient ascent in 2D.](./02_gradient.py)
* Gradient ascent in 3D ideal case:
    * f(x,y) = 1 - x^2 - y^2
    * df(x,y) = (-2x,-2y)
    * How do you determine step size, gamma?
* Problems with gradient ascent
    * Local optima
    * Step size
* Gradient ascent vs 'simple' search algorithms

## Terminology and representations
* Approaching *hard* problems (Why take this course).
* Problem
    * Goal / Concept / What needs to be done
    * Constraints and requirements
* Solution
    * Representations
    * Some way to score / compare solutions (fitness function)
* Algorithm to find solutions

## Mandatory assignment 1
* Travelling Salesman Problem
    * Few cities vs. more cities
    * Distances, not coordinates
* Representation
