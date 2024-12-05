# IMPORT LIBRARIES
import pandas as pd
import numpy as np
import random


# DIE CLASS
class Die:
    
    # TODO
    # class docstrings
    # method docstrings
    
    def __init__(self, faces):
        '''
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
        '''
        
        # TODO
        # input argument descriptions describe data types, formats, defaults
        # return TypeError if not a numpy array
        # return ValueError if faces not unique
        
        self.faces = faces
        self.weights = np.ones(len(self.faces))
        self._settings = pd.DataFrame(data = {'weights': self.weights},
                                      index = self.faces)
        self._settings.index.name = 'faces'
        
        
    def change_weights(self, face, weight):
        '''
        Change the weight of a given face from a Die object.

        Parameters
        ----------
        face : int, float, or str
            The face value to be changed.
        weight : int
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
        
        '''
        
        # TODO
        # check if face passed is a valid value in the die and raises IndexError
        # checks if weight is a valid type (integer or float) or castable as numeric and raises TypeError
        # checks weights are positive numbers including 0
        
        
        self._settings.loc[face] = weight
    
    
    def roll_die(self, num_rolls=1):
        '''
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
            
        Raises
        ------
        ValueError
            If number of rolls is not greater than or equal to 1.
        '''
        
        # TODO
        # checks number is given and is greater than 0
        # try and except
        
        results = random.choices(population = self._settings.index,
                                 weights = self._settings['weights'],
                                 k = num_rolls)
        
        return results
    
    
    def show_state(self):
        '''
        Displays all the faces and weights associated with Die object.

        Returns
        -------
        states : dataframe
            A dataframe with faces and associated weights.

        '''
        
        states = self._settings.copy(deep=True)
        
        return states


# GAME CLASS
class Game:
    
    def __init__(self, dice):
        '''
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
        ValueError
            If given die are not Die objects or do not all have the same faces.

        '''
        
        # TODO
        # check that Die objects exist in list and that all have the same faces
        
        self.dice = dice
        self._results = pd.DataFrame()


    def play_game(self, rolls):
        '''
        Rolls Die objects a given number of times and compile results.

        Parameters
        ----------
        rolls : int
            Number of times the dice should be rolled.

        Returns
        -------
        None.
        
        Raises
        ------
        ValueError
            If number of rolls is less than 1.

        '''
        
        if not self._results.empty:
            self._results = pd.DataFrame()
            
        result_cols = [i for i in range(1,len(self.dice)+1)]
        idx = [i for i in range(1,rolls+1)]
        self._results = pd.DataFrame(columns=result_cols, index=idx)
        self._results.index.name = 'roll'
        
        for i in range(1, rolls+1):
            
            round_result = {}
            
            for j,d in enumerate(self.dice):
                result = d.roll_die(1)
                round_result[j+1] = result[0]
                
            # add roll num to dataframe
            # self._results = pd.concat([self._results,
            #                           pd.DataFrame([round_result])],
            #                           ignore_index=True)
            
            self._results.loc[i] = round_result
    
    def show_results(self, form='wide'):
        '''
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

        '''
        
        results = self._results.copy(deep=True)
        
        if form == 'wide':
            
            return results
        
        if form == 'narrow':
            
            results = pd.DataFrame(results.stack())
            results.index.set_names(names='roll', level=0, inplace=True)
            results.index.set_names(names='die', level=1, inplace=True)
            results.rename(columns={0:'value'}, inplace=True)
                
            return results
        
        else:
            # TODO
            # return ValueError of option is not wide or narrow
            pass


# ANALYZER CLASS
class Analyzer:
    
    def __init__(self, game):
        '''
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

        '''
        
        # Check that game is of game object data type
        self.game = game
    
    
    def jackpot_counts(self):
        '''
        Compute how many times in a game a roll resulted in which all faces
        were the same (e.g. all die rolled a one).
        
        Returns
        -------
        counts : int
            The number of times a roll resulted in all the same faces (jackpot).

        '''
        
        results = self.game.show_results()
        jackpots = results[results.nunique(axis=1) == 1]
        counts = jackpots.shape[0]
        
        return counts


    def face_counts(self):
        '''
        Compute the number of times each face was rolled in each round.

        Returns
        -------
        face_counts : dataframe
            Dataframe consists of the roll number (rows), face values(columns)
            and the number of times each face value occurred in each roll.

        '''
        
        # Get faces from dice
        faces = self.game.dice[0].faces
        
        # Get row value counts from results
        results = self.game.show_results()
        counts = results.apply(lambda row: row.value_counts(), axis=1).fillna(0).astype('int')
        
        # Create new dataframe with faces as columns and face_counts as values
        face_counts = pd.DataFrame(np.zeros((results.shape[0], len(faces)), dtype='int'),
                                   index = results.index,
                                   columns = faces)
        
        # Create new dataframe with counts of each face for each roll
        face_counts.update(counts)
        
        return face_counts

    def combo_counts(self):
        '''
        Computes the unique combinations of faces rolled along with the
        number of times that unique combination occurred.

        Returns
        -------
        combos : dataframe
            A dataframe consists of a MultiIndex of distinct combinations
            with a column associated with the number of counts.

        '''

        # Get results from game
        results = self.game.show_results()

        # Get all combinations of results and convert to sorted list
        data = results.to_dict(orient='tight')['data']
        combo_data = []
        for d in data:
            combo_data.append(sorted(d))

        # Get value counts of all distinct combinations and output results to dataframe
        combo_counts = pd.DataFrame(sorted(combo_data)).value_counts()
        combos = pd.DataFrame(combo_counts)

        return combos

    
    def permutations(self):
        '''
        Computes unique permutations of faces rolled along with the number
        of times that unique permutation occurred.

        Returns
        -------
        perms : dataframe
            A dataframe consisting of a MultiIndex of distinct permutations
            with a column associated with the number of counts.

        '''

        '''
        • Computes the distinct permutations of faces rolled, along with their counts.
        • Permutations are order-dependent and may contain repetitions.
        • Returns a data frame of results.
        • The data frame should have a MultiIndex of distinct permutations and a column for the associated counts.
        '''
        
        pass























