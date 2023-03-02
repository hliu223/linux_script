#!/usr/bin/env python3
#bckupVM.py
# Purpose: Backs up virtual machines
#
# USAGE: ./backupVM.py
#
# Date: Feb 5, 2023
import os
currentuser = os.popen('whoami').read().strip()
# get the result of "whoami"
if currentuser != 'root':
  print(f"You must be root, current user is {currentuser}" )
  exit()
#if the username is not root, exit
else:
  x = input('Do you wanna back up all VMs?(yes or no): ')
	#ask user if want to backup all vms
  if x == 'yes':#it will backup all VMs when get " yes"
    print('Backing up centos1')
    os.system('gzip < /var/lib/libvirt/images/centos1.qcow2 > ~hliu223/backups/centos1.qcow2.gz')
    print('Backing up centos2')
    os.system('gzip < /var/lib/libvirt/images/centos2.qcow2 > ~hliu223/backups/centos2.qcow2.gz')
    print('Backing up centos3')
    os.system('gzip < /var/lib/libvirt/images/centos3.qcow2 > ~hliu223/backups/centos3.qcow2.gz')
  elif x == 'no':#if user type "no", will inquire user enter the vm that wanna back up
    y = input('which VM you want to back up(centos1,centos2,centos3): ')
    if y == 'centos1':#get vm1's name, back up vm1
      print('Backing up centos1')
      os.system('gzip < /var/lib/libvirt/images/centos1.qcow2 > ~hliu223/backups/centos1.qcow2.gz')
    elif y == 'centos2':#get vm2's name, back up vm2
      print('Backing up centos2')
      os.system('gzip < /var/lib/libvirt/images/centos2.qcow2 > ~hliu223/backups/centos2.qcow2.gz')
    elif y == 'centos3':#get vm3's name, back up vm3
      print('Backing up centos3')
      os.system('gzip < /var/lib/libvirt/images/centos3.qcow2 > ~hliu223/backups/centos3.qcow2.gz')
    else:#when the user input cannot be idtified, print an error message.
      print('your input cannot be idtified')
      exit()
  else:
    print('This input cannot be identified')
    exit()
