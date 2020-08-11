#!/bin/bash

NAME[0]="Zara"
NAME[1]="James"
NAME[2]="Kate"
NAME[3]="Mohalalasa"

echo "First Index: ${NAME[0]}"
echo "Second Index: ${NAME[1]}"

echo "First Method: ${NAME[*]}"
echo "Second Method: ${NAME[@]}"
