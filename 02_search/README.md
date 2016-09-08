# Week 2
Plan/notes for group lecture September 8th 2016
# Info
* [GitHub repository for this course](https://github.com/olehermanse/INF3490-AI_Machine_Learning)
    * Submit an issue if you find an error/mistake...
    * ... or fix it yourself and make a pull request...
    * ... or e-mail me if you don't use github: [olehelg@uio.no](mailto:olehelg@uio.no)
* [Exercises and solutions](https://github.com/olehermanse/INF3490-AI_Machine_Learning/tree/master/material)

# Python intro
* [The Zen of Python](https://www.python.org/dev/peps/pep-0020/)
    * "Beautiful is better than ugly."
    * "Simple is better than complex."
    * "Readability counts."
* Python is/has
    * Readable and beautiful
    * Easy and fast to write
    * Decent performance
    * Modern features
    * Functions and libraries to do *anything*.
* Last week - printing, variables, lists, dicts, plotting, matrices. (Basic examples that you should understand and be familiar with for this course)
* This week - classes:
    * Class vs instance(object)
    * self
    * instance method, class method, static method
    * Use classes and OOP (Object oriented programming) when it makes sense, not by default.

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

## Terminology, representations and problem solving
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
