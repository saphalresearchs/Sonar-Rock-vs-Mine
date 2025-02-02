## **Sonar Rock vs. Mine Classifier**
This project is a basic **Machine Learning** model using **Logistic Regression** to classify whether an object detected by SONAR is a **rock or a mine**. It is deployed using **Streamlit**, allowing users to input feature values and get predictions instantly.

## **🔹 Features**
- Uses a **Logistic Regression** model trained on the **SONAR dataset**.
- Accepts **60 feature values** from sonar signals.
- Provides a simple **Streamlit UI** for easy interaction.
- Allows users to **copy-paste** all 60 values at once for convenience.

## **🛠 Installation**
### **1️⃣ Clone the Repository**

### **2️⃣ Install Dependencies**
pip install -r requirements.txt

## **🚀 Usage**
### **1️⃣ Run the Streamlit App**
streamlit run app.py

This will open the app in your **browser at** `http://localhost:8501/`.

### **2️⃣ Enter Input Data**
- **Copy-paste** all **60 feature values** as a comma-separated list or enter all the values manually.
- Click **"Predict"** to see whether the object is a **rock or a mine**.

---

## **📜 Project Files**
- **`app.py`** → Streamlit web app for user interaction.
- **`model.pkl`** → Trained Logistic Regression model.
- **`requirements.txt`** → List of required Python libraries.
- **`README.md`** → This documentation. 
- **`Sonar_data.csv`** → This is the dataset. 
- **`Rock vs Mine_prediction.ipynb`** → Jupyter Notebook involving importing libraries, data preprocessing, model training and dumping the model. 

---

## **📊 Model Training**
The model is trained on the **SONAR dataset** from UCI Machine Learning Repository.
- **Algorithm:** Logistic Regression  
- **Dataset:** SONAR signal data  
- **Target Classes:**  
  - **Rock (`R`)**  
  - **Mine (`M`)**  

---

## **📌 Example Input**
```
0.02,0.0371,0.0428,0.0207,0.0954,0.0986,0.1539,0.1601,0.3109,0.2111,
0.1609,0.1582,0.2238,0.0645,0.0660,0.2273,0.3100,0.2999,0.5078,0.4797,
0.5783,0.5071,0.4328,0.5550,0.6711,0.6415,0.7104,0.8080,0.6791,0.3857,
0.1307,0.2604,0.5121,0.7547,0.8537,0.8507,0.6692,0.6097,0.4943,0.2744,
0.0510,0.2834,0.2825,0.4256,0.2641,0.1386,0.1051,0.1343,0.0383,0.0324,
0.0232,0.0027,0.0065,0.0159,0.0072,0.0167,0.0180,0.0084,0.0089,0.0032,
0.0132,0.0127,0.0055,0.0169,0.0073,0.0168,0.0080,0.0184,0.0079,0.0042
