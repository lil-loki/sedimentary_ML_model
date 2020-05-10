import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pickle
df1=pd.read_csv(r"C:\Users\vansi\Desktop\ML\data_Set\data\data\idle\idle-1.csv")
df2=pd.read_csv(r"C:\Users\vansi\Desktop\ML\data_Set\data\data\idle\idle-2.csv")
df3=pd.read_csv(r"C:\Users\vansi\Desktop\ML\data_Set\data\data\idle\idle-3.csv")
df4=pd.read_csv(r"C:\Users\vansi\Desktop\ML\data_Set\data\data\idle\idle-4.csv")
df5=pd.read_csv(r"C:\Users\vansi\Desktop\ML\data_Set\data\data\idle\idle-5.csv")
df6=pd.read_csv(r"C:\Users\vansi\Desktop\ML\data_Set\data\data\running\running-1.csv")
df7=pd.read_csv(r"C:\Users\vansi\Desktop\ML\data_Set\data\data\running\running-2.csv")
df8=pd.read_csv(r"C:\Users\vansi\Desktop\ML\data_Set\data\data\stairs\stairs-1.csv")
df9=pd.read_csv(r"C:\Users\vansi\Desktop\ML\data_Set\data\data\stairs\stairs-2.csv")
df10=pd.read_csv(r"C:\Users\vansi\Desktop\ML\data_Set\data\data\walking\walking-1.csv")
frames=[df1,df2,df3,df4,df5,df6,df7,df8,df9,df10]
all=pd.concat(frames)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(all.drop('idle',axis=1),all['idle'], test_size=0.20,random_state=101)
from sklearn.tree import DecisionTreeClassifier
logmodel =DecisionTreeClassifier()
logmodel.fit(X_train,y_train)
predictions = logmodel.predict(X_test)
from sklearn.metrics import classification_report
print(classification_report(y_test,predictions))
pickle.dump(logmodel,open(r'C:\Users\vansi\Desktop\ML\sedentary_model.sav','wb'))