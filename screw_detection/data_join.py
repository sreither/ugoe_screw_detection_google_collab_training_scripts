#!/usr/bin/env python
import os
from glob import glob
from tqdm.autonotebook import tqdm
import shutil
import argparse


def create_dir(_path):
    if not os.path.exists(_path):
        os.mkdir(_path)


def merge_dir(_dir):
    for class_name in class_names:
        count = 0
        if class_name == 'non_screw':
            class_dir = os.path.join(dest_dir, class_name)
            create_dir(class_dir)
        else:
            class_dir = os.path.join(dest_dir, 'screw')
            create_dir(class_dir)

        source_dir = os.path.join(_dir, class_name)

        src_paths = glob(os.path.join(source_dir,'*.jpg'))
        for src_ipath in tqdm(src_paths):
            dest_ipath = os.path.join(class_dir, f"{count}.jpg")
            shutil.copyfile(src_ipath, dest_ipath)
            count += 1
        src_paths = glob(os.path.join(source_dir, '*.png'))
        for src_ipath in tqdm(src_paths):
            dest_ipath = os.path.join(class_dir, f"{count}.png")
            shutil.copyfile(src_ipath, dest_ipath)
            count += 1


def get_input_args():
    ''' 
        1. Read command line arguments and convert them into the apropriate data type. 
        2. Returns a data structure containing everything that have been read, or the default values 
        for the paramater that haven't been explicitly specified.
    '''
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--src_dir', type=str, default=os.path.join(os.getcwd(), 'src'),
                        help='The folder of the collected images')

    parser.add_argument('--dataset_dir', type=str, default=os.path.join(os.getcwd(), 'dataset'),
                        help='The folder of the base dataset')

    parser.add_argument('--dest_dir', type=str, default=os.path.join(os.getcwd(), 'data'),
                        help='Target folder for the new combined dataset')

    in_args = parser.parse_args()

    return in_args


if __name__ == '__main__':
    args = get_input_args()
    src_dir = args.src_dir if os.path.exists(args.src_dir) else os.path.join(os.getcwd(), 'src')
    dataset_dir = args.dataset_dir if os.path.exists(args.src_dir) else os.path.join(os.getcwd(), 'dataset')
    class_names = os.listdir(dataset_dir)
    print('Found Classes:', class_names)
    dest_dir = args.dest_dir if os.path.exists(args.dest_dir) else os.path.join(os.getcwd(), 'data')

    create_dir(dest_dir)
    merge_dir(src_dir)
    merge_dir(dataset_dir)




