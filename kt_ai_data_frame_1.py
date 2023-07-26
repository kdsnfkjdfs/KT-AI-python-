# -*- coding: utf-8 -*-
"""KT-AI:DATA FRAME-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18gWPRmR49f2obgZrWS3Z2r8lScQsUKta

# Pandas
"""

import pandas as pd
import numpy as np

a1 = pd.DataFrame({"a":[1,2,3],"b":[2,3,4],"c":[3,4,5]})

print(a1)

a2 = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],["a","b","c"])

print(a2)

ct = pd.read_csv('/content/sample_data/FL_insurance_sample.csv',encoding = "cp949")

print(ct)

ct.head(n=3) #원한는 갯수만큼 상위 데이터를 가지고 온다

ct.tail(n = 10) #원한는 갯수만큼 하위 데이터를 가지고 온다

ct.shape

ct.columns

ct.info()

ct.describe() #데이터 프레임에 기본적인 통계정보를 보여줌



ct.dtypes #데이터 타입

ct.ct_polocyID = ct['policyID']

ct[['policyID']]

ct[7:10]

ct.info()

cp = np.arange(10,20,3)
print(cp)

ct.loc[[289,23,232,323,23]] #원하는 row값을 가지고온다

ct.loc[[1,3,5,234,4,6,],['policyID','county','statecode']] #row. col

ct.iloc[[1,3,5,234,4,6,],[0.1,2,3]] # row,col(원하는 컬럼의 인덱스 번호로 쓴다)

ct['policyID'] = ct['policyID'] * 2
ct.head()

ct.drop('policyID',axis = 1) # axis가 0이면 행, 1이면 열
ct.head()