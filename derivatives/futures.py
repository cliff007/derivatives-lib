import math
from decimal import Decimal

import requests
import numpy as np
import pandas as pd

from lib import formulas

def get_fixed_storage_cost(storage_cost, risk_free_rate, term):
    return storage_cost * math.exp(-risk_free_rate * term)

def get_price(spot_price, risk_free_rate, term, known_income=0, known_yield=0):
    return (spot_price - known_income) * math.exp(
        (risk_free_rate - known_yield) * term
    )

def get_value(spot_price, delivery_price, risk_free_rate, term,
              known_income=0, known_yield=0):
    return (spot_price * math.exp(-known_yield * term)) - known_income - \
        (delivery_price * math.exp(-risk_free_rate * term))

def get_historical_data():
    r = requests.get(
        "https://www.quandl.com/api/v1/datasets/ICE/BF1998.json?trim_start=1996-12-17&trim_end=1997-12-16"
    )
    req_data = r.json()
    data = req_data.get('data')
    prices = [ price[4] for price in data ]
    return prices

def compute_fun_stuff():
    data = pd.DataFrame(data=get_historical_data())
    return data    
