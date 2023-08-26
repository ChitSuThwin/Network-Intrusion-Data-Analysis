import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from collections import Counter
from sklearn.preprocessing import LabelEncoder, StandardScaler
import warnings
warnings.filterwarnings("ignore")
from sql_connection import mydb

anormal_data=pd.read_sql_query("SELECT * FROM training",mydb)
df=pd.DataFrame(anormal_data,columns=["duration","protocol_type","service","flag","src_bytes","dst_bytes","land",
"wrong_fragment","urgent","hot","num_failed_logins","logged_in",
"num_compromised","root_shell","su_attempted","num_root","num_file_creations",
"num_shells","num_access_files","num_outbound_cmds","is_host_login",
"is_guest_login","count","srv_count","serror_rate", "srv_serror_rate",
"rerror_rate","srv_rerror_rate","same_srv_rate", "diff_srv_rate", "srv_diff_host_rate","dst_host_count","dst_host_srv_count","dst_host_same_srv_rate",
"dst_host_diff_srv_rate","dst_host_same_src_port_rate",
"dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate",
"dst_host_rerror_rate","dst_host_srv_rerror_rate","attack", "last_flag"]
)

print(df.head())
print(df.shape) 
print(df.describe())

df.drop(['land','urgent','num_failed_logins','num_outbound_cmds'],axis=1,inplace=True)
print(df.isna().sum())
print(df.select_dtypes(exclude=[np.number])) 
df['attack'].loc[df['attack']!='normal']=df['attack']
y_train=df['attack']
print(y_train)

sns.catplot(data=df, y="attack",kind="count")
plt.show()

le=LabelEncoder()
df['protocol_type']=le.fit_transform(df['protocol_type'])
df['service']=le.fit_transform(df['service'])
df['flag']=le.fit_transform(df['flag'])
df['attack']=le.fit_transform(df['attack'])
x_train=df.drop(['attack'],axis=1)
print(x_train)
#fig, ax = plt.subplots(figsize=(100, 5))

print("Class distribution: {}".format(Counter(y_train)))

scaler=StandardScaler()
scaler.fit(x_train)
x_train_transformed=scaler.transform(x_train)