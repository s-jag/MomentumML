import pandas as pd

def detect_changepoints(data, threshold=0.5):
    changepoints = []

    # Calculate daily returns
    data['returns'] = data['Close'].pct_change()

    # Initialize cumulative sums
    cum_sum = 0
    for i in range(1, len(data)):
        cum_sum = max(0, cum_sum + data['returns'][i])
        
        # If cumulative sum exceeds threshold, consider a potential changepoint
        if cum_sum > threshold:
            changepoints.append(data.index[i])
            cum_sum = 0  # Reset cumulative sum

    return changepoints

if __name__ == "__main__":
    # Load your data from data_acquisition.py or replace this with your data loading method
    data = pd.read_csv("your_data.csv")

    # Detect changepoints
    detected_changepoints = detect_changepoints(data)
    
    print("Detected Changepoints:")
    for cp in detected_changepoints:
        print(cp)
