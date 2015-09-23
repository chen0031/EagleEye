#!/bin/sh
#change the physical resource of the system implementing Hyperviser
domain_name=$1
metric_name=$2
metric_value=$3
if [ $2 eq "memory" ]
then
  virsh setmem $domain_name $metric_value 
elif [ $2 eq "cpu" ]
then
  virsh setvcpus $domain_name $metric_value   
fi   
