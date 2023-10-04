# -*- coding: utf-8 -*-
"""BankTermModel.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iVHIkTvFDlm7kpXXmNjqApKGiE85O7c5
"""

#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing

#loading the data set into data frame
df = pd.read_csv('/content/bank-full_edited.csv')
df

df.shape

#The top 5 records of the data set
df.head()

#The data set's data types, null values count
df.info()

#Replacing the target variable 'yes' with 1
df['y'] = df['y'].replace('yes', 1)

#Replacing the target variable 'no' with 0
df['y'] = df['y'].replace('no', 0)

#The values & counts of the feature 'AGE'
age_counts = df['age'].value_counts()

age_counts,df.age.mean()

#The values & counts of the feature 'job'
job_counts = df['job'].value_counts()
job_counts

#The values & counts of the feature 'marital'
marital_counts = df["marital"].value_counts()
marital_counts

#The values & counts of the feature 'education'
education_counts = df['education'].value_counts()
education_counts

#The values & counts of the feature 'housing'
housingloan_counts = df['housing'].value_counts()
housingloan_counts

#The values & counts of the feature 'contact'
contact_counts = df['contact'].value_counts()
contact_counts

#The values & counts of the feature 'month'
contact_month_counts = df['month'].value_counts()
contact_month_counts

#The values & counts of the feature 'poutcome'
prev_outcome_counts = df['poutcome'].value_counts()
prev_outcome_counts

#Now, we look at the counts of the target variable; if they subscribed to the term deposit
outcome_counts = df['y'].value_counts()
outcome_counts

#dummying all categorical values
job = pd.get_dummies(df['job'],drop_first=True)
marital =pd.get_dummies(df['marital'],drop_first=True)
education=pd.get_dummies(df['education'],drop_first=True)
housing=pd.get_dummies(df['housing'],drop_first=True)
loan =pd.get_dummies(df['loan'],drop_first=True)
contact=pd.get_dummies(df['contact'],drop_first=True)
month=pd.get_dummies(df['month'],drop_first=True)
poutcome=pd.get_dummies(df['poutcome'],drop_first=True)

#dropping the columns which aren't needed
df.drop(['default','job','marital','education','housing','loan','contact','month','poutcome'],axis=1,inplace=True)

#concatenate new columns
df=pd.concat([df,job,marital,education,housing,loan,contact,month,poutcome],axis=1)

df

df.describe()

#The columns/features of data set
df.columns

#Making sure all the features are in numerical values
df.dtypes

#Taking a look at the data set with relevant features
df.head()

#Checking for null values
df.isnull().sum()

"""EDA

"""

#DISTRIBUTION OF AGES
plt.figure(figsize=(7,4))
plt.boxplot(df['age'],vert=False)
plt.show()

#EDA :: Correlation matrix
correlation_matrix = df.corr()
correlation_matrix

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

#Seperating the target variable from the data set
X = df.drop('y', axis=1)
y = df['y']

#Splitting the data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train.shape, X_test.shape

"""LOGISITIC REGRESSION MODEL"""

#Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)*100
print(f'Accuracy: {accuracy:.2f}')
#Accuracy: 88.80

confusion = confusion_matrix(y_test, y_pred)
print('Confusion Matrix:')
print(confusion)
#Confusion Matrix:
#[[7797  155]
# [ 851  240]]

report = classification_report(y_test, y_pred)
print('Classification Report:')
print(report)

"""DECISION TREE MODEL"""

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=0)

clf.fit(X_train, y_train)

y_pred_gini=clf.predict(X_test)

from sklearn.metrics import accuracy_score

print('Model accuracy score with criterion gini index: {0:0.2f}'. format(accuracy_score(y_test, y_pred_gini)*100))
#Model accuracy score with criterion gini index: 89.59

report = classification_report(y_test, y_pred)
print('Classification Report:')
print(report)

confusion = confusion_matrix(y_test, y_pred)
print('Confusion Matrix:')
print(confusion)
#Confusion Matrix:
#[[7716  236]
 #[ 639  452]]

"""RANDOM FOREST MODEL"""

from sklearn.ensemble import RandomForestClassifier

rfc= RandomForestClassifier(criterion='gini', random_state=0)

rfc.fit(X_train,y_train)

y_pred = rfc.predict(X_test)

from sklearn.metrics import accuracy_score

print('Model accuracy score : {0:0.4f}'. format(accuracy_score(y_test, y_pred)*100))
#Model accuracy score : 90.3240

confusion = confusion_matrix(y_test, y_pred)
print('Confusion Matrix:')
print(confusion)
#Confusion Matrix:
#[[7716  236]
# [ 639  452]]

report = classification_report(y_test, y_pred)
print('Classification Report:')
print(report)