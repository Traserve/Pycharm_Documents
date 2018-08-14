import pandas as pd
import MySQLdb
# data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv" #填写url读取
df = pd.read_csv('E:\\Pycharm_Documents\\tips.csv')
print(df)

mysql_cn= MySQLdb.connect(host='localhost', port=3306,user='myusername', passwd='mypassword', db='mydb')
df = pd.read_sql('select * from test;', con=mysql_cn)
mysql_cn.close()