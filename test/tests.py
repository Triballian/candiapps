# tests

import os
os.chdir('\\Users\\Noe\\workspace\\stakenanny\\candiapps')
#import utils.py

import imp 
imp.load_source('utils','utils.py')
import utils
import unittest

class NewConfTest(unittest.TestCase):


    def test_can_grab_env_from_conf_n_use_it_later(self):
        
        self.assertIn('turbostake, bottlecaps', utils.envars['coinlist'])
        self.assertIn('coinlist', utils.envars)
        self.assertEqual(utils.envars['coinlist'], 'turbostake, bottlecaps')
        self.assertEqual(utils.envars['gitdir'], '/Program Files/Git/bin')
        self.assertEqual(utils.envars['gitexe'], 'git.exe')
        self.assertEqual(utils.envars['sclone'], '/Users/Noe/workspace/cvim')

        #self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()



