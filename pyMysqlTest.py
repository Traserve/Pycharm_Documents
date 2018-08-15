import pandas as pd
import pymysql

# mysql_cn= pymysql.connect(host='localhost', port=3306,user='wht_dev', passwd='wht_dev', db='wht_dev')
# df = pd.read_sql('select * from hap_demo_b;', con=mysql_cn)
# print(df)
# mysql_cn.close()


db = pymysql.connect(host='localhost', port=3306, user='wht_dev', passwd='wht_dev', db='wht_dev')
# df = pd.read_csv('D:\\PycharmProjects\\tips.csv')
cur = db.cursor()
sql = 'select * from hap_demo_b'
df = pd.read_sql(sql, db)
# index=False表示导出时去掉行名称，如果数据中含有中文，一般encoding指定为‘utf-8’
df.to_csv('D:\\PycharmProjects\\hapDemoB.csv', encoding='utf-8', index=False)
try:
    cur.execute(sql)
    results = cur.fetchall()
    for row in results:
        # print(row[0],' ',row[1],' ',row[2],' ',row[3],' ',row[4])
        print(row)
except Exception as e:
    raise e
finally:
    db.close()
