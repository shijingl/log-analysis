Descriptions
This program answers three questions using sql queries and python codes: 
1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top
2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

Preparation 
1. Vagrant/Virtual Box Set Up
This will be run on Vagrant/Virtual Box. If you have not install Vagrant/Virtual Box, please install. 
Install Vagrant: https://www.vagrantup.com
Install VirtualBox: https://www.virtualbox.org/wiki/Download_Old_Builds_5_1 
Download VM Configuration: https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip
Run vagrant up
Run vagrant ssh. If you can successfully log in, then you are good. 
2.  Download data, unzip it and then put newsdata.sql in your vagrant folder
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

Requirements 
1. Python 2.7.12 
https://www.python.org/download/releases/2.7/
2. psycopg2
3. Postgresql 9.6

How to run 
1. load the data onto the database
psql -d news -f newsdata.sql
2. connect to the database
psql -d news
3. python main.py
