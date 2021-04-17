#!/usr/bin/env python
import h5py 
import cv2
import numpy as np
import os
from glob import glob
import matplotlib.pyplot as plt
from tqdm.notebook import tqdm
import argparse



def create_dir(_path):
    if not os.path.exists(_path):
        os.mkdir(_path)

def saveh5(path,data):
    hf = h5py.File(path,'w')
    hf.create_dataset('data',data=data)
    hf.close()

def readh5(d_path):
    data=h5py.File(d_path, 'r')
    data = np.array(data['data'])
    return data

def create_h5_data(_dir,iden,h5path):
    print('Creating Data Store:',iden)
    data=[]
    for img_path in tqdm(glob(os.path.join(_dir,'*.*'))):
        img=cv2.imread(img_path)
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img=cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        data.append(img)
    data=np.array(data)
    saveh5(h5path,data)

def create_ds(_dir,ds_dir):
    for class_name in class_names:
        # source
        class_dir=os.path.join(_dir,class_name)
        # h5
        h5path=os.path.join(ds_dir,f"{class_name}.h5")
        # datastore
        create_h5_data(class_dir,class_name,h5path)
  
def get_input_args():
    ''' 
        1. Read command line arguments and convert them into the apropriate data type. 
        2. Returns a data structure containing everything that have been read, or the default values 
        for the paramater that haven't been explicitly specified.
    '''
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--work_dir',  type = str, default=os.getcwd(),help = 'Where the folders old and new')


    in_args = parser.parse_args()

    return in_args


if __name__ == '__main__':
    args = get_input_args()
    # fixed params
    dim=(75,75) #based on minimum dimension of the models
    work_dir = args.work_dir if os.path.exists(args.work_dir) else os.getcwd()
    #class_names=set(os.listdir(work_dir))
    class_names=[filename for filename in os.listdir(work_dir) if os.path.isdir(os.path.join(work_dir,filename))]
    print('Found Classes:', class_names)

    create_ds(work_dir, os.getcwd())
