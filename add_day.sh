#!/bin/bash

if [ $1 -lt 10 ]; then
	day="day0$1"
else
	day="day$1"
fi

mkdir $day
touch "$day/example"
touch "$day/input"
touch "$day/solution.py"
