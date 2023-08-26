# Anomarly Network Detection

Anomarly Network Detection means that detect network packets and classify them which are attacked or not . For attacked packets , type of attacks is classfied . Then, making prediction of the type of attack for future network packets. 



## Deployment

Installation

```bash
 git clone https://github.com/ChitSuThwin/anomalyNetwork-Detection.git
 cd anomalyNetwork-Detection
 pip install -r requirements.txt
 connet to mysql 
```
Porgram Guide 
```bash
trainingData.py - statistics of Train Data for Data Modelling and Prediction .
testingData.py - statistics of Test Data for Data Modelling and Prediction .
Logistic_Regression.py - modelling and traing Logistic Regression Classifer and giving results
Random_Forest.py - modelling and traing Random_Forest Classifer and giving results
Naive_Bayes.py - modelling and traing Naive_Bayes Classifer and giving results
Decision_Tree.py - modelling and traing Decision_Tree Classifer and giving results
Support_Vector.py - modelling and traing Support_Vector Machine Classifer and giving results
```
