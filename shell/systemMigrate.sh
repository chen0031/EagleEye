#!/bin/shell
source_domain_name=$1
destination_ip=$2
virsh migrate $source_domain_name $destination_ip
