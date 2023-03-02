#!/usr/bin/env python3
# tarchiver.py
# Purpose: Creates a tar archive of a directory
#
# USAGE: ./tarchiver.py
#
# Author: Honglin Liu
# Date: Feb 14, 2023
import os
loopSwitch1 = 1
loopSwitch2 = 1
#set 2 varables for the coming while loop 
directory = input("Enter the directory you wish to archive: ")
#get directory path
name = input("Enter the name you want to give the archive: ")
#get the name we want
while loopSwitch1 == 1:
#while loop, if everything goes right, jump out of it, otherwise reload this section
 ifCompress = input("Do you want the archive to be compressed?(yes or no): ")
 #get if user want compress
 if ifCompress == "yes":
  while loopSwitch2 == 1:
  #another while loop has the same intention with the last while loop
   compressionType = input("What type of compression do you want to apply? (gzip/bzip2/xz): ")
   if compressionType == "gzip":
   #gzip use z with cvf
    compression = "z"
    os.system(f"tar -zcvf {name}.tar.{compressionType} {directory}")
    loopSwitch2 = 2
   elif compressionType  == "bzip2":
   #bzip2 use j with cvf
    compression = "j"
    os.system(f"tar -jcvf {name}.tar.{compressionType} {directory}")
    loopSwitch2 = 2
   elif compressionType == "xz":
   #xz use J with cvf
    compression = "J"
    os.system(f"tar -Jcvf {name}.tar.{compressionType} {directory}")
    loopSwitch2 = 2
   else:
    print("Please reinput your option")
   #if the input doesn't work, reload the while loop
   loopSwitch1 = 2
 elif ifCompress == "no":
  os.system(f"tar -cvf {name}.tar {directory}")
  loopSwitch1 = 2
  #if no need to compress,use this command
 else:
  print("Please reinput the option")
  #response the other answer from yes or no


