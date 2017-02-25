# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 19:02:39 2017

@author: gunjan
"""

import pandas as pd

sh1 = pd.read_excel("Tab_Villages_Mapping, Krishna District, 25 July 2015.xlsx")
sh2 = pd.read_excel("Tab_Villages_Mapping, Krishna District, 25 July 2015.xlsx", sheetname = 1)


sh2["Survey End Date"] = pd.to_datetime(sh2["Survey End Date"])

sh2["Survey Start Date"] = pd.to_datetime(sh2["Survey Start Date"])

for i in range(len(sh1["Tab No"])):
    for j in range(len(sh2["Tab No"])):
        if sh1["Tab No"][i] == sh2["Tab No"][j]:
            if sh2["Survey Start Date"][j] <= sh1["Survey Date"][i] <= sh2["Survey End Date"][j]:
                    sh1["Village Name"][i] = sh2["Village Name"][j]
 
sh1.to_excel("predicted_villages.xls")

'''                    
18218 villages have been predicted out of 21531
i.e, 84.613% of the villages have been predicted
'''
