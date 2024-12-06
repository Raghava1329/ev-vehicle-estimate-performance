#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt


# In[2]:


df=pd.read_csv('D:/Burnoutrate.csv')
df


# In[3]:


x=df.iloc[:,:4]
y=df.iloc[:,-1]
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)


# In[4]:


X = df[["Existing rate"]]
Y = df["Burnout"]

#LINEAR REGRESSION
mdl = LinearRegression()
mdl.fit(X, Y)
pred = mdl.predict([[66]])
print("Predicted value (LR): ",pred[0])
print("Accuracy (LR): ",mdl.score(X[:100], Y[:100])*100)

plt.scatter(X['Existing rate'], Y, color='b')
plt.plot(X['Existing rate'], mdl.predict(X),color='black',linewidth=3)
plt.xlabel('Existing rate')  
plt.ylabel('Burnout') 
plt.show()


# In[5]:


#SVR
from sklearn.svm import SVR
mdl = SVR(kernel = 'rbf')
mdl.fit(X, Y)
pred = mdl.predict([[6.575]])
print("Predicted value (SVR): ",pred[0])
print("Accuracy (SVR): ",mdl.score(X[:100], Y[:100])*100)

plt.scatter(X['Existing rate'], Y, color='b')
plt.plot(X['Existing rate'], mdl.predict(X),color='black',linewidth=3)
plt.xlabel('Existing rate')
plt.ylabel('Burnout')
plt.show()


# In[6]:


#RANDOM FOREST REGRESSION
from sklearn.ensemble import RandomForestRegressor
mdl = RandomForestRegressor(n_estimators=100,max_depth=6)
mdl.fit(X, Y)
pred = mdl.predict([[66]])
print("Predicted value (RFR): ",pred[0])
print("Accuracy (RFR): ",mdl.score(X[:100], Y[:100])*100)

plt.scatter(X['Existing rate'], Y, color='b')
plt.plot(X['Existing rate'], mdl.predict(X),color='black',linewidth=3)
plt.xlabel('Existing rate')  
plt.ylabel('Burnout') 
plt.show()


# In[17]:


from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)
score=regressor.score(x_train,y_train)
y_predL=regressor.predict(x_test)
print("Accuracy of Linear Regression",score)
y_predL=regressor.predict(x_test)

MAE=mean_absolute_error(y_test,y_predL)
print("MAE",MAE)
 


# In[20]:


from sklearn.ensemble import RandomForestRegressor
rf_model=RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(x_train, y_train)
y_pred=rf_model.predict(x_test)

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
mse=mean_squared_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)
mae=mean_absolute_error(y_test,y_pred)
print("Mean Square Error of RandomForest Regression",mse)
print("R2 score of RandomForest Regression",r2)
print("Mean absolute Error of RandomForest Regression",mae)


# In[22]:


from sklearn.svm import SVR
svr=SVR(kernel='rbf')
svr.fit(x_train,y_train)

# Make predictions on the test set
y_preds=svr.predict(x_test)

# Evaluate the model
mse=mean_squared_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)
mae=mean_absolute_error(y_test,y_pred)
print("Mean Square Error of RandomForest Regression",mse)
print("R2 score of RandomForest Regression",r2)
print("Mean absolute Error of RandomForest Regression",mae)


# In[ ]:




