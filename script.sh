#!/bin/bash
echo  Image name is $1
python imgup.py $1 > output.txt
value=`cat output.txt`  
echo $value  
python yandex.py $value
python tineye.py $value
python bing.py $value
python google.py $1
