
/*
1. 查出至少有一个员工的部门。显示部门编号、部门名称、部门位置、部门人数。
*/
SELECT d1.deptno,d1.dname,d1.loc,COUNT(*)
FROM t_dept  d1 , t_employees  d2
WHERE d1.deptno = d2.deptno
GROUP BY deptno


/*
3. 列出所有员工的姓名及其直接上级的姓名。
*/
SELECT t1.ename,t2.ename
FROM t_employees t1 LEFT JOIN t_employees t2
ON t1.mgr = t2.empno




/*
4. 列出受雇日期早于直接上级的所有员工的编号、姓名、部门名称。
*/
SELECT t1.empno,t1.ename,t1.deptno
FROM t_employees t1 , t_employees t2
WHERE t1.mgr = t2.empno AND t1.hiredate < t2.hiredate





/*
5. 列出部门名称和这些部门的员工信息，同时列出那些没有员工的部门。
*/
SELECT t2.dname,t1.*
FROM t_employees t1 RIGHT JOIN t_dept t2
ON t1.deptno=t2.deptno




/*
7. 列出最低薪金大于15000的各种工作及从事此工作的员工人数。
*/
SELECT job, COUNT(*)
FROM t_employees 
GROUP BY job
HAVING MIN(sal) > 15000


/*
8. 列出在公关部工作的员工的姓名，假定不知道公关部的部门编号。
*/
SELECT *
FROM t_employees e
WHERE e.deptno=(SELECT deptno FROM t_dept WHERE dname='公关部')


/*
9. 列出薪金高于公司平均薪金的所有员工信息，所在部门名称，上级领导，工资等级。
*/



/*
10.列出与张飞从事相同工作的所有员工及部门名称。
*/
SELECT e.*, d.dname
FROM t_employees e, t_dept d
WHERE e.deptno=d.deptno AND job=(SELECT job FROM t_employees WHERE ename='张飞')


/*
11.列出薪金高于在部门30工作的所有员工的薪金的员工姓名和薪金、部门名称。
*/

SELECT e.ename, e.sal, d.dname
FROM t_employees e, t_dept d
WHERE e.deptno=d.deptno AND sal > ALL (SELECT sal FROM t_employees WHERE deptno=30)
