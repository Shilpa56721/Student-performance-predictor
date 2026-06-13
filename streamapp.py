import streamlit as st
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

def main():
    st.set_page_config(page_title="Student Exam Performance Indicator")
    
    st.title("Student Exam Performance Indicator")
    st.header("Student Exam Performance Prediction")

    # Using st.form to match the HTML <form> behavior
    with st.form("predict_form"):
        # Dropdowns
        gender = st.selectbox(
            "Gender", 
            options=["male", "female"],
            index=None,
            placeholder="Select your Gender"
        )
        
        ethnicity = st.selectbox(
            "Race or Ethnicity", 
            options=["group A", "group B", "group C", "group D", "group E"],
            index=None,
            placeholder="Select Ethnicity"
        )
        
        parental_level_of_education = st.selectbox(
            "Parental Level of Education", 
            options=[
                "associate's degree", 
                "bachelor's degree", 
                "high school", 
                "master's degree", 
                "some college", 
                "some high school"
            ],
            index=None,
            placeholder="Select Parent Education"
        )
        
        lunch = st.selectbox(
            "Lunch Type", 
            options=["free/reduced", "standard"],
            index=None,
            placeholder="Select Lunch Type"
        )
        
        test_preparation_course = st.selectbox(
            "Test Preparation Course", 
            options=["none", "completed"],
            index=None,
            placeholder="Select Test_course"
        )

        # Number Inputs
        writing_score = st.number_input(
            "Writing Score out of 100", 
            min_value=0, 
            max_value=100, 
            value=0,
            step=1
        )
        
        reading_score = st.number_input(
            "Reading Score out of 100", 
            min_value=0, 
            max_value=100, 
            value=0,
            step=1
        )

        # Submit Button
        submit_button = st.form_submit_button(label="Predict your Maths Score")

    # Logic to execute upon form submission
    if submit_button:
        # Basic validation to ensure dropdowns aren't left empty
        if None in [gender, ethnicity, parental_level_of_education, lunch, test_preparation_course]:
            st.error("Please ensure all fields are selected before predicting.")
        else:
            # 1. Map the inputs to CustomData
            data = CustomData(
                gender=gender,
                race_ethnicity=ethnicity,
                parental_level_of_education=parental_level_of_education,
                lunch=lunch,
                test_preparation_course=test_preparation_course,
                reading_score=reading_score,
                writing_score=writing_score
            )
            
            # 2. Convert to DataFrame
            pred_df = data.get_data_as_data_frame()
            
            # 3. Predict via Pipeline
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            
            # 4. Display the result
            st.success("Prediction Complete!")
            st.subheader(f"THE prediction is {results}")

if __name__ == "__main__":
    main()