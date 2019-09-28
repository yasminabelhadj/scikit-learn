clf1= svm.OneClassSVM(nu=0.1 , kernel = "rbf" , gamma=0.5)

clf1.fit(x_train1,y_train1)

import numpy as np
X_test1 = np.concatenate((x_test1,data0),axis=0)
y_pred_test_2=clf1.predict(X_test1)
Y_test1= np.concatenate ((y_test1, label0-1),axis=0)
dataset_selected1= dataset.loc[dataset['Outcome'].isin([1])]

dataset_selected0= dataset.loc[dataset['Outcome'].isin([0])]

label1 = dataset_selected1['Outcome']
label0 = dataset_selected0['Outcome']
data0=dataset_selected0.drop(['Outcome'],axis =1)# to know the type of the data
data1=dataset_selected1.drop(['Outcome'],axis =1)# to know the type of the data

x_train1 , x_test1 , y_train1 , y_test1 = train_test_split(data1, label1, test_size=0.33,random_state=0)

x_train0 , x_test0 , y_train0 , y_test0 = train_test_split(data0, label0, test_size=0.33,random_state=0)

clf1= svm.OneClassSVM(nu=0.1 , kernel = "rbf" , gamma=0.5)

clf1.fit(x_train1,y_train1)

import numpy as np
X_test1 = np.concatenate((x_test1,x_test0),axis=0)
Y_test1= np.concatenate ((y_test1, y_test0 - 1),axis=0)

y_pred_test_2=clf1.predict(X_test1)
Y_test1= np.concatenate ((y_test1, y_test0 - 1),axis=0)
dataset_selected1= dataset.loc[dataset['Outcome'].isin([1])]

dataset_selected0= dataset.loc[dataset['Outcome'].isin([0])]

label1 = dataset_selected1['Outcome']
label0 = dataset_selected0['Outcome']
data0=dataset_selected0.drop(['Outcome'],axis =1)# to know the type of the data
data1=dataset_selected1.drop(['Outcome'],axis =1)# to know the type of the data

x_train1 , x_test1 , y_train1 , y_test1 = train_test_split(data1, label1, test_size=0.33,random_state=0)

x_train0 , x_test0 , y_train0 , y_test0 = train_test_split(data0, label0, test_size=0.33,random_state=0)

clf1= svm.OneClassSVM(nu=0.3 , kernel = "rbf" , gamma=0.4)

clf1.fit(x_train1,y_train1)

import numpy as np
X_test1 = np.concatenate((x_test1,x_test0),axis=0)
Y_test1= np.concatenate ((y_test1, y_test0 - 1),axis=0)


y_pred_test_2=clf1.predict(X_test1)
y_pred_test_2=clf1.predict(X_test1)
acc= accuracy_score(Y_test1 , y_pred_test_2)
import numpy as np
X_test1 = np.concatenate((x_test1,x_test0),axis=0)
Y_test1= np.concatenate ((y_test1, y_test0 - 1),axis=0)
l=len(X_test1.shape[1])
l2=len(x_test1.shape[1])
dataset_selected1= dataset.loc[dataset['Outcome'].isin([1])]

dataset_selected0= dataset.loc[dataset['Outcome'].isin([0])]

label1 = dataset_selected1['Outcome']
label0 = dataset_selected0['Outcome']
data0=dataset_selected0.drop(['Outcome'],axis =1)# to know the type of the data
data1=dataset_selected1.drop(['Outcome'],axis =1)# to know the type of the data

x_train1 , x_test1 , y_train1 , y_test1 = train_test_split(data1, label1, test_size=0.33,random_state=0)

x_train0 , x_test0 , y_train0 , y_test0 = train_test_split(data0, label0, test_size=0.33,random_state=0)

clf1= svm.OneClassSVM(nu=0.3 , kernel = "rbf" , gamma=0.4)

clf1.fit(x_train1,y_train1)

import numpy as np
X_test1 = np.concatenate((x_test1,x_test0),axis=0)
Y_test1= np.concatenate ((y_test1, y_test0 - 1),axis=0)
l=X_test1.size()
l2=x_test1.size()


y_pred_test_2=clf1.predict(X_test1)
acc= accuracy_score(Y_test1 , y_pred_test_2)
import numpy as np
X_test1 = np.concatenate((x_test1,x_test0),axis=0)
Y_test1= np.concatenate ((y_test1, y_test0 - 1),axis=0)
l=X_test1.shape[1]
l2=x_test1.shape[1]


y_pred_test_2=clf1.predict(X_test1)
acc= accuracy_score(Y_test1 , y_pred_test_2)
import numpy as np
X_test1 = np.concatenate((x_test1,x_test0),axis=0)
Y_test1= np.concatenate ((y_test1, y_test0 - 1),axis=0)
l=X_test1.shape[0]
l2=x_test1.shape[0]

## ---(Fri Sep 27 21:58:36 2019)---
runfile('C:/Users/user/.spyder-py3/business.py', wdir='C:/Users/user/.spyder-py3')
sp500_df
runfile('C:/Users/user/.spyder-py3/business.py', wdir='C:/Users/user/.spyder-py3')
stock_price
runfile('C:/Users/user/.spyder-py3/business.py', wdir='C:/Users/user/.spyder-py3')