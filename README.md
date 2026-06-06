# Name Gender Detection Using Machine Learning

## 📌 Project Overview

This project predicts the gender (Male or Female) based on a person's first name using Machine Learning techniques. The model is trained on a dataset containing names and their corresponding genders and can classify new names with high accuracy.

The project demonstrates data preprocessing, feature engineering, model training, evaluation, and prediction using Python and Scikit-Learn.

---

## 🚀 Features

- Predict gender from a given name
- Data preprocessing and cleaning
- Feature extraction from names
- Machine Learning model training
- Model evaluation with accuracy metrics
- Easy-to-use prediction interface

---

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Scikit-Learn
- Matplotlib
- Seaborn
- Joblib

---

## 📂 Project Structure

```
NAME_GENDER_DETECTION_PROJECT/
│
├── data/
│   └── names_dataset.csv
│
├── models/
│   └── gender_model.pkl
│
├── notebooks/
│   └── Gender_Detection.ipynb
│
├── src/
│   ├── data_preprocessing.py
│   ├── feature_extraction.py
│   ├── train_model.py
│   └── predict.py
│
├── outputs/
│   ├── confusion_matrix.png
│   └── accuracy_report.txt
│
├── requirements.txt
├── README.md
└── main.py
```

---

## 📊 Dataset

The dataset contains:

| Column | Description |
|----------|-------------|
| Name | Person's First Name |
| Gender | Male / Female |

Example:

| Name | Gender |
|--------|---------|
| Akshay | Male |
| Priya | Female |
| Rahul | Male |
| Sneha | Female |

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Akshaya44372/NAME_GENDER_DETECTION_PROJECT.git
cd NAME_GENDER_DETECTION_PROJECT
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Train the model:

```bash
python main.py
```

Run prediction:

```bash
python predict.py
```

Example:

```text
Enter Name: Akshay
Predicted Gender: Male
```

---

## 📈 Model Workflow

1. Load Dataset
2. Data Cleaning
3. Feature Engineering
4. Convert Names into Numerical Features
5. Train Machine Learning Model
6. Evaluate Performance
7. Save Trained Model
8. Predict Gender for New Names

---

## 📊 Evaluation Metrics

The model is evaluated using:

- Accuracy Score
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## 🎯 Future Improvements

- Deep Learning (CNN/LSTM) Implementation
- Web Application using Flask
- Streamlit Dashboard
- Real-Time API Integration
- Support for Multiple Languages

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to GitHub
5. Create a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---


