from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def prepare_data(data):
    # Prepare features and labels
    features = data[['rolling_mean', 'rolling_std', 'other_features']]
    labels = data['signal']
    
    return features, labels

def train_model(features, labels):
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
    
    # Initialize and train a RandomForestClassifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate the model on the testing data
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model Accuracy: {accuracy:.2f}")
    
    return model

if __name__ == "__main__":
    # Load your data from data_acquisition.py or replace this with your data loading method
    data = pd.read_csv("your_data.csv")
    
    # Prepare features and labels
    features, labels = prepare_data(data)
    
    # Train the machine learning model
    trained_model = train_model(features, labels)
    
    # You can now use 'trained_model' to make predictions for generating trading signals
