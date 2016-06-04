#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H:%M:%S")
raspistill -t 3000 -br 65 -o /home/pi/Desktop/web_view/picture/$DATE.jpg
