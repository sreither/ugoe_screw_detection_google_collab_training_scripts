#!/bin/bash

if [ ! $# -eq 2 ]; then
    echo "Please specifiy which weights should be downloaded and where to store them."
    echo "i.e. ./download_weights.sh [SCREW_DETECTION or SCREW_CLASSIFICATION] [path_to_target_dir]"
    exit
fi

target_dir=$2
if [ $1 == "SCREW_DETECTION" ]; then
    echo "Downloading weights for screw detector"
    file_id="1q50790KXuURFX1VvjW1Yln2L4APXWtom"
elif [ $1 == "SCREW_CLASSIFICATION" ]; then
    echo "Downloading weights for screw classifier"
    file_id="1H2zS9m7SMXWYhtSwZz_P1EePNXT51Hky"
else
    echo "Invalid first parameter: ("$1"). Must be SCREW_DETECTION or SCREW_CLASSIFICATION."
    exit
fi

mkdir -p $target_dir
cd $target_dir
gdown --id $file_id
