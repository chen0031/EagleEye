#!/bin/sh
localVar=$1
lsof -i:$localVar > InterfaceInfo_1.tmp
sed '1d' InterfaceInfo_1.tmp > InterfaceInfo_2.tmp
awk '{ if ($10=="(ESTABLISHED)") print $1 " " $9 }' InterfaceInfo_2.tmp > /EagleEye/service_dep/InterfaceInfo.tmp
rm -f InterfaceInfo_1.tmp InterfaceInfo_2.tmp 

