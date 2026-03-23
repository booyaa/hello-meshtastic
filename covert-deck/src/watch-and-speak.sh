#!/bin/bash

while inotifywait -e close_write foo.txt
do 
	espeak-ng -f foo.txt
done
