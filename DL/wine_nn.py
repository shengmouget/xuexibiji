# coding: utf-8 
# @Time    : 2022/11/5 下午8:21
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
from sklearn.neural_network import MLPClassifier  #神经网络
if __name__ == '__main__':
    col_names = ['type','Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium','Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins','Color intensity','Hue','OD280/OD315 of diluted wines','Proline']
    data = pd.read_csv('data/wine.data',header=None,names=col_names)
    m,n = data.shape
    # print(m,n)
    # print(data)
    x = data.iloc[:,1:]
    y = data.iloc[:,:1]
    # print(y)
#     样本分为测试集20%和训练集80%
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)
    # 创建训练模型
    model = MLPClassifier(hidden_layer_sizes=(64,32),activation='relu',learning_rate_init=0.01,max_iter=100)
    model.fit(x_train,y_train)
    y_train_pred = model.predict(x_train)
    # 输出
    print('训练集的正确率：',accuracy_score(y_train,y_train_pred))
    print('混淆矩阵\n',confusion_matrix(y_train,y_train_pred))
    print(classification_report(y_train,y_train_pred,digits=4))
#   测试集
    y_test_pred = model.predict(x_test)
    print('测试集的正确率:',accuracy_score(y_test,y_test_pred))
    print('混淆矩阵:',confusion_matrix(y_test,y_test_pred))
    print(classification_report(y_test,y_test_pred,digits=4))