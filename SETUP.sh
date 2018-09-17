#!/bin/bash

echo "Hello! Please enter your name, so we know where to put your files (no spaces)."
echo "Dont use the ones below"
ls /home/pi/code
echo "please enter your name"
read -p "name: " -e studentName

mkdir -p /home/pi/code/${studentName}
cp -r deep3 /home/pi/code/${studentName}/deep3

cp -r completeExamples /home/pi/code/${studentName}/example

touch /home/pi/code/${studentName}/Write_Your_Code_In_This_Folder
touch /home/pi/code/${studentName}/lesson.py

#Copy in pre canned minecraft world (may fail if using diffrent pirmary system user)
cp -r deep3/lessonWorld /home/pi/.minecraft/games/com.mojang/minecraftWorlds/lessonWorld

echo " You are now ready to start coding!"
echo "make your files inside the /home/pi/code/${studentName} folder"

nohup /usr/bin/thonny %F /home/pi/code/${studentName}/lesson.py &
cd /opt/minecraft-pi/
nohup minecraft-pi &

cd /home/pi/code/${studentName}/deep3
n=0
until [$n -ge 100]
do
	pwd
        ls 
        python3 util.py && break
	n=$[$n+1]
	sleep 5
done

cd /home/pi/code/${studentName}


