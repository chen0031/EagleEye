#!/bin/sh
ip_address=$1
ssh root@$ip_address  "echo 3 > /proc/sys/vm/drop_caches"
