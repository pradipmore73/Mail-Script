#!/bin/bash
count=`df -h | grep -v Filesystem |sed 's/\%//g' | awk '{if($5>=80)print}' | wc -l`
echo $count
if [ count != 0 ]
then
./mail.sh    // Path for the script which sends mail 
else
echo "No Match with the pattern for $(hostname) as on $(date)"
fi
