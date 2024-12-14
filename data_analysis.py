import pandas as pd

def calculate_moving_average(data, window_size=50):
    return data['Close'].rolling(window=window_size).mean()
