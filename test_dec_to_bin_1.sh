#!/bin/bash
echo Deciman Number: $1

a=0; b=0; b0=0; b1=01; b2=0; b3=0; b4=0; b5=0; b6=0; b7=0;

a=$(($1/2)); b=$(($1%2)); b0=$b
echo $a $b $b0
 
a=$(($a/2)); b=$(($b%2)); b1=$b
echo $a $b $b1

a=$(($a/2)); b=$(($b%2)); b2=$b
echo $a $b $b2

