#!/bin/bash

# unused in this short course
rm -rf /var/lib/influxdb

# not necessary anymore
rm -rf /usr/src/*
rm /opt/spark-3.0.0-bin-hadoop2.7.tgz
/usr/bin/apt-get clean
/usr/bin/apt-get autoclean
rm -rf /srv/apps/*

# it's a development environment, we can clean older logs...
journalctl --vacuum-size=5M
rm /var/log/elasticsearch/gc.log.*

cd /opt/
wget https://artifacts.elastic.co/downloads/elasticsearch-hadoop/elasticsearch-hadoop-7.9.3.zip
unzip elasticsearch-hadoop-7.9.3.zip
cd /opt/elasticsearch-hadoop-7.9.3/dist
mv elasticsearch-spark-20_2.11-7.9.3.jar /opt/
mv elasticsearch-hadoop-7.9.3.jar /opt/

