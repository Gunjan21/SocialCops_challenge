# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 19:02:39 2017

@author: gunjan
"""

import pandas as pd

#read both the sheets from data file
sh1 = pd.read_excel("Tab_Villages_Mapping, Krishna District, 25 July 2015.xlsx")
sh2 = pd.read_excel("Tab_Villages_Mapping, Krishna District, 25 July 2015.xlsx", sheetname = 1)


## making sure the Dates are in datetime format
sh2.dtypes
'''
AC Name                      object
Mandal Name                  object
Village Name                 object
Tab No                        int64
Survey Start Date    datetime64[ns]
Survey End Date      datetime64[ns]
dtype: object
'''

sh1.dtypes
'''
Response No              int64
Tab No                   int64
Survey Date     datetime64[ns]
AC Name                float64
Mandal Name            float64
Village Name           float64
dtype: object
'''

#checking for equal tab numbers in both dataframes
#copying the village names if the Survey Dates also match.
#There are some survey dates overlapping for the same Tab No.
#In such cases, all the village names are being predicted.
#Either one of them is true.
for i in range(len(sh1["Tab No"])):
    village_list = []
    for j in range(len(sh2["Tab No"])):
        if sh1["Tab No"][i] == sh2["Tab No"][j]:
            if sh2["Survey Start Date"][j] <= sh1["Survey Date"][i] <= sh2["Survey End Date"][j]:
                if sh2['Village Name'][j] not in village_list:
                    village_list.append(sh2["Village Name"][j])
    sh1['Village Name'][i] = village_list


#writing the predicted village names to a file.
sh1.to_excel("predicted_villages.xlsx")

'''
19655 villages have been predicted out of 21531
i.e. 91.291% of the villages have been predicted
Out of these, 2351 have 2 village predictions 
and 132 have 3 village predictions.
'''
