#!/bin/sh

echo -e "Enter value"
read var

if [ $var -gt 30 ]; then
	sysctl -n machdep.cpu.brand_string
else 
	echo "Value is less than 30"
fi 