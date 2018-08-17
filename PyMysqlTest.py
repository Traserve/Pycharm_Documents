import pandas as pd
import pymysql

# Python连接Mysql数据库操作
# https://blog.csdn.net/qq_37176126/article/details/72824106

# mysql_cn= pymysql.connect(host='localhost', port=3306,user='wht_dev', passwd='wht_dev', db='wht_dev')
# df = pd.read_sql('select * from hap_demo_b;', con=mysql_cn)
# print(df)
# mysql_cn.close()

# 打开数据库连接
db = pymysql.connect(host='localhost', port=3306, user='wht_dev', passwd='wht_dev', db='wht_dev')
# 使用cursor()方法获取操作游标
cur = db.cursor()
sql = 'select * from hap_demo_b'
df = pd.read_sql(sql, db)
# 导出数据到cvs表格
# index=False表示导出时去掉行名称，如果数据中含有中文，一般encoding指定为'gb18030','utf-8'测试无效，因该是Excel只识别gb编码
# 日期数据导出后在Excel表格中显示为####是因为列宽太窄，增加列宽之后正常显示
df.to_csv('D:\\PycharmProjects\\hapDemoB.csv', encoding='gb18030', index=False)
try:
    # 执行sql语句
    cur.execute(sql)
    # 获取查询的所有记录
    results = cur.fetchall()
    # 遍历结果
    for row in results:
        # print(row[0],' ',row[1],' ',row[2],' ',row[3],' ',row[4])
        print(row)
except Exception as e:
    raise e
finally:
    db.close()