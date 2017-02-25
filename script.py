# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 23:00:20 2017

@author: gunjan
"""

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
%matplotlib inline

distr_wise = pd.read_csv("district_wise_final3.csv")

#finding correlation between different features
corr = distr_wise.corr()
###normalizing each value
distr_wise_norm = (distr_wise - distr_wise.mean()) / distr_wise.std() 

distr_wise_norm['District'] = distr_wise['District']
distr_wise_norm = distr_wise_norm.set_index(keys="District")

pca = PCA(n_components=15)
###tried with 20 components first, but 15 were explaining all the variance
### so used 15
pca.fit(distr_wise_norm)

#The amount of variance that each PC explains
var= pca.explained_variance_ratio_

#Cumulative Variance explained
var1=np.cumsum(np.round(pca.explained_variance_ratio_, decimals=4)*100)

plt.plot(var1)

#findind the factor score
loading = pca.components_ 
##factorscore associated with the first principle component
score = loading[0]

distr_wise_norm['Score'] = (distr_wise_norm.multiply(score)).sum(axis=1)
#### This gives the order of districts
distr_wise_norm = distr_wise_norm.sort(columns='Score', ascending = False)


