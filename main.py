#!/usr/bin/env python
import psycopg2

DB = "news"

answer_1 = '''select articles.title, count(*) as views from articles
 join log on log.path = concat('/article/', articles.slug)
 group by log.path, articles.title order by views desc limit 3;'''

answer_2 = '''select authors.name, count(*) as views from articles
join authors on authors.id=articles.author join
log on log.path = concat('/article/', articles.slug)
group by authors.name order by views desc;'''

answer_3 = '''select * from (select TO_CHAR(date, 'Mon DD, YYYY'),
ROUND (error * 100.0 / total, 2)
 as per from (select ERROR_TABLE.date, total, error
  from (select date(time) as date, count(*) as error from log
   where log.status like '%404%' group by date) as ERROR_TABLE join
    (select date(time) as date, count(*) as total from
    log group by date) as TOTAL_TABLE on ERROR_TABLE.date=TOTAL_TABLE.date)
    as final_table) as error where per >1.0;'''

if __name__ == '__main__':
    conn = psycopg2.connect(database=DB)
    curr = conn.cursor()
    curr.execute(answer_1)
    result = curr.fetchall()
    print 'Q1: What are the most popular three articles of all time?'
    for i in range(len(result)):
        print i+1, ':', result[i][0], '-', result[i][1], 'views'
    print '================================================================='

    curr.execute(answer_2)
    result = curr.fetchall()
    print 'Q2: Who are the most popular article authors of all time?'
    for i in range(len(result)):
        print i+1, ':', result[i][0], '-', result[i][1], 'views'
    print '================================================================='

    curr.execute(answer_3)
    result = curr.fetchall()
    print 'Q3: On which days did more than 1% of requests lead to errors?'
    for i in range(len(result)):
        print i+1, ':', result[i][0], '-', result[i][1], '% errors'
    print '================================================================='

    conn.close()
