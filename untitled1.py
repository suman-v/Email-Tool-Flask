# -*- coding: utf-8 -*-
"""
Created on Sun May 16 23:57:51 2021

@author: User
"""

import pickle

with open('database.pkl', 'rb') as input:
  with open("database.pkl", "wb") as output:
    pickle.dump(pickle.load(input), output, 2) # embedding_weights


