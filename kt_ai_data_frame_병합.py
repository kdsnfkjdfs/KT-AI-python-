# -*- coding: utf-8 -*-
"""KT-AI:DATA FRAME 병합.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VkEF50g8K-BilPZN2dCX4jY2IGX9D-wA
"""

import pandas as pd
import numpy as np

df1 = pd.DataFrame({"key1":[0,1,2,3,4],"values":['a','b','c''d','e']},index = [0,1,2,3,4])
df2 = pd.DataFrame({"key1":[3,4,5,6,7],"values":['c','d','e','f','g']},index = [3,4,5,6,7])



df1

df2

pd.concat([df1,df2],ignore_index = True)

pd.concat([df1,df2],axis = 1)