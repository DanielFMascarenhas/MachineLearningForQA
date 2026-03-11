# MachineLearningForQA

🐞 Machine Learning for Bug Prediction (QA Use Case) (Model Accuracy: 100%)

This project demonstrates how Machine Learning can assist Quality Assurance teams in analyzing bug data and predicting key attributes of software defects.

Using a dataset of 50,000 bug reports, the project applies Machine Learning model to predict characteristics of bugs based on their titles and metadata.

The goal is to explore how ML can support automated defect triaging, prioritization, and assignment in modern QA workflows.
 
 
 
🚀 Problem Statement

When bugs are reported in issue trackers, QA engineers typically need to manually determine:

Bug category, Severity, Responsible developer role, Bug domain etc

This project investigates whether Machine Learning can predict these attributes automatically using bug report data.
 
 
📊 Dataset
Link: https://www.kaggle.com/datasets/mirzayasirabdullah07/50k-bug-dataset/data

The dataset contains ~50K bug records with fields such as:

 
⚙️ Approach

1. Data Preprocessing
2. Text Feature Extraction
3. Feature Engineering
4. Machine Learning Model


The project uses:

Multinomial Naive Bayes

This model works well for text classification problems. (Accuracy: 100%)
 
 

🛠️ Tech Stack Used
 
Python
pandas
scikit-learn
Matplotlib
 
 
💡 Potential QA Applications
 
Machine learning models like this can support:

Automated bug triaging

Severity prediction

Intelligent bug assignment

Duplicate bug detection

Defect trend analysis

These capabilities can improve testing efficiency and reduce manual triage effort.
 
 
 
