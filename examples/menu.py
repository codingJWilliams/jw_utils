# Jay Williams 2017
# This module is included as part of https://github.com/codingJWilliams/jw_utils
# Liscenced according to ../../LISCENCE
# Contact codingJWilliams on github with any queries

# ----------- Code so I can import jw_utils from the examples folder - you don't need this ---------------------
import sys
sys.path.append("..") # Adds higher directory to python modules path.
# ----------- End hacky code -------------


import jw_utils

def callback1():
  print("This is callback one")

def callback2():
  print("This is callback two")

menu = jw_utils.helpers.menu.Menu("Test Menu!")

menu.addOption("Test Callback 1", callback1)
menu.addOption("Test Callback 2", callback2)

menu.doMenu()