#!/bin/sh
#use a default interface file in /EagleEye/service_dep/InterfaceInfo.tmp
interfaceInfoFile=/EagleEye/service_dep/InterfaceInfo.tmp
shell_dir=/EagleEye/shell
#cmd_interfaceInfo_path=$shell_dir/InterfaceInfo.sh
networkIF=$1
$shell_dir/InterfaceInfo.sh $networkIF
if [ ! -s $interfaceInfoFile ]; then
 echo 'The InterfaceInfo.tmp does not exist!'
# echo $cmd_interfaceInfo_path
 $shell_dir/InterfaceInfo.sh $networkIF
fi  
#echo 'The InterfaceInfo.tmp has existed!'
$shell_dir/listProcByNetworkInterface.awk -v interface=$networkIF  $interfaceInfoFile> processName_1.tmp
sed -n '1p' processName_1.tmp > /EagleEye/service_dep/processName.tmp
rm -f processName_1.tmp

 



