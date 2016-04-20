# tests

import os
os.chdir('\\Users\\Noe\\workspace\\stakenanny\\candiapps')
#import utils.py

import imp 
imp.load_source('utils','utils.py')
import utils
import unittest

class NewUserTest(unittest.TestCase):


    def test_can_grab_conf_and_check_it_later(self):
        # Jody uses this library to parse test.conf to get needed env
        self.assertIn('coinlist',stakenanny.envars['turbo,bottlecaps'])
        self.fail('Finish the test!')
        pass
