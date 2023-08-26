import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, r2_score, mean_squared_error
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, accuracy_score, classification_report, precision_recall_curve
def RandomForest(x_train,y_train,x_test,y_test):
    print(" Random Forest ")
    rf=RandomForestClassifier()
    rf.fit(x_train,y_train)
    rf_pred=rf.predict(x_test)
    rf_df=pd.DataFrame()
    rf_df['actual']=y_test
    rf_df['pred']=rf_pred
    print(rf_df.head())
    print("Accuracy Score : ",accuracy_score(y_test,rf_pred))
    # print(confusion_matrix(y,lr_pred))
    print("Classification Report")
    print(classification_report(y_test,rf_pred))