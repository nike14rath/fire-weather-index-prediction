🔥 Fire Weather Index Prediction – Flask ML App

This project is a Machine Learning model deployment using Flask, where a trained Ridge Regression model predicts the Fire Weather Index (FWI) based on meteorological inputs.

The application provides a web-based interface for users to input weather parameters and get real-time predictions.

🚀 Features

Flask-based web application

Ridge Regression model for prediction

StandardScaler for feature scaling

User-friendly HTML form

Real-time prediction results

Clean and modular project structure

🧠 Machine Learning Model

Algorithm: Ridge Regression

Preprocessing: StandardScaler

Target Variable: Fire Weather Index (FWI)

Feature Engineering:

Sine and cosine transformation of month for seasonality handling

📂 Project Structure
Model_deployment/
│
├── application.py
├── Models/
│   ├── ridge.pkl
│   └── scaler.pkl
│
├── templates/
│   ├── index.html
│   └── home.html
│
├── project_env/
│
└── README.md

🛠️ Tech Stack

Programming Language: Python

Framework: Flask

ML Libraries: Scikit-learn, NumPy, Pandas

Frontend: HTML, CSS

Model Serialization: Pickle

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/nike14rath/fire-weather-index-prediction.git
cd fire-weather-index-prediction

2️⃣ Create and activate virtual environment
python -m venv project_env


Windows

project_env\Scripts\activate

3️⃣ Install dependencies
pip install flask scikit-learn numpy pandas

4️⃣ Run the application
python application.py


Open browser and visit:

http://127.0.0.1:5000/

📊 Input Parameters

Month (1–12)

Temperature

Relative Humidity (RH)

Wind Speed (Ws)

Rain

FFMC

DMC

ISI

Classes

Region

📈 Output

Predicted Fire Weather Index (FWI) value

🧪 Example Use Case

This project can be used to:

Demonstrate ML model deployment

Practice Flask web development

Showcase end-to-end ML pipeline

Serve as a mini-project for interviews or portfolios

📌 Future Improvements

Input validation and error handling

Model comparison (Lasso, ElasticNet)

UI improvement using Bootstrap

Deployment on Render / Railway / AWS

REST API support

👤 Author

Nikhil Rathawar
B.Tech – Electronics & Communication Engineering
Interests: Machine Learning, Data Analysis, VLSI Design

📄 License

This project is for educational purposes.