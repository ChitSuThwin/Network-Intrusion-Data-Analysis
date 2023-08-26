import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, r2_score, mean_squared_error
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, accuracy_score, classification_report, precision_recall_curve
def Logistic_Regression(x_train,y_train,x_test,y_test):
    print(" Logistic Regression ")
    lr=LogisticRegression()
    lr.fit(x_train,y_train)
    lr_pred=lr.predict(x_test)
    lr_df=pd.DataFrame()
    lr_df['actual']=y_test
    lr_df['pred']=lr_pred
    print(lr_df.head())
    print("Accuracy Score : ",accuracy_score(y_test,lr_pred))
    # print(confusion_matrix(y,lr_pred))
    print("Classification Report")
    print(classification_report(y_test,lr_pred))