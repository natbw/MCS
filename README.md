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
d1 = Die(faces) # create die with 6 faces
```

Create a Game object:

```
d1 = Die(np.array([1,2,3,4,5,6]))
d2 = Die(np.array([1,2,3,4,5,6]))

game = Game([d1,d2]) # create game with 2 of the same die
game.play(10) # roll each die for 10 rounds
```

Create an Analyzer:

```
game = Game([d1,d2]) 
analyzer = Analyzer(game) # create analyzer to analyze game
```



## API Description

Below is a list of all classes along with methods and attributes
associated with each class. 

**Die Class**

- Die(faces)
    - Description: Initializes die with given faces.
    - Parameters: numpy array of distinct values.
    - Raises: `TypeError` if not numpy array, `ValueError` if faces not distinct.
    - Attributes: Die objects have faces and weights.
    
- change_weights(face, weight)
    - Description: Changes the weight of a given face.
    - Parameters: `face` to be changed and new `weight` to change to.
    - Raises: `IndexError` if face does not exist and `TypeError` if weight is not numeric.
    
- roll_die(num_rolls)
    - Description: Rolls die given number of times.
    - Parameters: `num_rolls` is number of rolls defaults to 1. 
    - Returns: List of outcomes from number of rolls. 
    
- show_state()
    - Description: Shows current faces and weight of Die object
    - Parameters: None
    - Returns: Dataframe of Die faces and weights.

**Game Class**

- Game(faces : np.ndarray)
    - Description: Initializes die with given faces
    - Parameters:
    - Raises:
    - Attributes:
    
- play_game(faces : np.ndarray)
    - Description: Initializes die with given faces
    - Parameters:
    - Raises:
    - Attributes:
    
- show_results(faces : np.ndarray)
    - Description: Initializes die with given faces
    - Parameters:
    - Raises:
    - Attributes:

**Analyzer Class**

- Analyzer(faces : np.ndarray)
    - Description: Initializes die with given faces
    - Parameters:
    - Raises:
    - Attributes:

- jackpot_counts(faces : np.ndarray)
    - Description: Initializes die with given faces
    - Parameters:
    - Raises:
    - Attributes:

- face_counts(faces : np.ndarray)
    - Description: Initializes die with given faces
    - Parameters:
    - Raises:
    - Attributes:

- combo_counts(faces : np.ndarray)
    - Description: Initializes die with given faces
    - Parameters:
    - Raises:
    - Attributes:
    
- permutations(faces : np.ndarray)
    - Description: Initializes die with given faces
    - Parameters:
    - Raises:
    - Attributes: