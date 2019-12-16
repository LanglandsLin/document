#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 21:06:34 2019

@author: langlands
"""

import csv
#data = []
#with open("./城市_20150101-20151231/china_cities_20150102.csv") as f:
#    Data = csv.reader(f)
#    for row in Data:  # 将csv 文件中的数据保存到birth_data中
#        data.append(row)

import pandas as pd
import os
import numpy as np
full_data = {"bj":np.zeros([1488, 3]), "tj":np.zeros([1488, 3]), "sjz":np.zeros([1488, 3]), "ts":np.zeros([1488, 3])}
for path,dir_list,file_list in os.walk("./data"):
        for file_name in file_list:
            file = os.path.join(path, file_name)
            data = pd.read_csv(file)
            if "date" in data:
                time = data.loc[0, "date"]
                y = time // 10000
                m = (time % 10000) // 100
                d = time % 100
                x = (y - 2015) * 12 + m - 1
                y = d - 1
                data = data[data.type == "AQI"]
                data = data.iloc[:,3:7].mean()
                full_data["bj"][x*31+y][0] = int(x)
                full_data["bj"][x*31+y][1] = int(y)
                full_data["bj"][x*31+y][2] = data[0]
                full_data["tj"][x*31+y][0] = int(x)
                full_data["tj"][x*31+y][1] = int(y)
                full_data["tj"][x*31+y][2] = data[1]
                full_data["sjz"][x*31+y][0] = int(x)
                full_data["sjz"][x*31+y][1] = int(y)
                full_data["sjz"][x*31+y][2] = data[2]
                full_data["ts"][x*31+y][0] = int(x)
                full_data["ts"][x*31+y][1] = int(y)
                full_data["ts"][x*31+y][2] = data[3]
pd.DataFrame(full_data["bj"], columns=['ym','d','v']).to_csv('bj.tsv',sep='\t', index=False, quoting=csv.QUOTE_NONE)
pd.DataFrame(full_data["tj"], columns=['ym','d','v']).to_csv('tj.tsv',sep='\t', index=False, quoting=csv.QUOTE_NONE)
pd.DataFrame(full_data["sjz"], columns=['ym','d','v']).to_csv('sjz.tsv',sep='\t', index=False, quoting=csv.QUOTE_NONE)
pd.DataFrame(full_data["ts"], columns=['ym','d','v']).to_csv('ts.tsv',sep='\t', index=False, quoting=csv.QUOTE_NONE)
#np.savetxt("bj.tsv", full_data["bj"], delimiter='\t')
#np.savetxt("tj.tsv", full_data["tj"], delimiter='\t')
#np.savetxt("sjz.tsv", full_data["sjz"], delimiter='\t')
#np.savetxt("ts.tsv", full_data["ts"], delimiter='\t')
            
        
#data = pd.read_csv('./城市_20150101-20151231/china_cities_20150102.csv')
#data = data[data.type == "AQI"]
#data = data.iloc[:,3:7].mean()