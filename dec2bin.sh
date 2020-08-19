#!/bin/bash
echo " Convert decimal number to binary"
echo " Type your number " 
#n is number that will be converted
read n
#c represents devided number by 2, loop will work untill
# it's value is not equal to 0
array=()
index=0
c=$n
while [ $c -gt 0 ]; do
    d=$(($c%2))
    #echo $d
    array[$index]=$d
    #echo "${array[$index]}"
    c=$(($c/2))
    index=$index+1
done
b=$(echo "${array[*]}" | rev)
echo "Binary of $n is:" $b



