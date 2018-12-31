Questions
1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top
2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

Requirements 
1. Python 2.7.12
2. psycopg2
3. Postgresql 9.6

How to run 
1. load the data onto the database
psql -d news -f newsdata.sql
2. connect to the database
psql -d news
3. python main.py
