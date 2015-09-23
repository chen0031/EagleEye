#!/bin/sh
ip_address=$1
metric=$2
value=$3
#ssh root@$ip_address  printf "hhh"
ssh root@$ip_address  "echo $value > $metric" 
#ssh root@$ip_address  sync
#echo $2 > $1 
#sync 


