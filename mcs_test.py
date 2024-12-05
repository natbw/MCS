from src.mcs import Die, Game, Analyzer
import pandas as pd
import numpy as np
import unittest


##################
# DIE CLASS TEST #
##################


class DieTestSuite(unittest.TestCase):
    
    def test_1_die_init(self):
        """
        Test Die object is created with user faces and default weights.
        """
        
        # create test objects
        d1 = Die(np.array([1,2,3,4,5,6]))
        d1_faces = d1.faces.tolist()
        d1_weights = d1.weights.tolist()
        
        # create test variables
        test_faces = [1,2,3,4,5,6]
        test_weights = [1.,1.,1.,1.,1.,1.]
        
        # create assert method
        self.assertEqual(d1_faces, test_faces)
        self.assertEqual(d1_weights, test_weights)

    
    def test_2_die_change_weights(self):
        """
        Test change_weights() changes weights to self.settings and self.weights
        """
        
        # create test objects
        d1 = Die(np.array([1,2,3,4,5,6]))
        d1.change_weights(1, 10)
        
        # create test variables
        changed_weight = 10.0
        
        # create assert method
        self.assertEqual(d1.weights[0], changed_weight)
        self.assertEqual(d1.show_state()['weights'][1], changed_weight)
        
    
    def test_3_die_roll_die(self):
        """
        Test roll die outputs an integer value.
        """
        # create test objects
        d1 = Die(np.array([1,2,3,4,5,6]))
        
        # create test variables
        roll_results = d1.roll_die(10)
        
        # create assert method
        self.assertIsInstance(roll_results, list)
    
    
    def test_4_die_show_state(self):
        """
        Test show state outputs a dataframe type.
        """
        # create test objects
        d1 = Die(np.array([1,2,3,4,5,6]))
        
        # create test variables
        state = d1.show_state()
        
        # create assert method
        self.assertIsInstance(state, pd.DataFrame)
    
    
    def test_5_die_str(self):
        """
        Test string representation of Die object is correct.
        """
        # create test objects
        d1 = Die(np.array([1,2,3,4,5,6]))
        obj_str = str(d1)
        
        # create test variables
        test_str = 'Die'
        
        # create assert method
        self.assertEqual(obj_str, test_str)


###################
# GAME CLASS TEST #
###################


class GameTestSuite(unittest.TestCase):
    
    def test_6_game_init(self):
        """
        Test game object is correctly initialized with dice objects.
        """
        # create test objects
        d1 = Die(np.array([1,2,3,4,5,6]))
        d2 = Die(np.array([1,2,3,4,5,6]))
        
        g1 = Game([d1,d2])
        
        # create test variables
        # none
        
        # create assert method
        self.assertIn(d1, g1.dice)
        self.assertIn(d2, g1.dice)


    def test_7_game_play_game(self):
        """
        Test play_game stores results as dataframe.
        """
        # create test objects
        d1 = Die(np.array([1,2,3,4,5,6]))
        d2 = Die(np.array([1,2,3,4,5,6]))
        
        g1 = Game([d1,d2])
        
        # create test variables
        rolls = 5
        g1.play_game(rolls)
        results_len = g1.show_results().shape[0]
        
        # create assert method
        self.assertEqual(rolls, results_len)
    
    
    def test_8_game_show_results(self):
        """
        Test show_results is dataframe type with wide and narrow.
        """
        # create test objects
        d1 = Die(np.array([1,2,3,4,5,6]))
        d2 = Die(np.array([1,2,3,4,5,6]))
        
        g1 = Game([d1,d2])
        
        # create test variables
        rolls = 3
        g1.play_game(rolls)
        results_wide = g1.show_results('wide')
        results_narrow = g1.show_results('narrow')
        
        # create assert method
        self.assertIsInstance(results_wide, pd.DataFrame)
        self.assertIsInstance(results_narrow, pd.DataFrame)
    
    
    def test_9_game_str(self):
        """
        Test string representation of Game object is correct.
        """
        # create test objects
        d1 = Die(np.array([1,2,3,4,5,6]))
        d2 = Die(np.array([1,2,3,4,5,6]))
        
        g1 = Game([d1,d2])
        obj_str = str(g1)
        
        # create test variables
        test_str = 'Game'
        
        # create assert method
        self.assertEqual(obj_str, test_str)


#######################
# ANALYZER CLASS TEST #
#######################


class AnalyzerTestSuite(unittest.TestCase):
    
    def test_10_analyzer_init(self):
        """
        Test initializer works with game object and stores game correctly.
        """
        # create test objects
        d1 = Die(np.array([1,2,3,4,5,6]))
        d2 = Die(np.array([1,2,3,4,5,6]))
        g1 = Game([d1,d2])
        g1.play_game(5)
        
        # create test variables
        a1 = Analyzer(g1)
        
        # create assert method
        self.assertEqual(g1, a1.game)
    
    
    def test_11_analyzer_jackpot_counts(self):
        """
        Test jackpot_counts() outputs an integer.
        """
        # create test objects
        d1 = Die(np.array([1,2,3,4,5,6]))
        d2 = Die(np.array([1,2,3,4,5,6]))
        g1 = Game([d1,d2])
        g1.play_game(5)
        
        # create test variables
        a1 = Analyzer(g1)
        counts = a1.jackpot_counts()
        
        # create assert method
        self.assertIsInstance(counts, int)
    
    
    def test_12_analyzer_face_counts(self):
        """
        Test face_counts() method outputs dataframe type.
        """
        # create test objects
        d1 = Die(np.array([1,2,3,4,5,6]))
        d2 = Die(np.array([1,2,3,4,5,6]))
        g1 = Game([d1,d2])
        g1.play_game(5)
        
        # create test variables
        a1 = Analyzer(g1)
        face_counts = a1.face_counts()
        rolls = 5
        faces = 6
        
        # create assert method
        self.assertIsInstance(face_counts, pd.DataFrame)
        self.assertEqual(face_counts.shape[0], rolls)
        self.assertEqual(face_counts.shape[1], faces)
    
    
    def test_13_analyzer_combo_counts(self):
        """
        Test combo_counts() method outputs dataframe type with multi index.
        """
        # create test objects
        d1 = Die(np.array([1,2,3,4,5,6]))
        d2 = Die(np.array([1,2,3,4,5,6]))
        g1 = Game([d1,d2])
        g1.play_game(5)
        
        # create test variables
        a1 = Analyzer(g1)
        combo_counts = a1.combo_counts()
        
        # create assert method
        self.assertIsInstance(combo_counts, pd.DataFrame)
        self.assertIsInstance(combo_counts.index, pd.MultiIndex)
    
    
    def test_14_analyzer_permutations(self):
        """
        Test permutations() method outputs dataframe type with multi index.
        """
        # create test objects
        d1 = Die(np.array([1,2,3,4,5,6]))
        d2 = Die(np.array([1,2,3,4,5,6]))
        g1 = Game([d1,d2])
        g1.play_game(5)
        
        # create test variables
        a1 = Analyzer(g1)
        perm_counts = a1.permutations()
        
        # create assert method
        self.assertIsInstance(perm_counts, pd.DataFrame)
        self.assertIsInstance(perm_counts.index, pd.MultiIndex)
    
    
    def test_15_analyzer_str(self):
        """
        Test string representation of Analyzer object is correct.
        """
        # create test objects
        d1 = Die(np.array([1,2,3,4,5,6]))
        d2 = Die(np.array([1,2,3,4,5,6]))
        g1 = Game([d1,d2])
        g1.play_game(5)
        a1 = Analyzer(g1)
        
        obj_str = str(a1)
        
        # create test variables
        test_str = 'Analyzer'
        
        # create assert method
        self.assertEqual(obj_str, test_str)


if __name__ == "__main__":
    unittest.main(verbosity=2)
    