#functional tests
import os
os.chdir('\\Users\\Noe\\workspace\\stakenanny\\candiapps')
#import utils.py

import imp 
imp.load_source('utils','utils.py')
import utils
# Jody uses this library to parse test.conf to get needed env
assert 'turbostake, bottlecaps' in utils.envars['coinlist']