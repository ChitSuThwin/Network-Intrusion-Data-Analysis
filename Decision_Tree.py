import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree  import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, r2_score, mean_squared_error
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, accuracy_score, classification_report, precision_recall_curve
def DecisionTree(x_train,y_train,x_test,y_test):
    print(" Decision Tree")
    ds = DecisionTreeClassifier()
    ds.fit(x_train,y_train)
    ds_pred=ds.predict(x_test)
    ds_df=pd.DataFrame()
    ds_df['actual']=y_test
    ds_df['pred']=ds_pred
    fig = plt.figure(figsize = (30,12))
    tree.plot_tree(ds, filled=True)
    plt.show()
    print(ds_df.head())
    print("Accuracy Score : ",accuracy_score(y_test,ds_pred))
    print("Classification Report")
    # print(confusion_matrix(y,lr_pred))
    print(classification_report(y_test,ds_pred))