# Explainable Diabetes Prediction System

An AI/ML-based web application that predicts diabetes risk using patient health parameters and provides a simple, understandable explanation of the factors associated with the prediction.

## Problem Statement

**Explainable Diabetes Prediction:** Develop an explainable machine learning system that predicts diabetes risk and displays the major factors influencing the prediction.

## Overview

The system accepts selected patient health parameters and uses a trained machine learning model to estimate diabetes risk.

Along with the prediction, the application provides a simplified explanation of the entered health factors so that the result is easier to understand.

> This project is intended for educational and academic purposes and should not be used as a substitute for professional medical diagnosis.

## Features

- Diabetes risk prediction
- Prediction probability
- Explainable prediction results
- Patient-factor analysis
- Interactive Streamlit interface
- Real-time input updates
- Simple visualization of prediction probability
- Educational information about diabetes

## Input Parameters

The application uses the following parameters:

| Parameter | Description |
|---|---|
| Pregnancies | Number of pregnancies |
| Glucose | Blood glucose level |
| Insulin | Insulin level |
| BMI | Body Mass Index |
| Age | Age of the patient |

## System Workflow

```text
Patient Health Parameters
          |
          v
     Preprocessing
          |
          v
 Machine Learning Model
          |
          v
 Diabetes Risk Prediction
          |
          +------------------+
          |                  |
          v                  v
   Risk Probability    Factor Explanation
          |                  |
          +--------+---------+
                   |
                   v
          Streamlit Dashboard
```

## Explainability

The application includes a **"Why This Prediction?"** section.

It summarizes important patient parameters and presents them in an understandable format.

Example:

| Factor | Patient Value | Level |
|---|---:|---|
| Glucose | 160 | High |
| BMI | 35.2 | High |
| Age | 42 | Moderate |
| Insulin | 120 | Normal |
| Pregnancies | 2 | Low |

The displayed contextual levels are intended to make the entered parameters easier to interpret. They should not be treated as independent medical diagnoses or causal explanations.

## Technology Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Joblib
- Plotly

## Project Structure

```text
Explainable-Diabetes-Prediction/
│
├── app/
│   ├── about.py
│   ├── explainer.py
│   ├── explanation.py
│   ├── header.py
│   └── predict.py
│
├── data/
│
├── datasets/
│
├── main.py
├── loader.py
├── model.pkl
├── requirements.txt
└── README.md
```

The exact contents may vary slightly depending on the current project version.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/shamald09/Explainable-Diabetes-Prediction.git
cd Explainable-Diabetes-Prediction
```

### 2. Create a virtual environment

On Windows:

```bash
py -3.11 -m venv venv
```

Activate it in PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Or in Command Prompt:

```cmd
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m streamlit run main.py
```

Streamlit will display the local application URL in the terminal, typically:

```text
http://localhost:8501
```

## Example

### Input

```text
Pregnancies: 2
Glucose: 160
Insulin: 120
BMI: 35.2
Age: 42
```

### Output

The application displays:

```text
Prediction: Diabetes Risk / No Diabetes
Probability: XX%
```

followed by a simple explanation of the relevant patient factors.

## Machine Learning Pipeline

```text
Dataset
   ↓
Data Preprocessing
   ↓
Feature Processing
   ↓
Model Training
   ↓
Saved ML Model
   ↓
Patient Input
   ↓
Prediction
   ↓
Probability + Explanation
```

## Dataset

The project is based on diabetes-related patient health data derived from the Pima Indians Diabetes dataset.

The dataset contains clinical attributes used for diabetes classification.

## Future Improvements

Possible future enhancements include:

- Support for additional clinical parameters
- Comparison of multiple ML algorithms
- Improved model-level explainability
- Patient history tracking
- Improved dashboard visualizations
- Model evaluation on additional datasets

## Disclaimer

This application is an academic machine-learning project. Predictions and displayed explanations are for educational purposes and are **not medical diagnoses or treatment recommendations**.

## Acknowledgement

This project is based on and modified from the open-source **UznetDev Diabetes Prediction** project.

Original repository:

https://github.com/UznetDev/Diabetes-Prediction

The application has been modified and simplified for an academic mini-project, including changes to the user interface and explainability presentation.

Please refer to the repository's license for applicable licensing terms.

## Author

**Shamal Deore**

B.Tech Information Technology  
K. J. Somaiya Institute of Technology
