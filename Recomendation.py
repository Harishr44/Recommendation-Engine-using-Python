# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 21:46:55 2020

@author: Harish
"""

import pandas as pd
import numpy as np

book=pd.read_csv("book.csv",encoding='latin 1')
len(book.BookTitle.unique())
len(book.UserID.unique())

user_book = book.pivot_table(index='UserID',
                       columns='BookTitle',
                       values='BookRating').reset_index(drop=True)

user_book.index = book.UserID.unique()
user_book

user_book.fillna(0, inplace=True)
 user_book


from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import cosine, correlation

user_sim = 1 - pairwise_distances( user_book.values,metric='cosine')
user_sim

user_sim_df = pd.DataFrame(user_sim)

user_sim_df.index = book.UserID.unique()
user_sim_df.columns = book.UserID.unique()
user_sim_df

user_sim_df.iloc[0:5, 0:5]

np.fill_diagonal(user_sim, 0)
user_sim_df.iloc[0:5, 0:5]

user_sim_df.idxmax(axis=1)[0:5]


book[(book['UserID']==8) | (book['UserID']==276744)]

user_1=book[book['UserID']==8]
user2=book[book['UserID']==99]
