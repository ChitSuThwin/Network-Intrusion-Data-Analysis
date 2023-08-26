import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, r2_score, mean_squared_error
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, accuracy_score, classification_report, precision_recall_curve
def svm(x_train,y_train,x_test,y_test):
    print(" Support Vector Machine ")
    sm=SVC()
    sm.fit(x_train,y_train)
    sm_pred=sm.predict(x_test)
    sm_df=pd.DataFrame()
    sm_df['actual']=y_test
    sm_df['pred']=sm_pred
    print(sm_df.head())
    print("Accuracy Score : ",accuracy_score(y_test,sm_pred))
    # print(confusion_matrix(y,lr_pred))
    print("Classification Report")
    print(classification_report(y_test,sm_pred))