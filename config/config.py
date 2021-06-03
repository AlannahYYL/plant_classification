#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
root = '/data/plant2018'

#ori_data
val_dataset = os.path.join(root,r'ai_challenger_pdr2018_validationset_20181023/AgriculturalDisease_validationset/images')
val_data_json = os.path.join(root,r'ai_challenger_pdr2018_validationset_20181023/AgriculturalDisease_validationset/AgriculturalDisease_validation_annotations.json')
train_dataset =os.path.join(root,r'ai_challenger_pdr2018_trainingset_20181023/AgriculturalDisease_trainingset/images')
train_data_json =os.path.join(root, r'ai_challenger_pdr2018_trainingset_20181023/AgriculturalDisease_trainingset/AgriculturalDisease_train_annotations.json')
testa_dataset = os.path.join(root,r'ai_challenger_pdr2018_testa_20181023/AgriculturalDisease_testA/images')
testb_dataset =os.path.join(root,r'ai_challenger_pdr2018_testb_20181023/AgriculturalDisease_testB/images')

#process
val_dir = os.path.join(root,'val')
train_dir = os.path.join(root,'train')
if not os.path.exists(val_dir):
    os.makedirs(val_dir)
if not os.path.exists(train_dir):
    os.makedirs(train_dir)
val_json_path = os.path.join(root,'val.json')
train_json_path = os.path.join(root,'train.json')
