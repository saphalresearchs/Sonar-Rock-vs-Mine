# import streamlit as st
# import pickle
# import numpy as np

# # Open the file in read-binary mode
# with open("model.pkl", "rb") as file:
#     model = pickle.load(file)

# # Title
# st.title("Sonar Rock vs Mine")

# # Input fields
# st.write("Enter the feature values:")

# input_data = []
# # Assuming your model takes 3 numerical inputs
# for i in range(0, 61):
#     feature_value = st.number_input(f"Feature {i}", value=0.0)
#     input_data.append(feature_value)

# # Prediction
# if st.button("Predict"):
#     prediction = model.predict(input_data)
#     st.write(f"Prediction: {prediction[0]}")

import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Title
st.title("Sonar Rock vs Mine")

# Input field for all 60 values
st.write("Enter 60 feature values, separated by commas:")

user_input = st.text_area("Paste your 60 values here", placeholder="Example: 0.1,0.2,0.3, ... ,1.0")


# Prediction
if st.button("Predict"):
    try:
        # Convert input string to a NumPy array
        input_data = np.array([list(map(float, user_input.split(",")))])  # Convert to 2D array
        
        # Ensure exactly 60 values are entered
        if input_data.shape[1] != 60:
            st.error(f"Please enter exactly 60 values. You entered {input_data.shape[1]}.")
        else:
            prediction = model.predict(input_data)
            if prediction[0]=="R":
                st.write(f"Prediction is Rock. Safe to go")
            else:
                st.write(f"Prediction is Mine. Danger!!!")
    
    except ValueError:
        st.error("Invalid input! Please enter numbers separated by commas.")

