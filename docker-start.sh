#! /bin/bash

cd /output

mkdir -p /data

openssl enc -aes-256-cbc -iter 1 -d -in /code/toy_dataset_new.csv.enc -out /data/toy_dataset_new.csv -k toy_dataset_new.csv

python -m dssg_disinfo

rm /data/toy_dataset_new.csv