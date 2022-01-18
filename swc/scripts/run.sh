#!/bin/bash
# copy scripts and src to home
if [ ! -d "/home/swc/scripts" ]
then
  cp -r /opt/swc/scripts /home/swc/scripts
fi
if [ ! -d "/home/swc/src" ]
then
  cp -r /opt/swc/src /home/swc/src
fi

# clear directories
rm -rf /home/swc/src/swc/conf

ln -s /home/swc/conf /home/swc/src/swc/conf

/usr/bin/supervisord -c /home/swc/conf/supervisord.conf