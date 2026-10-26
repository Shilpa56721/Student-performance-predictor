# 🎓 Student Performance Predictor

An end-to-end machine learning project that predicts a student's **Math score** from demographic and academic inputs such as gender, parental education, lunch type, test preparation and reading/writing scores. The trained model is served through both a **Flask** web app and a **Streamlit** app, and the repo includes configuration for deployment on **AWS Elastic Beanstalk**.

🚀 **Live Demo:** [https://student-performance--predictor.streamlit.app/](https://student-performance--predictor.streamlit.app/)

---

## 📌 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Dataset & Input Features](#-dataset--input-features)
- [ML Workflow](#-ml-workflow)
- [Live Demo](#-live-demo)
- [Installation](#-installation)
- [Running the Apps](#-running-the-apps)
- [Deployment](#-deployment)
- [Screenshots](#-screenshots)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

## 📖 Overview

Understanding which factors influence exam performance can help educators spot students who may need extra support. This project builds a regression model that takes seven student attributes and returns a predicted **Math score**. It follows a modular ML pipeline structure (data ingestion → transformation → model training → prediction) with custom logging, so it is easy to extend and maintain.

---

## ✨ Features

- 🔮 Predicts Math score from 7 input features
- 🧱 Modular, production-style pipeline under `src/`
- 🌐 **Flask** web interface (`app.py`)
- 📊 **Streamlit** interface (`streamapp.py`) with input validation
- 🤖 Multiple regression models compared (scikit-learn, CatBoost, XGBoost)
- 📝 Logging of pipeline runs in `logs/`
- ☁️ AWS Elastic Beanstalk deployment config included
- 🌍 Streamlit app deployed live on Streamlit Community Cloud

---

## 🛠️ Tech Stack

| Area | Tools |
|---|---|
| Language | Python |
| Data & analysis | Pandas, NumPy, Seaborn, Matplotlib |
| Machine learning | Scikit-learn, CatBoost, XGBoost |
| Web frameworks | Flask, Streamlit |
| Serialization | Dill |
| Deployment | Streamlit |

---

## 📂 Project Structure

```
Student-performance-predictor/
├── .ebextensions/        # AWS Elastic Beanstalk configuration
├── artifacts/            # Saved model, preprocessor and datasets
├── catboost_info/        # CatBoost training logs
├── logs/                 # Application and pipeline logs
├── notebook/             # EDA and model training notebooks
├── src/                  # Source code (components, pipeline, utils)
│   └── pipeline/
│       └── predict_pipeline.py   # CustomData + PredictPipeline classes
├── templates/            # HTML templates for the Flask app (index.html, home.html)
├── app.py                # Flask application
├── streamapp.py          # Streamlit application
├── python.config         # Deployment config
├── requirements.txt      # Python dependencies
└── .gitignore
```

---

## 🗃️ Dataset & Input Features

The model uses the student exam performance dataset. The prediction form takes:

| Feature | Type | Values |
|---|---|---|
| `gender` | Categorical | male, female |
| `race_ethnicity` | Categorical | group A – group E |
| `parental_level_of_education` | Categorical | some high school, high school, some college, associate's degree, bachelor's degree, master's degree |
| `lunch` | Categorical | standard, free/reduced |
| `test_preparation_course` | Categorical | none, completed |
| `reading_score` | Numeric | 0 – 100 |
| `writing_score` | Numeric | 0 – 100 |

**Target:** `math_score`

---

## 🔄 ML Workflow

1. **Data ingestion** – load the dataset and split it into train and test sets.
2. **Data transformation** – impute missing values, one-hot encode categorical features, and scale numerical features through a preprocessing pipeline.
3. **Model training** – train and compare several regressors, then select the best performer on the test set.
4. **Persistence** – save the best model and the preprocessor to `artifacts/`.
5. **Prediction pipeline** – `CustomData` converts user input into a DataFrame, and `PredictPipeline` loads the saved artifacts and returns the predicted score.

---

## 🚀 Live Demo

Try the app without installing anything: **[https://student-performance--predictor.streamlit.app/](https://student-performance--predictor.streamlit.app/)**

Select the student's details, enter the reading and writing scores, and click **Predict your Maths Score**.

> ℹ️ Free Streamlit apps go to sleep after a period of inactivity. If you see a "wake up" screen, click the button and wait a few seconds.

---

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/Shilpa56721/Student-performance-predictor.git
cd Student-performance-predictor

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Running the Apps

### Option 1: Flask app
```bash
python app.py
```
Open **http://127.0.0.1:5000/** in your browser, then go to `/predictdata` to enter student details and get a prediction.

### Option 2: Streamlit app
```bash
streamlit run streamapp.py
```
Fill in all fields and click **Predict your Maths Score**.

> ⚠️ Both apps load the trained model and preprocessor from `artifacts/`. If those files are missing, train the model first by running the training pipeline in `src/`.

---

## ☁️ Deployment

The repo includes `.ebextensions/` and `python.config` for deploying the Flask app on **AWS Elastic Beanstalk**. In `app.py` the WSGI object is exposed as `application`, which is what Elastic Beanstalk expects.

Typical flow:
```bash
pip install awsebcli
eb init
eb create student-performance-env
eb open
```

---

## 📸 Screenshots

> *Add screenshots of the Flask form and Streamlit app here, for example:*
> ```md
> ![Flask App](images/flask_app.png)
> ![Streamlit App](images/streamlit_app.png)
> ```

---

## 🔮 Future Improvements

- Add model performance metrics (R², RMSE) and comparison charts to this README
- Add support for predicting reading and writing scores
- Containerize with Docker
- Add a CI/CD pipeline with GitHub Actions
- Add unit tests for the pipeline

---

## 👩‍💻 Author

**Shilpa**
GitHub: [@Shilpa56721](https://github.com/Shilpa56721)

---

⭐ If you found this project useful, consider giving it a star!
