# -*- coding: utf-8 -*-
"""
Created on Sun May 16 22:41:44 2021

@author: User
"""
import os
import datetime
import namegenerator
import numpy as np
import pandas as pd
import openpyxl

def random_dates(start=None, end=None, n=1, unit='D', seed=None):
    """A function which produces random dates"""
    if not seed:  # from piR's answer
        np.random.seed(0)
    if not start:
        start = datetime.datetime(2020,6,1)
    if not end:
        end = datetime.datetime.now()
    ndays = (end - start).days + 1
    return pd.to_timedelta(np.random.rand(n) * ndays, unit=unit) + start

# --------------------------------------------------------

# Choose the size of your data
n_rows = int(1.50 * 10**6)
n_cols = 7

# Create your dataframe – Mix up the data bit
df = pd.DataFrame(np.random.rand(n_rows,n_cols), columns=[f"Col_{i}" for i in range(1,n_cols+1)])
df["name"] = df.apply(lambda x: namegenerator.gen(), axis=1)
df["timestamp_1"] = random_dates(n=n_rows, seed=1)
df["timestamp_2"] = random_dates(n=n_rows, seed=2)

# How big we talking about?
print(f"{len(df):,} rows\n{len(df.columns):,} cols")