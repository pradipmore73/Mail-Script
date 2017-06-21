#!/bin/bash
count=`df -h | grep -v Filesystem |sed 's/\%//g' | awk '{if($5>=80)print}' | wc -l`
echo $count
if [ count != 0 ]
then
./mail.sh | telnet 10.20.30.40 25   // Path for the script which sends mail  | ip or FQDN of SMTP Server and SMTP Port (default port is 25)
else
echo "No Match with the pattern for $(hostname) as on $(date)"
fi
