#!/bin/awk  -f
BEGIN{
localVar=interface;
}
{
  split($2,address_sub_str,"->");
  if (address_sub_str[1] != "")
   { 
    split(address_sub_str[1],source_address_sub_str,":");
    if (source_address_sub_str[2]==localVar)
      {
       print $1;
      }
   }  
  
}
END{

}

