#!/usr/bin/env python3
# vmbackup.py
# Purpose: Backs up virtual machines using tar
#
# USAGE: ./vmbackup.py
#
# Author: Honglin Liu
# Date: Feb 20, 2023
import os
import datetime
switch = True
print("Here are the list of the names of all VMs on current machine:")
os.system("sudo virsh list --name --all")
  #show all the VMs' name in this machine
listOfVMs = os.popen("sudo virsh list --name --all").read().splitlines()
  #put all the VMs' name in a list
for VMs in listOfVMs:
  if VMs == '':
    listOfVMs.remove(VMs);
  #remove the element has nothing but '' in this list
while switch == True:
  #put a while loop here to parepare to ask user to reenter
  VMbackup = input("Enter the VM you wanna backup:")  
  if VMbackup not in listOfVMs:
    print("The VM name doesn't exist in current system, please reenter it.")
     # error message
  else:
    os.system(f"sudo virsh dumpxml {VMbackup} > {VMbackup}.xml")
    #create a xml file on current directory
    xmlpath = f"{VMbackup}.xml"
    #get xml file path
    imageFilePath = os.popen(f"cat {xmlpath} | grep source | grep file | awk -F \"'\" '{{print $2}}'").read().strip()
     #get the image file path from xml file, and it was sorounding by something we don't need, so use awk to cut it and pick the second part, it is what we want.
    datetime = str((datetime.date.today())).replace("-","")
     #use the function and store it in a variable as a name that we are going to use for the .tar file
    backupName = str(VMbackup)+'-'+str(datetime)
    print("creating archive file, it may take over 20 mins")
    os.system(f"sudo tar -cJvf {backupName}.tar.xz {imageFilePath} {xmlpath}")
     # create an archive file with image file and xml file at the same time by this command, and compress it using xzip
    print("complete!")
    switch = False
      #jump out of this while loop












