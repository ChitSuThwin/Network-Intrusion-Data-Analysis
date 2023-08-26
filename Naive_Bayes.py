import pandas as pd
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import confusion_matrix, r2_score, mean_squared_error
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, accuracy_score, classification_report, precision_recall_curve
def NaiveBayes(x_train,y_train,x_test,y_test):
    print(" Naive Bayes")
    Nb = BernoulliNB()
    Nb.fit(x_train,y_train)
    Nb_pred=Nb.predict(x_test)
    Nb_df=pd.DataFrame()
    Nb_df['actual']=y_test
    Nb_df['pred']=Nb_pred
    print(Nb_df.head())
    print("Accuracy Score : ",accuracy_score(y_test,Nb_pred))
    # print(confusion_matrix(y,lr_pred))
    print("Classification Report")
    print(classification_report(y_test,Nb_pred))