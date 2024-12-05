# IMPORT LIBRARIES
import pandas as pd
import numpy as np
import random

#############
# DIE CLASS #
#############

class Die:
    
    """
    A class used to represent a Die or any discrete random variable associated
    with a stochastic process such as deck of cards or flipping a coin. A die
    has N sides or faces and W weights and can be rolled any number of times.
    At time of initialization, Die weights are set to a default of 1 (fair die)
    but can be changed after the object is created. 

    Attributes
    ----------
    faces : numpy array
        Values may be strings or numbers and must be distinct.
    weights : int or floats
        Positive numbers (integers or floats, including 0)
    _settings : DataFrame
        Private attribute for storing die faces and weights. Not to be
        manipulated directly, but documented for clarity.

    Methods
    -------
    __init__():
        Creates initial class object with faces and default weights.
    change_weights():
        Changes weight associated with specified face of class object.
    roll_die():
        Returns results from N rolls of class object.
    show_state():
        Returns dataframe of faces and weights associated with class object.
    __str__():
        Returns string representation of class object.
    """


    def __init__(self, faces):
        """
        Initialize an equal weighted Die object with given distinct faces.

        Parameters
        ----------
        faces : numpy array
            Values may be strings or numbers and must be distinct.

        Returns
        -------
        None.
        
        Raises
        ------
        TypeError
            If faces is not a numpy array data type.
        ValueError
            If values in faces are not distinct values.
        """
        
        # return TypeError if not a numpy array
        if not isinstance(faces, np.ndarray):
            raise TypeError('Die faces must be of numpy array dtype.')
        
        # return ValueError if faces not unique
        is_unique = len(np.unique(faces)) == len(faces)
        if not is_unique:
            raise ValueError('All Die faces must have distinct values.')
            
        # if no errors raised, create die object with faces and default weights
        self.faces = faces
        self.weights = np.ones(len(self.faces))
        
        # store die object settings to private dataframe with faces as index
        self._settings = pd.DataFrame(data = {'weights': self.weights},
                                      index = self.faces)
        self._settings.index.name = 'faces'
        
        return


    def change_weights(self, face, weight):
        """
        Change the weight of a given face from a Die object. Only supports
        one weight change at a time.

        Parameters
        ----------
        face : int, float, or str
            The face value to be changed.
        weight : int or float
            The new weight to be associated with the face.
        
        Returns
        -------
        None.
        
        Raises
        ------
        IndexError
            If given face value is not in the Die object's faces.
        TypeError
            If given weight is not numeric (integer or float) or castable as numeric.
        """
        
        # check if face passed is a valid value in the die and raises IndexError
        if not np.isin(face, self.faces):
            raise IndexError('Face not found in Die faces. Try again with different face or use Die.faces to view valid options.')
            
        # checks if weight is a valid type (integer or float) or castable as numeric and raises TypeError
        if not isinstance(weight, (int,float)):
            try:
                weight = float(weight)
            except:
                raise TypeError('Not a valid weight. Weight should be of type int or float or castable as numeric.')
        
        # if no errors, update weights and settings attributes with new weight
        new_weight = float(weight)
        self.weights[self.faces == face] = new_weight
        self._settings.loc[face] = new_weight
        
        return


    def roll_die(self, num_rolls=1):
        """
        Roll a Die object a given number of times. A random sample with
        replacement is generated that applies the associated weight.

        Parameters
        ----------
        num_rolls : int, optional
            Number of times Die object is rolled. The default is 1.

        Returns
        -------
        results : list
            A list of outcomes from a given number of rolls.
        """

        # make sure rolls entered is not less than 1
        if num_rolls < 1:
            print('Roll number cannot be less than 1. Setting to default 1 and rolling die.')
            num_rolls = 1
        
        # roll die and store as results
        results = random.choices(population = self._settings.index,
                                 weights = self._settings['weights'],
                                 k = num_rolls)
        
        # return results from roll
        return results


    def show_state(self):
        """
        Displays all the faces and weights associated with Die object.

        Returns
        -------
        states : dataframe
            A dataframe with faces and associated weights.
        """

        # return copy of private dataframe with faces and weights of die
        states = self._settings.copy(deep=True)
        
        return states


    def __str__(self):
        """
        Create string representation of class to check for
        class type in other objects

        Returns
        -------
        str rep of die object
        """
        
        return 'Die'


##############
# GAME CLASS #
##############

class Game:
    
    """
    A class used to simulate rolls with a Die class and consists of rolling
    one or more Die objects one or more times. A Game class must consist of
    Die class objects with the same number of sides and associated faces but
    may have varying weights among Die. A Game class plays a game with Die
    objects and stores results of recent game play.

    Attributes
    ----------
    dice : list
        A list of Die objects consisting of one or more similar Die objects.
    _game_results : DataFrame
        Private attribute for storing recent game play results. Not to be
        manipulated directly, but documented for clarity.

    Methods
    -------
    __init__():
        Creates initial class object with list of Die objects.
    play_game():
        Rolls Die objects a given number of times and saves results.
    show_results():
        Returns results from game play round.
    __str__():
        Returns string representation of class object.
    """
    
    
    def __init__(self, dice):
        """
        Initialize a Game object to perform game actions on one
        or more given Die objects.

        Parameters
        ----------
        dice : list
            A list of valid Die objects. Each Die object in a Game
            has the same number of sides and associated faces,
            but may have different weights.

        Returns
        -------
        None.
        
        Raises
        ------
        TypeError
            If die are not a list of Die objects
        ValueError
            If die do not all have the same face number and values.
        """

        # make sure game object is initialized with list of dice objects
        if not isinstance(dice, list):
            raise TypeError('Dice parameter must be of list type.')
        
        # if dice is of list type, loop through list and check for dice objects and equality
        for die in dice:
            # check for dice objects and raise error if needed
            if str(die) != 'Die':
                raise TypeError('Dice list does not contain all dice objects. Double check dice objects and try creating Game again.')
                
            # check each die's faces are equal to first die
            if not np.array_equal(dice[0].faces, die.faces):
                raise ValueError('Die objects do not have all the same face length and values. Make sure all die objects are the same for each Game.')

        # if no errors, assign list of die objects to game and create empty dataframe for results
        self.dice = dice
        self._game_results = pd.DataFrame()
        
        return


    def play_game(self, rolls):
        """
        Rolls Die objects a given number of times and compile results.

        Parameters
        ----------
        rolls : int
            Number of times the dice should be rolled.

        Returns
        -------
        None.
        """
        
        # make sure rolls entered is not less than 1
        if rolls < 1:
            print('Roll number cannot be less than 1. Setting to default 1 and playing game.')
            rolls = 1

        # if game already played, reset results dataframe to empty
        if not self._game_results.empty:
            self._game_results = pd.DataFrame()
            
        
        # create row/col names for game results based on dice faces and roll num    
        result_cols = [i for i in range(1,len(self.dice)+1)]
        idx = [i for i in range(1,rolls+1)]
        self._game_results = pd.DataFrame(columns=result_cols, index=idx)
        self._game_results.index.name = 'roll'
        
        # for each roll, roll each die, save results to dataframe in wide format
        for i in range(1, rolls+1):
            
            round_result = {}
            
            for j,d in enumerate(self.dice):
                result = d.roll_die(1)
                round_result[j+1] = result[0]
            
            self._game_results.loc[i] = round_result

        return


    def show_results(self, form='wide'):
        """
        Display dataframe of results of rolls, faces, and outcomes
        from game play.

        Parameters
        ----------
        form : str, optional
            The format of how the results should be displayed. Options are
            either 'wide' with faces as columns and roll number as rows
            or 'narrow' with rolls and faces as multiindex rows and one column
            with the roll outcomes. The default is 'wide'.

        Returns
        -------
        results : dataframe
            A dataframe of the most recent results from playing
            Game which rolls a given number of die a given number of times.
            
        Raises
        ------
        ValueError
            If given form is not 'narrow' or 'wide'.
        """
        
        # get copy of private dataframe to format for output
        results = self._game_results.copy(deep=True)
        
        # if dataframe is empty, advise playing game first
        if results.empty:
            print('No game has been played yet. Play game before viewing results.')
            return

        # if form is wide, just return results
        if form == 'wide':
            
            return results

        # if form is narrow, format dataframe and return narrow form
        if form == 'narrow':
            results = pd.DataFrame(results.stack())
            results.index.set_names(names='roll', level=0, inplace=True)
            results.index.set_names(names='die', level=1, inplace=True)
            results.rename(columns={0:'value'}, inplace=True)

            return results

        # if form is not wide or narrow, raise ValueError
        else:
            raise ValueError('Invalid option. Form must be "wide" or "narrow".')
            return
        
        
    def __str__(self):
        """
        Create string representation of class to check for
        class type in other objects

        Returns
        -------
        str rep of game object
        """
        
        return 'Game'


##################
# ANALYZER CLASS #
##################


class Analyzer:

    """
    A class used to analyze various descriptive statistical properties
    from results of a single Game object.

    Attributes
    ----------
    game : Game class
        A single game class with results from recent game play.

    Methods
    -------
    __init__():
        Creates initial Analyzer class object with Game object.
    jackpot_counts():
        Returns an integer of number of jackpots (same face each roll).
    face_counts():
        Returns dataframe of number of times each face was rolled.
    combo_counts():
        Returns dataframe of number of distinct combinations of faces rolled.
    permutations():
        Returns dataframe of number of distinct permutations of faces rolled.
    __str__():
        Returns string representation of class object.
    """    

    
    def __init__(self, game):
        """
        Initialize an Analyzer object to perform statistics on Game results
        Takes a game object as input parameter.

        Parameters
        ----------
        game : Game object
            A valid Game object to perform summary statistics on.

        Returns
        -------
        None.
        
        Raises
        ------
        ValueError
            If given game parameter is not a Game type object.
        """
        
        # check that game is of game object data type
        # try getting string representation of game class
        try:
            str(game)
        # if can't get str of parameter, raise error that parameter may not be of game object type
        except TypeError:
            print('Cannot retrieve str rep of object. Make sure parameter is valid game object.')
            
        # raise ValueError if game is not of game object type 
        if not str(game) == 'Game':
            raise ValueError('Invalid game parameter. Must be of Game object type.')

        # if no errors, assign game object to analyzer class
        self.game = game

        return


    def jackpot_counts(self):
        """
        Compute how many times in a game a roll resulted in which all faces
        were the same (e.g. all die rolled a one).
        
        Returns
        -------
        counts : int
            The number of times a roll resulted in all the same faces (jackpot).
        """
        
        # get results of rolls from game object
        results = self.game.show_results()
        
        # count the number of times rows had all the same values
        jackpots = results[results.nunique(axis=1) == 1]
        counts = int(jackpots.shape[0])
        
        # return total count of jackpots
        return counts


    def face_counts(self):
        """
        Compute the number of times each face was rolled in each round.

        Returns
        -------
        face_counts : dataframe
            Dataframe consists of the roll number (rows), face values(columns)
            and the number of times each face value occurred in each roll.
        """
        
        # get faces from dice
        faces = self.game.dice[0].faces
        
        # get row value counts from results
        results = self.game.show_results()
        counts = results.apply(lambda row: row.value_counts(), axis=1).fillna(0).astype('int')
        
        # create new dataframe with faces as columns and face_counts as values
        face_counts = pd.DataFrame(np.zeros((results.shape[0], len(faces)), dtype='int'),
                                   index = results.index,
                                   columns = faces)
        
        # Create new dataframe with counts of each face for each roll
        face_counts.update(counts)
        
        # return counts of each face of die
        return face_counts


    def combo_counts(self):
        """
        Computes the unique combinations of faces rolled along with the
        number of times that unique combination occurred.

        Returns
        -------
        combos : dataframe
            A dataframe consists of a MultiIndex of distinct combinations
            with a column associated with the number of counts.
        """

        # get results from game object
        results = self.game.show_results()

        # get all combinations of results and convert to sorted list
        data = results.to_dict(orient='tight')['data']
        combo_data = []
        for d in data:
            combo_data.append(sorted(d))

        # get value counts of all distinct combinations by sorting
        # combinations and counting how many each combo was rolled
        combo_counts = pd.DataFrame(sorted(combo_data)).value_counts()
        combos = pd.DataFrame(combo_counts)

        # return dataframe with combos and counts
        return combos


    def permutations(self):
        """
        Computes unique permutations of faces rolled along with the number
        of times that unique permutation occurred.

        Returns
        -------
        perms : dataframe
            A dataframe consisting of a MultiIndex of distinct permutations
            with a column associated with the number of counts.
        """
        
        # get results from game object
        results = self.game.show_results()
        
        # get all combinations of results and convert to list
        data = results.to_dict(orient='tight')['data']
        
        # get value counts of all distinct permutations
        perm_counts = pd.DataFrame(data).value_counts()
        perms = pd.DataFrame(perm_counts)
        
        # return dataframe with permutations and counts
        return perms
    
    
    def __str__(self):
        """
        Create string representation of class to check for
        class type in other objects

        Returns
        -------
        str rep of analyzer object
        """
        
        return 'Analyzer'
