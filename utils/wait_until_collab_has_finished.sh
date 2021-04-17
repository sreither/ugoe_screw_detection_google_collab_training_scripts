#!/bin/bash

target_dir="/tmp/"

if [ ! $# -eq 1 ]; then
    echo "Please specifiy for which training should be waited. [SCREW_DETECTION or SCREW_CLASSIFICATION]"
    exit
fi

if [ $1 == "SCREW_DETECTION" ]; then
    echo "Waiting for training of screw detector"
    train_info_file_id="1u6Ub-nVtMoAaiMMEQ0-00DDQfqDqay3O"
elif [ $1 == "SCREW_CLASSIFICATION" ]; then
    echo "Waiting for training of screw classifier"
    train_info_file_id="1ZTduhE9fADxAZDF3hXMEJg-z8CqFktUW"
else
    echo "Invalid first parameter: ("$1"). Must be SCREW_DETECTION or SCREW_CLASSIFICATION."
    exit
fi


# Get curent time in seconds since epoch
script_start_time=$(date +%s)
echo "Script start: " $script_start_time

check_train_info_file() {
    gdown --id $train_info_file_id -O $target_dir > /dev/null 2>&1

    start_time=0
    end_time=0
    counter=0
    while read -r line ; do
        if [ $counter -eq 0 ]; then
            start_time=$line
        elif [ $counter -eq 1 ]; then
            end_time=$line
        else
            echo "file has too many lines"
        fi
        let counter=$counter+1
    done < $target_dir"/train_info.txt"

    if (( $(echo "$start_time > $script_start_time && $end_time > $start_time" |bc -l ) )); then
        echo "Finished"
    else
        echo "Training..."
    fi

}

while
    sleep 1
    finished=$(check_train_info_file)
    echo $finished
    [ ! $finished == "Finished" ]
do true; done

echo "Done"
