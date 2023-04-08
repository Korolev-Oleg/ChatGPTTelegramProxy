#!/usr/bin/env sh
apk update && apk add openssh
adduser -D sshuser
echo 'sshuser:password' | chpasswd
mkdir /home/sshuser/.ssh
echo MaxAuthTries 666 >> /etc/ssh/sshd_config
ssh-keygen -A
/usr/sbin/sshd -D
