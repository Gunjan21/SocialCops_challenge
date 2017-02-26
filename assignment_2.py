# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 23:00:20 2017

@author: gunjan
"""

import pandas as pd
from sklearn.decomposition import PCA

distr_wise = pd.read_csv("district_wise_final.csv")

##finding correlation between different features
corr = distr_wise.corr()
###normalizing each value
distr_wise_norm = (distr_wise - distr_wise.mean()) / distr_wise.std() 

## The 'District' column became NaN after the above computation.
##Copying 'District' names from the original dataframe
distr_wise_norm['District'] = distr_wise['District']

## Making the 'districts' column as the index
distr_wise_norm = distr_wise_norm.set_index(keys="District")

pca = PCA(n_components=15)
pca.fit(distr_wise_norm)

##findind the factor score
loading = pca.components_ 

##factorscore associated with the first principle component
score = loading[0]

##Summing all the normalized values of the dataframe after multiplying with
##the corresponding score
distr_wise_norm['Score'] = (distr_wise_norm.multiply(score)).sum(axis=1)

##This gives the order of districts
distr_wise_norm = distr_wise_norm.sort(columns='Score', ascending = False)

##Writing the final order and Score in a file
distr_wise_norm.to_csv('index_final.csv', header= True, columns = {'Score'})