#!/bin/bash

SEC="$(($RANDOM% 10+5))"
RND="$(($RANDOM% 5+25))"

TIME=`date +"%Y-%m-%d_%H:%M:%S"`
StartTime=$(date +%s)

EXE='/opt/anaconda3/envs/crawling/bin/python'
DIR="/Users/username/Crawling/facebook_click_like/"
LOG="/Users/username/Crawling/logs/"

echo -e "START:"$TIME >> $LOG"facebook_click_like.log"
echo -e $DIR >> $LOG"facebook_click_like.log"
echo "random:"$RND >> $LOG"facebook_click_like.log"

#source activate crawling

echo -e "\n"$SEC"\n" >> $LOG"facebook_click_like.log"
sleep $SEC

OUTPUT=$(${EXE} ${DIR}execute.py $RND)
echo -e "\n"$OUTPUT"\n" >> $LOG"facebook_click_like.log"

echo -e "END:"$TIME >> $LOG"facebook_click_like.log"

EndTime=$(date +%s)
echo "It takes $(($EndTime - $StartTime)) seconds to complete this task." >> $LOG"facebook_click_like.log"