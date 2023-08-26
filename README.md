# Anomarly Network Detection

Anomarly Network Detection means that detect network packets and classify them which are attacked or not . For attacked packets , type of attacks is classfied . Then, making prediction of the type of attack for future network packets. 



# Installation & Program Guide

Installation

```bash
 git clone https://github.com/ChitSuThwin/anomalyNetwork-Detection.git
 cd anomalyNetwork-Detection
 pip install -r requirements.txt
 connet to mysql 
```
Porgram Guide 
```bash
analysis.py -Analyzing resuls of multiple classifier
trainingData.py - statistics of Train Data for Data Modelling and Prediction 
testingData.py - statistics of Test Data for Data Modelling and Prediction
Logistic_Regression.py - modelling and traing Logistic Regression Classifer and giving results
Random_Forest.py - modelling and traing Random Forest Classifer and giving results
Naive_Bayes.py - modelling and traing Naive Bayes Classifer and giving results
Decision_Tree.py - modelling and traing Decision Tree Classifer and giving results
Support_Vector.py - modelling and traing Support Vector Machine Classifer and giving results
```
