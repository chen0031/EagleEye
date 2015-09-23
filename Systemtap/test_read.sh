#!/bin/sh
cat collection.conf | while read line
do
 indicator= `awk '{print $1}' $line`
  
 if [  ]
 then 
  continue
 else
  echo $line
 fi

done 
