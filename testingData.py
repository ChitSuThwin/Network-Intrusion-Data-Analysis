import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from collections import Counter
from sklearn.preprocessing import LabelEncoder, StandardScaler
import warnings
warnings.filterwarnings("ignore")
from sql_connection import mydb
anormal_testing_data=pd.read_sql_query("SELECT * FROM testdata",mydb)
df_test=pd.DataFrame(anormal_testing_data,columns=["duration","protocol_type","service","flag","src_bytes","dst_bytes","land",
"wrong_fragment","urgent","hot","num_failed_logins","logged_in",
"num_compromised","root_shell","su_attempted","num_root","num_file_creations",
"num_shells","num_access_files","num_outbound_cmds","is_host_login",
"is_guest_login","count","srv_count","serror_rate", "srv_serror_rate",
"rerror_rate","srv_rerror_rate","same_srv_rate", "diff_srv_rate", "srv_diff_host_rate","dst_host_count","dst_host_srv_count","dst_host_same_srv_rate",
"dst_host_diff_srv_rate","dst_host_same_src_port_rate",
"dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate",
"dst_host_rerror_rate","dst_host_srv_rerror_rate","attack", "last_flag"]
)
print(df_test.head())
print(df_test.shape) 
print(df_test.describe())


df_test.drop(['land','urgent','num_failed_logins','num_outbound_cmds'],axis=1,inplace=True)
print(df_test.isna().sum())
print(df_test.select_dtypes(exclude=[np.number])) 
df_test['attack'].loc[df_test['attack']!='normal']=df_test['attack']
y_test=df_test['attack']
print(y_test)
# fig, ax = plt.subplots(figsize=(20,200))
sns.catplot(data=df_test, y="attack",kind="count")
plt.show()
print("Class distribution: {}".format(Counter(y_test)))

le=LabelEncoder()
df_test['protocol_type']=le.fit_transform(df_test['protocol_type'])
df_test['service']=le.fit_transform(df_test['service'])
df_test['flag']=le.fit_transform(df_test['flag'])
df_test['attack']=le.fit_transform(df_test['attack'])
x_test=df_test.drop(['attack'],axis=1)
print(x_test)
#fig, ax = plt.subplots(figsize=(100, 5))



scaler=StandardScaler()
scaler.fit(x_test)
x_transformed_test=scaler.transform(x_test)
