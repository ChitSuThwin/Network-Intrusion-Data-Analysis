import warnings
warnings.filterwarnings("ignore")

from sql_connection import mydb
from trainingData import x_train_transformed,y_train
from testingData import x_transformed_test,y_test
from Logicstic_Regression import Logistic_Regression
from Random_Forest import RandomForest
from Decision_Tree import DecisionTree
from Naive_Bayes import NaiveBayes
from Support_Vector import svm


Logistic_Regression(x_train_transformed,y_train,x_transformed_test,y_test)
RandomForest(x_train_transformed,y_train,x_transformed_test,y_test)
DecisionTree(x_train_transformed,y_train,x_transformed_test,y_test)
NaiveBayes(x_train_transformed,y_train,x_transformed_test,y_test)
svm(x_train_transformed,y_train,x_transformed_test,y_test)