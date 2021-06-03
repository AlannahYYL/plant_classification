#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import matplotlib.pyplot as plt
import pandas as pd

from config.config import *

# 可视化
with open(train_data_json) as datafile1:
    trainDataFram=pd.read_json(datafile1,orient='records')
with open(val_data_json) as datafile2: #first check if it's a valid json file or not
    validateDataFram =pd.read_json(datafile2,orient='records')
total=trainDataFram.isnull().sum().sort_values(ascending=False)
percent=(trainDataFram.isnull().sum())/(trainDataFram.isnull().count()).sort_values(ascending = False)
missing_validation_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'],sort=False)
# print(missing_validation_data.head())
dataDistribute=trainDataFram.groupby(by=['disease_class']).size()
# print(dataDistribute)
plt.figure(figsize=(50,20),dpi=100)
plt.xticks(range(len(dataDistribute)),dataDistribute.index.tolist(),fontsize=40)
plt.yticks(fontsize=40)
bar=plt.bar(dataDistribute.index.tolist(), dataDistribute.tolist(),width=0.7)
for b in bar:
    h=b.get_height()
    plt.text(b.get_x()+b.get_width()/2,h,int(h),ha='center',fontsize=30)
plt.show()

# 9-16
with open(train_data_json) as train_json:
    train_oridata = pd.read_json(train_json, orient='records')
with open(val_data_json) as val_json:
    val_oridata = pd.read_json(val_json, orient='records')
# print(val_oridata)
# 筛选数据
train_data = train_oridata.drop(train_oridata[(train_oridata['disease_class'] != 9) & (train_oridata['disease_class'] != 10) & (
            train_oridata['disease_class'] != 11) & (train_oridata['disease_class'] != 12) & (
                                                    train_oridata['disease_class'] != 13) & (
                                                    train_oridata['disease_class'] != 14) & (
                                                    train_oridata['disease_class'] != 15) & (
                                                    train_oridata['disease_class'] != 16)].index)
val_data = val_oridata.drop(val_oridata[(val_oridata['disease_class'] != 9) & (val_oridata['disease_class'] != 10) & (
            val_oridata['disease_class'] != 11) & (val_oridata['disease_class'] != 12) & (
                                                    val_oridata['disease_class'] != 13) & (
                                                    val_oridata['disease_class'] != 14) & (
                                                    val_oridata['disease_class'] != 15) & (
                                                    val_oridata['disease_class'] != 16)].index)
# train_data.to_json(train_json_path,orient='records')
# val_data.to_json(val_json_path,orient='records')
#制作新的数据集
for i in range(9,17):
    img_dir = str(i)
    val_img_dir = os.path.join(val_dir,img_dir)
    train_img_dir = os.path.join(train_dir,img_dir)
    if not os.path.exists(val_img_dir):
        os.makedirs(val_img_dir)
    if not os.path.exists(train_img_dir):
        os.makedirs(train_img_dir)
for index,rows in train_data.iterrows():
    ori_trainimg = os.path.join(train_dataset,rows['image_id'])
    p_trainimg = os.path.join(os.path.join(train_dir,str(rows['disease_class'])),rows['image_id'])
    print(ori_trainimg,' ',p_trainimg)
    shutil.copyfile(ori_trainimg,p_trainimg)
for index,rows in val_data.iterrows():
    ori_valimg = os.path.join(val_dataset,rows['image_id'])
    p_valimg = os.path.join(os.path.join(val_dir,str(rows['disease_class'])),rows['image_id'])
    print(ori_valimg,' ',p_valimg)
    shutil.copyfile(ori_valimg,p_valimg)
