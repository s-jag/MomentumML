import pandas as pd

def calculate_bollinger_bands(data, window=20, num_std=2):
    # Calculate the rolling mean and standard deviation
    data['rolling_mean'] = data['Close'].rolling(window=window).mean()
    data['rolling_std'] = data['Close'].rolling(window=window).std()
    
    # Calculate the upper and lower Bollinger Bands
    data['upper_band'] = data['rolling_mean'] + num_std * data['rolling_std']
    data['lower_band'] = data['rolling_mean'] - num_std * data['rolling_std']
    
    return data


#The generate_signals() function 
# generates buy/sell/hold signals based on whether the closing price is above the upper band 
# (sell signal) or below the lower band (buy signal).
def generate_signals(data):
    signals = []
    for i in range(len(data)):
        if data['Close'][i] > data['upper_band'][i]:
            signals.append("SELL")
        elif data['Close'][i] < data['lower_band'][i]:
            signals.append("BUY")
        else:
            signals.append("HOLD")
    data['signal'] = signals
    return data

if __name__ == "__main__":
    # Load your data from data_acquisition.py or replace this with your data loading method
    data = pd.read_csv("your_data.csv")

    # Calculate Bollinger Bands
    data_with_bands = calculate_bollinger_bands(data)
    
    # Generate buy/sell signals
    data_with_signals = generate_signals(data_with_bands)
    
    print(data_with_signals)
