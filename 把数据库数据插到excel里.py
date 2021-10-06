import xlwt
import pymysql
host="localhost"
user="root"
password=""
database = "company"
def select(sql,param,mode="all",size=1):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql, param)

    if mode == "all":
        return cursor.fetchall()
    elif mode == "one":
        return cursor.fetchone()
    elif mode == "many":
        return cursor.fetchmany(size)
    con.commit()
    cursor.close()
    con.close()

company=xlwt.Workbook()
t_dept=company.add_sheet('t_dept', cell_overwrite_ok=True)
t_employees=company.add_sheet('t_employees', cell_overwrite_ok=True)
for i in range(4):
    for j in range (3):
        sal='select * from t_dept'
        param=[]
        rows=select(sal,param)
        print(type(rows))
        print(rows)
        t_dept.write(i,j,rows[i][j])
for k in range(15):
    for l in range(8):
        sal1='select * from t_employees'
        param1=[]
        rows=select(sal1,param1)
        t_employees.write(k,l,rows[k][l])
company.save('company.xls')







