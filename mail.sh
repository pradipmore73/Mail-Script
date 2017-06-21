#!/bin/bash
echo "EHLO hostname"
sleep 1
echo "MAIL FROM: abc@xyz.com"
sleep 1
echo "RCPT TO: john@domain.com"
sleep 1
echo 'DATA'
echo "To: abc@xyz.com"
echo "From: john@domain.com"
echo "Subject: File System full on $(hostname)"
echo ""

df -h | grep -v Filesystem |sed 's/\%//g' | awk '{if($5>=80)print "Running out of space "$6" ["$5"%] on '$(hostname)' as on '$( date +"%d-%m-%Y")'\n"}'

echo "From"
echo "Sys Admin"
echo ""
echo ""
echo "."
echo 'QUIT'
