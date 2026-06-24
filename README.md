# 🚘 Car Price Prediction Using Machine Learning

## 📌 Project Overview

The Car Price Prediction project uses Machine Learning to estimate the resale value of a used car based on various features such as manufacturing year, showroom price, kilometers driven, fuel type, seller type, transmission, and number of previous owners.

The application is built using **Python**, **Scikit-Learn**, and **Streamlit**, providing an interactive web interface for real-time price prediction.

---

## ✨ Features

* Predict used car selling prices instantly
* Interactive Streamlit web application
* User-friendly and modern UI
* Machine Learning powered predictions
* Real-time valuation system
* Responsive design

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Pickle

---

## 📊 Input Features

| Feature       | Description                       |
| ------------- | --------------------------------- |
| Present Price | Current showroom price of the car |
| Driven KMS    | Total kilometers driven           |
| Owner         | Number of previous owners         |
| Car Age       | Age of the car                    |
| Fuel Type     | Petrol / Diesel                   |
| Seller Type   | Dealer / Individual               |
| Transmission  | Manual / Automatic                |

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/car-price-prediction.git
cd car-price-prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```text
Car-Price-Prediction/
│
├── app.py
├── car_price_model.pkl
├── requirements.txt
├── README.md
└── dataset.csv
```

---

## 🎯 Machine Learning Model

The project uses a trained Machine Learning Regression model to predict car prices based on historical vehicle data.

Model Inputs:

* Present Price
* Driven KMS
* Owner
* Car Age
* Fuel Type
* Seller Type
* Transmission Type

---

## 📷 Application Preview

The application provides:

* Luxury automotive-themed UI
* Interactive form inputs
* Instant price prediction
* Clean and professional dashboard

---

## 🌐Live Project

https://carpricepredictionwithml.streamlit.app/

---

## ⭐ Future Enhancements

* Upload car images for valuation
* Advanced analytics dashboard
* Model performance visualization
* Cloud deployment
* Multiple ML model comparison
