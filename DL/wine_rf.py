# coding: utf-8 
# @Time    : 2022/11/4 下午5:31
# 决策树 / 随机森林 svm
# from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report   #计算正确率 混淆矩阵
from sklearn.model_selection import train_test_split # 数据分割
from sklearn.ensemble import RandomForestClassifier  #随机森林

import pandas as pd
import numpy as np
if __name__ == '__main__':
    # 显示问题
    pd.set_option('display.max_columns',20)
    pd.set_option('display.width',1000)
    col_names = ['type','Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium','Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins','Color intensity','Hue','OD280/OD315 of diluted wines','Proline']
    data = pd.read_csv('data/wine.data',header=None,names=col_names)
    y = data['type']
    x = data.iloc[:,1:]
    # print(x)
    # print(y)
    # x的其他写法
    # x = data.drop(labels='type',axis=1,inplace=False)
    # 建立决策树模型
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
    model = RandomForestClassifier(n_estimators=20,criterion='gini',max_depth=5,min_samples_split=5,max_features=0.8,min_samples_leaf=3,random_state=2020)
    model.fit(x_train,y_train)
    # 重要度
    # print('特征:',col_names[1:])
    # print('重要度:',model.feature_importances_)
    fi = pd.DataFrame(index=col_names[1:],data=model.feature_importances_,columns=['特征重要度'])
    fi.sort_values(by='特征重要度',ascending=False,inplace=True)
    print(fi)
    # y_pred = model.predict(x)
    y_train_pred = model.predict(x_train)
    # print(pd.value_counts(y_train_pred == y_train))
    # print(pd.value_counts(y_test_pred == y_test))
    # print(np.mean(y_train_pred == y_train))
    print('训练集正确率：',accuracy_score(y_train,y_train_pred))
    print('混淆矩阵:\n',confusion_matrix(y_train,y_train_pred))
    print(classification_report(y_train,y_train_pred,digits=3))
    y_test_pred = model.predict(x_test)
    print('测试集正确率:',accuracy_score(y_test,y_test_pred))
    print('混淆矩阵:\n',confusion_matrix(y_test,y_test_pred))
    print(classification_report(y_test,y_test_pred,digits=3))


