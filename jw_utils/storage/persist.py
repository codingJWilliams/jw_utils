# Jay Williams 2017
# This module is included as part of https://github.com/codingJWilliams/jw_utils
# Liscenced according to ../../LISCENCE
# Contact codingJWilliams on github with any queries

import jw_utils
import os

class PersistantString(str):
  def __init__(self, value):
    self.storeValue(value)
  def __repr__(self):
    return 'PersistantString("' + self.getValue() + '")'
  