# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 19:02:22 2017

@author: lin
"""

import tushare as ts
import numpy as np
import time
import datetime
import pandas as pd
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

#data = ts.get_hist_data('601618',start='2012-10-01',end='2017-10-26', ktype='30')

stock_industry_type = pd.read_csv(r'/home/lin/Py_QuantTrading/Data/CSV_data/stock_industry_type.csv')
index = stock_industry_type['c_name']=='金融行业'
stock_industry_type = stock_industry_type[index]
stock_industry_type = stock_industry_type.loc[:,['code','name']] 