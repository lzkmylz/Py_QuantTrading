# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 19:06:46 2017

@author: lin
"""

import tushare as ts
import numpy as np
import time
import pandas as pd

"""

Get stock data using tushare lib.

"""

def get_one_stock_data(code, start, end, ktype, retry_count, pause):
    """Get basic data for one stock
    
    Args:
        code: stock id such as "601618", or index code such as "sh"
        start: data start date, format: YYYY-MM-DD
        end: data end date, format: YYYY-MM-DD
        ktype: data type, D = day line
    
    Return:
        data: pandas dataframe including: date,open, high, close, low,
        volume, price_change, p_change, ma5, ma10, ma20, v_ma5, v_ma10,
        v_ma20, turnover
    """
    data = ts.get_hist_data(code, start, end, ktype, retry_count, pause)
    
    return data
    
def get_one_stock_years_data(code, years, ktype, retry_count, pause):
    """Get one stock last several years data
    
    Args:
        code: stock id such as "601618", or index code such as "sh"
        years: years need trace back
        ktype: data type, D = day line
    
    Return:
        data: pandas dataframe including: date,open, high, close, low,
        volume, price_change, p_change, ma5, ma10, ma20, v_ma5, v_ma10,
        v_ma20, turnover
    """
    current_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    current_year = int(current_time.split('-')[0])
    current_month = int(current_time.split('-')[1])
    current_day = int(current_time.split('-')[2])
    trace_year = current_year - years
    trace_back_time = str(trace_year) + str(current_month) + str(current_day)
    data = ts.get_hist_data(code, trace_back_time, current_time, ktype, retry_count, pause)
    
    return data

def get_financial_industry_stocks():
    """Get financial industry stocks.
    
    Return:
        stocks: pandas dataframe, including stocks in financial industry
        shape: [code, name]
    """
    stock_industry_type = pd.read_csv(r'/home/lin/Py_QuantTrading/Data/CSV_data/stock_industry_type.csv')
    index = (stock_industry_type['c_name']=='金融行业')
    stock_industry_type = stock_industry_type[index]
    stock_industry_type = stock_industry_type.loc[:,['code','name']]
    
    return stock_industry_type