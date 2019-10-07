import os
import random

# trainval_percent = 0.8    #  修改训练集与测试集比例，此时train:test=8:2
# train_percent = 0.7       #  train 占 trainval 中的 0.7 ， 后面只用 trainval，所以这里这个数值不重要
fdir = '../ImageSets/Main'      # 修改对应路径
xmlfilepath = '/root/data/WIDER_FACE/WIDER_val_annotations'  # 修改对应路径
txtsavepath = fdir
total_xml = os.listdir(xmlfilepath)

num=len(total_xml)
list=range(num)
data_list = random.sample(list,num)

fdata = open(fdir + '/val.txt', 'w')

for i  in list:
    name=total_xml[i][:-4]+'\n'
    if i in data_list:
        fdata.write(name)

fdata.close()