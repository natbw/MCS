# MCS
DS5100 Final Project Monte Carlo Simulator by Brian Natale


## Metadata

This project defines three related classes that allow for simulation of
various Monte Carlo experiments.

**Die** --> **Game** --> **Analyzer**

From these simulator classes, a 'Die' object can be any discrete random variable
associated with a stochastic process such as a deck of cards, the flipping
of a coin, or rolling an actual die.

A 'Game' object consists of rolling, flipping, etc. of one or more 'Die' objects
on or more times and compiling results of those rolls.

An 'Analyzer' object allows for further analysis of 'Game' object results 
such as frequent rolls as well as unique combinations and permutations.

## Synopsis

**Installation**

To install use the following command:

`pip install .`

**Importing Classes**

To import the package:

`montecarlo.msc import Die, Game, Analyzer`

**Usage**

Create a Die object:

```
import numpy as np

faces = np.array([1,2,3,4,5,6])
d1 = Die(faces)
```

Create a Game object:

```
d1 = Die(np.array([1,2,3,4,5,6]))
d2 = Die(np.array([1,2,3,4,5,6]))

game = Game([d1,d2])
```

Create an Analyzer:

```
game = Game([d1,d2])
analyzer = Analyzer(game)
```



## API Description

Below is a list of all classes along with methods and attributes
associated with each class. 

**Die Class**




**Game Class**




**Analyzer Class**







