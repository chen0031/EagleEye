#!/bin/sh 
netstat  | grep "tcp" > Connection.tmp
awk '{print $1 " " $4 " " $5 " " $6 " "}' Connection.tmp > Connection_1.tmp
rm -f Connection.tmp
host_ip=`awk '{print $1}' /hosts/host`
host_name=`awk '{print $2}' /hosts/host`
host_local_name=`awk '{print $3}' /hosts/host`
host_local_loop_ip=`awk '{print $4}' /hosts/host`
sed "s/$host_name/$host_ip/" Connection_1.tmp > Connection_2.tmp
sed "s/$host_local_name/$host_ip/g" Connection_2.tmp > Connection_3.tmp 
sed "s/$host_local_loop_ip/$host_ip/g" Connection_3.tmp > /EagleEye/service_dep/Connection.tmp
rm -f Connection_1.tmp Connection_2.tmp Connection_3.tmp
#iawk 'gsub(host_name,host_ip);gsub(host_local,host_ip){print $0}' Connection_1.tmp > Connection_2.tmp
