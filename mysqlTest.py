from pymysql import *
# 创建数据库链接
conn = connect(host='192.168.226.129',user='root',password='111111',
               database = 'pythonDB',charset = 'utf8')
# 创建一个游标对象，可以利用这游标对象进行数据库的操作
try:
    cur =conn.cursor()
    # 用游标去执行命令行。
    cur.execute('select * from student')
    # 查询所有数据并返回保存在result中
    result = cur.fetchall()
    # for循环遍历result，result是一个元祖形式的数据
    for iterm in result:
        print(f"姓名是:{iterm[1]},住址是:{iterm[3]}")
    # print(result)
    print('sucess')
    # 把游标关闭
    # cur.close()
    # 把数据库连接关闭，否则会占用资源
    # conn.close()
except Exception as ex:
    print(ex)
finally:
    cur.close()
    conn.close()



