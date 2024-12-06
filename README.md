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

To import the package with each class:

`from montecarlo.msc import Die, Game, Analyzer`

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

- Game(dice : list)
    - Description: Initializes a Game object with list of Dice objects.
    - Parameters: `dice` a list of valid Die objects.
    - Raises: `TypeError` if die are not a list of Die objects and `ValueError` if die do not all have the same face number and values.
    
- play_game(rolls : int)
    - Description: Rolls all dice a given number of times and stores results.
    - Parameters: `rolls` number of times to roll die.
    
- show_results(form='wide' : str)
    - Description: Returns dataframe of results from game play in narrow or wide format
    - Parameters: `form` must be string of 'wide' or 'narrow'
    - Raises: `ValueError` if term is not 'wide' or 'narrow'

**Analyzer Class**

- Analyzer(game : Game object)
    - Description: Initializes Analyzer object with Game object results and information.
    - Parameters: `game` must be a single Game object type.
    - Raises: `ValueError` if not of Game object type.

- jackpot_counts()
    - Description: Counts the number of times a roll resulted in all the same face value and returns integer count value.

- face_counts()
    - Description: Computes the number of times each face was rolled in each round and returns dataframe of results.

- combo_counts()
    - Description: Computes the unique combinations of faces rolled along with the number of times that unique combination occurred and returns result in a dataframe.
    
- permutations()
    - Description: Computes unique permutations of faces rolled along with the number of times that unique permutation occurred and returns results in a dataframe.
