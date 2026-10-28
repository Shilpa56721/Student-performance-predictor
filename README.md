# 🎓 Student Performance Predictor

An end-to-end machine learning project that predicts a student's **Math score** using demographic and academic inputs such as gender, parental education, lunch type, test preparation, and reading and writing scores. The project uses four regression algorithms and provides an interactive web application deployed on **Streamlit Community Cloud**.

🚀 **Live Demo:** [Student Performance Predictor](https://student-performance--predictor.streamlit.app/)

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Dataset & Input Features](#-dataset--input-features)
- [ML Workflow](#-ml-workflow)
- [Model Evaluation](#-model-evaluation)
- [Installation](#-installation)
- [Running the App](#-running-the-app)
- [Deployment](#-deployment)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

## 📖 Overview

This project predicts a student's Math score based on seven demographic and academic features. It follows a modular machine learning workflow covering data ingestion, preprocessing, model training, evaluation, and prediction.

The trained model and preprocessing pipeline are saved for reuse, and predictions are delivered through an interactive Streamlit application.

---

## ✨ Features

- Predicts Math scores using seven input features.
- Modular machine learning pipeline under `src/`.
- Implements four regression algorithms.
- Handles missing values, categorical encoding, and numerical scaling.
- Saves the trained model and preprocessor for reuse.
- Maintains logs of pipeline execution.
- Interactive web interface built with Streamlit.
- Deployed on Streamlit Community Cloud.

---

## 🛠️ Tech Stack

| Area | Tools |
|---|---|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn, XGBoost |
| Web Framework | Streamlit |
| Model Serialization | Dill |
| Deployment | Streamlit Community Cloud |

---

## 📂 Project Structure

```text
Student-performance-predictor/
├── artifacts/                  # Saved model, preprocessor and datasets
├── logs/                       # Pipeline execution logs
├── notebook/                   # EDA and model training notebooks
├── src/                        # ML components and utilities
│   ├── components/             # Data ingestion, transformation and training
│   ├── pipeline/
│   │   └── predict_pipeline.py # Prediction pipeline
│   └── utils.py                # Helper functions
├── streamapp.py                # Streamlit application
├── requirements.txt            # Python dependencies
└── .gitignore
```

---

## 🗃️ Dataset & Input Features

The project uses a student exam performance dataset with the following input features:

| Feature | Type | Values |
|---|---|---|
| `gender` | Categorical | Male, female |
| `race_ethnicity` | Categorical | Group A – Group E |
| `parental_level_of_education` | Categorical | Some high school, high school, some college, associate's degree, bachelor's degree, master's degree |
| `lunch` | Categorical | Standard, free/reduced |
| `test_preparation_course` | Categorical | None, completed |
| `reading_score` | Numeric | 0–100 |
| `writing_score` | Numeric | 0–100 |

**Target variable:** `math_score`

---

## 🔄 ML Workflow

1. **Data Ingestion:** Load the dataset and split it into training and testing sets.
2. **Data Transformation:** Handle missing values, encode categorical features using one-hot encoding, and scale numerical features through a preprocessing pipeline.
3. **Model Training:** Train and compare the following regression algorithms:
   - Linear Regression
   - Decision Tree Regression
   - Random Forest Regression
   - XGBoost Regression
4. **Model Evaluation:** Evaluate model performance using R², RMSE, and MAE.
5. **Model Persistence:** Save the selected trained model and preprocessor in the `artifacts/` directory.
6. **Prediction:** Process user inputs, load the saved artifacts, and generate the predicted Math score.
7. **Deployment:** Run the application through Streamlit Community Cloud.

---

## 📈 Model Evaluation

The four regression algorithms are evaluated using the following metrics:

- **R² Score:** Measures how much variation in Math scores is explained by the model.
- **RMSE:** Measures prediction error while penalizing larger errors more heavily.
- **MAE:** Measures the average absolute difference between actual and predicted scores.

The best-performing model is selected based on the evaluation results.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Shilpa56721/Student-performance-predictor.git
cd Student-performance-predictor
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App

Run the following command to launch the Streamlit application locally:

```bash
streamlit run streamapp.py
```

Open the local URL provided by Streamlit, usually `http://localhost:8501`.

Enter the student's details and click **Predict your Maths Score** to obtain the prediction.

> **Note:** The application requires the trained model and preprocessor files in the `artifacts/` directory. Train the model first if these files are missing.

---

## ☁️ Deployment

The application is hosted and deployed using **Streamlit Community Cloud**.

1. Push the project code to GitHub.
2. Ensure `streamapp.py`, `requirements.txt`, and the required model artifacts are available.
3. Visit [Streamlit Community Cloud](https://share.streamlit.io/).
4. Connect your GitHub account and select the repository.
5. Set `streamapp.py` as the main application file.
6. Deploy the application and obtain the public URL.

---

## 🔮 Future Improvements

- Add model performance comparison charts.
- Display actual versus predicted scores.
- Improve input validation and error handling.
- Add unit tests for preprocessing and prediction.
- Containerize the application with Docker.
- Implement automated testing and deployment workflows.
- Extend the application to predict reading and writing scores.

---

## 👩‍💻 Author

**Shilpa**

GitHub: [@Shilpa56721](https://github.com/Shilpa56721)

---

⭐ If you found this project useful, consider giving it a star!
