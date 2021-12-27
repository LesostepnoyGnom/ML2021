# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 21:49:01 2021

@author: 1618047
"""


import pandas as pd
data = pd.read_csv('math_students.csv', delimiter=',')

# ----------------------------------------------------------------------
# 1
# reason = data.groupby('reason').describe()
# print(reason)
# ----------------------------------------------------------------------
# 2
# a = data['Medu'].value_counts().to_frame()
# b = data['Fedu'].value_counts().to_frame()
# c = data['guardian'].value_counts().to_frame()
# print(a)
# print(b)
# print(c)
# print(data[(data['Medu'] == 0) & ((data['Fedu'] == 0))].shape[0])
# ----------------------------------------------------------------------
# 3
# a=data[(data['school'] == 'MS')].head()
# print(a['age'].min())
# ----------------------------------------------------------------------
# 4
# a = data['absences'] 
# a = list(data['absences'])
# j=0
# for i in range(len(a)):
#     if a[i]%2!=0:
#         j+=1
# print(j)
# ----------------------------------------------------------------------
# 5
# a = list(data['G3'])
# rom = list(data['romantic'])
# print(a)
# print(rom)

# jY = 0
# kY = 0
# jN = 0
# kN = 0

# for i in range(len(a)):
#     if rom[i]=='yes':
#         jY += a[i]
#         kY += 1
#     else:
#         jN += a[i]
#         kN += 1

# Yes = jY/kY
# No = jN/kN

# ans = Yes - No

# print(ans)
# ----------------------------------------------------------------------
#6
# print(data[data['activities'] == 'yes']['absences'].value_counts())