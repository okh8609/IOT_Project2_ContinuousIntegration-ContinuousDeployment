#!/bin/bash

curl https://khaos.tw/hosts > ip.txt
cat ip.txt

echo "[server]" > inventory

while IFS=" " read -r host _ port 
do
	echo "$host ansible_port=$port anisible_user=root" >> inventory  
done < ip.txt

echo "[server:vars]" >> inventory
echo "file_path=/home/kh/iot_project2_CI/rpi/" >> inventory # the path to working directory

while read line; do
	ssh-copy-id $line
done < ip.txt

ansible-playbook -i inventory  playbook.yml
