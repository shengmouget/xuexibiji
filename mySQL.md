# 01 数据库概述

​	为什么使用数据库：持久化  关系型数据库

​	DBMS数据库管理系统	SQL 结构化语言

​	关系型数据库（RDBMS）  以row和column 的形式存储，二位表格形式 

​	优点：便于复杂数据查询  安全性很高 事务支持

​	列式数据库降低I/O

~~~ sql
ORM思想：
数据库中的一个表 --- java或python中的一个类
表中的一条数据 --- 类中的一个对象
表中的一个列 --- 类中的一个字段、属性
~~~

​	E-R模型 实体-联系 实体集 属性 联系表

​	自我引用关系

# 02 mysql环境搭建

# 03 基本select语句

SQL功能上主要分为三大类：

- DDL数据定义语言 CREATER/ALTER/DROP/RENAME/TRYNCATE(清空)
- DML数据操作语言 insert \ delete \ update \ select
- DCL数据控制语言 commit \ rollback(回滚) \ savepoint (具体回滚点)\ grant(权限回收)\revoke

### SQL语言的规则与规范

- SQL可以写在一行或多行

- 每条命令以分号 或者\G \g结束

- 关键字不能被缩写、分行

- 字符串、日期、时间的变量必须用“”

- 在windows下大小写不敏感

- 在Linux下大小写敏感

  - 数据库名、表名、表的别名、变量名是严格区分大小写的
  - 关键字、函数名、反正自定义的忽略大小写

  推荐使用统一：

  - 数据库名、表名、表别名、字段名、字段别名都小写
  - SQL关键字、函数名、绑定变量名都大写

- 注释：

  ~~~ sql
  单行注释：# #
  单行注释：-- 
  多行注释：/*文字*/
  ~~~

### 导入现有的数据表、表的数据

- source 文件的全路径名
- 基于具体的图形化界面可以导入数据

### SELECT基本语法

​	表中字段

> SELECT 字段1 ,字段2...FROM 表名

​	列的别名

​			as:可以省略

​			列的别名可以使用一对“”引起来

>SELECT employess_id emp_id , last_name AS lname ,department_id "部门" FROM employess   

​	去除重复行

>SELECT DISTINCT department_id FROM employess  

​	空值参与运算 结果一定也是空  null不等同于0

>SELECT employee_id,salary '月工资',salary * (1 + commission_pct) * 12 '年工资',commission_pct
>FROM employees

​	着重号 ``

>SELECT * FROM `order`;

​	查询常数给每一行都给一个匹配

>SELECT '尚硅谷',employee_id,last_name FROM employees;

​	显示表结构 显示表中字段的详细信息

>DESCRIBE employees;  或者DESC

####  过滤数据 (where)

> SELECT * FROM employees *WHERE* department_id = 90;

# 04 运算符

### 算术运算符

~~~sql
+ - * / div % mod
浮点数参与运算 结果为浮点型
在sql中 + 没有连接的作用，就表示加法运算。此时会将字符串转换为数值（隐式转换）
SELECT 100 + '1'
FROM DUAL（伪表）  结果为101
SELECT 100 + 'a'   此时将a看作0处理
FROM DUAL  结果为100
NULL值参与运算结果为null
-------------------------------------------------------------------
SELECT 12%3,12%5,12MOD-5
FROM DUAL
~~~

### 比较运算符

~~~sql
结果为真返回1，结果为假返回0，其他情况返回null
SELECT 0='1',0='a'
FROM DUAL  结果为0 和 1
两边都是字符串的时候，按照ANSI的比较规则进行比较
只要有null参与比较，结果为null
-------------------
SELECT last_name,salary,commission_pct
FROM employees
WHERE commission_pct = NULL  #只有结果为1才能查询出来
---------------------------------------
安全等于 <=> 主要是针对null
两边操作数为null 返回 1 
1 <=> null 返回 0
SELECT last_name,salary,commission_pct
FROM employees
WHERE commission_pct <=> NULL  可以查询出来
------------------------------------------------
<> 不等于 !=
~~~

#### 具体关键字

~~~sql
# IS NULL \ IS NOT NULL \ISNULL
SELECT last_name,salary,commission_pct
FROM employees
WHERE  ISNULL(commission_pct) 
# LEAST(value1,value2,...)(最小) / GREATEST(value1,value2,...)（最大）
SELECT LEAST(first_name,last_name)
FROM employees
# BETWEEN ...AND
SELECT employee_id,last_name,salary
FROM employees
WHERE salary BETWEEN 6000 AND 8000   #包含6000和8000
# IN / NOT IN 集合
SELECT last_name,salary,department_id
FROM employees
WHERE department_id IN (10,20,30)
# %模糊查询
# 查询last_name 中包含‘a’的员工信息
# %代表不确定个数的字符
SELECT last_name
FROM employees
WHERE last_name LIKE '%a%'
# 查询last_name 中以‘a’开头的员工信息
SELECT last_name
FROM employees
WHERE last_name LIKE 'a%'
# -代表一个不确定字符
# 第二个字符为'a'的员工信息
SELECT last_name
FROM employees
WHERE last_name LIKE '_a%'
# 查询第二个字符是_且第三个字符是‘a’的员工信息
# 需要使用转义字符  ESCAPE 定义转义字符
SELECT last_name
FROM employees
WHERE last_name LIKE '_\_a%'
# 或者
WHERE last_name LIKE '_$_a%' ESCAPE '$' 
# 正则表达式 REGEXP / RLIKE
SELECT 'shkstaart' RLIKE '^shk'
~~~

### 逻辑运算符

>NOT 或 ！
>
>AND 或 &&
>
>OR 或 ｜｜
>
>XOR 异或   不同 一真一假   AND优先级高于OR

#  05 排序与分页

### 排序

~~~ sql
# 按照salary 从高到低的顺序显示员工信息
# 使用 ORDER BY 对查询到的数据进行排序操作 默认升序
# 升序 ASC(ascend)
# 降序 DESC（descend）
SELECT employee_id,last_name,salary
FROM employees
ORDER BY salary DESC
# 二级排序 显示员工信息 按照 departmentent_id降序排列
SELECT employee_id,salary,department_id
FROM employees
ORDER BY department_id DESC,salary 
# 每页显示pageSize条记录 此时显示pageNo页
# 公示 LIMIT （pageNo - 1）* pageSize,pageSize;
~~~

⚠️ 列的别名只能在order By 中使用 不能在where中使用

⚠️ where需要声明在from之后，order by之前

⚠️ WHERE ORDER BY LIMIT 声明顺序如下：

~~~ sql
# LIMIT的格式：严格来说 LIMIT 位置偏移量 条目数
# 结构  LIMIT	0，条目数 等价于   LIMIT 条目数
SELECT employee_id,last_name,salary
FROM employees
WHERE salary > 6000
ORDER BY salary DESC
LIMIT 10;
~~~

😊 mysql8.0新特性 LIMIT 记录数 OFFSET 偏移量

>SELECT employee_id,last_name
>FROM employees
>LIMIT 2 OFFSET 31 

# 06 多表查询

~~~ sql
# 多表查询，必须有连接条件
SELECT employee_id '员工ID',department_name
FROM employees,departments
# 多表连接条件
WHERE employees.department_id = departments.department_id
~~~

⚠️

> 如果查询语句中存在多个表中都存在的字段，必须指明字段所在表
> 从sql优化的角度，建议多表查询时，每个字段前都指明其所在的表

~~~sql
# 可以给表起别名 像 SELECT和where中使用表的别名
# 如果起了别名，一定要在表中使用别名，不能使用别名
SELECT emp.employee_id '员工ID',dept.department_name
FROM employees emp,departments dept
# 多表连接条件
WHERE emp.department_id = dept.department_id
~~~

### 多表查询的分类

#### 角度一 等值连接 vs 非等值连接

~~~ sql
# 非等值连接
SELECT last_name,salary,grade_level
FROM employees e,job_grades j
WHERE e.salary BETWEEN j.lowest_sal AND j.highest_sal
ORDER BY j.grade_level DESC
~~~

#### 角度二 自连接 vs 非自连接

~~~sql
# 查询员工id，员工姓名及其管理者id和姓名 自连接 单表操作
SELECT emp.employee_id,emp.last_name,mgr.employee_id,mgr.last_name
FROM employees emp,employees mgr
WHERE emp.employee_id = mgr.manager_id
~~~

#### 角度三 内连接 vs 外连接

SQL99版本 join...on 实现内外连接

~~~sql
# SQL99语法实现内连接
SELECT last_name,department_name
FROM employees e JOIN departments d
ON e.department_id = d.department_id
----------------
#添加多个表
SELECT last_name,department_name,city
FROM employees e JOIN departments d
ON e.department_id = d.department_id
JOIN locations l
ON d.location_id = l.location_id
~~~

#### 左外连接  left out  join

~~~sql
SELECT last_name,department_name
FROM employees e LEFT JOIN departments d
ON e.department_id = d.department_id
~~~

#### 右外连接  right out  join

~~~ sql
SELECT last_name,department_name
FROM employees e RIGHT JOIN departments d
ON e.department_id = d.department_id
~~~

#### 满外连接

~~~sql
SELECT last_name,department_name
FROM employees e LEFT JOIN departments d
ON e.department_id = d.department_id
WHERE e.department_id is NULL
UNION ALL
SELECT last_name,department_name
FROM employees e RIGHT JOIN departments d
ON e.department_id = d.department_id
~~~



#### union操作

union 去重

union all  不会执行去重的操作

结论： 如果明确知道合并数据后的结果数据不存在重复数据，或者不需要去重的数据 则尽量使用union ALL语句 提高查询效率

#### 7种SQL JOINS的实现

![image-20221112192450414](/Users/mac/Library/Application Support/typora-user-images/image-20221112192450414.png)

#### 自然连接

NATURAL 会自动查询两张表中的相同字段 然后进行等值连接。不够灵活

#### USING使用

当两个表中字段名字一样的时候，可以用using 不适用于自连接

# 07 单行函数

流程控制函数

~~~sql
### if
SELECT last_name,salary, # 记得逗号
IF(salary >=6000,'高工资','低工资')
FROM employees
# IFNULL(expr1,expr2) 如果不为null 返回第一个值 
#  CASE WHEN .... THEN...WHEN...THEN...ELSE..END
SELECT last_name,salary,
CASE WHEN salary >= 15000 THEN '白骨精'
WHEN salary >= 10000 THEN '潜力股'
WHEN salary >= 8000 THEN '小屌丝'
ELSE '草根' END 'deyails'
FROM employees
~~~

#### Mysql加密与解密函数

加密和解密函数主要用于对数据库中的数据进行加密和解密处理，以防止数据被他人窃取 

>password（） 加密结果不可逆
>
>MD5（） 返回字符串str的md5加密后的值，也是一种加密方式 若参数为null 则会返回null
>
>SHA（） 比md5更安全

# 08 聚合函数

~~~sql
# 3.COUNT 作用：计算指定字段在查询结果中出现的个数
SELECT COUNT(employee_id),COUNT(salary = 3000),COUNT(1)
FROM employees
# 如果计算表格中有多少条记录，如何实现
# 方式一 count(*)
# 方式二 count(1)
如果需要统计表中的字段数
~~~

#### group by 分组

~~~sql
#GROUP BY 分组
# SELECT中出现的非组函数的字段 必须声明在GROUP BY中 反之 GROUP BY 中声明的字段可以不出现在 SELECT中
#需求 查询各个部门的平均工资 最高工资
SELECT department_id,AVG(salary)
FROM employees
GROUP BY department_id
#需求 查询各个job_id的平均工资
SELECT job_id,AVG(salary)
FROM employees
GROUP BY job_id
# 需求 查询各个department_id,job_id的平均工资
SELECT department_id,job_id,AVG(salary)
FROM employees
GROUP BY department_id,job_id
~~~

~~~sql
# SELECT中出现的非组函数的字段 必须声明在GROUP BY中 反之 GROUP BY 中声明的字段可以不出现在 SELECT中
# Mysql中 GROUP BY中使用 WITH ROLLUP 计算总体工资 与 ORDER BY慎用
SELECT department_id,AVG(salary)
FROM employees
GROUP BY department_id WITH ROLLUP
~~~

#### HAVING

~~~sql
# HAVING 的使用（作用：用来过滤数据的）
# 如果过滤条件中使用了聚合函数 则必须使用having来替换where。否则报错
# 要求 having必须声明在GROUP BY的后面
# 开发中，我们使用having前提是sql中使用了 GROUP BY
SELECT department_id,MAX(salary) 'salary'
FROM employees
GROUP BY department_id
HAVING MAX(salary) > 10000
# 当过滤条件中 有聚合函数时 则此过滤条件必须声明在having中
# 当过滤条件中 没有聚合函数时 则此过滤条件声明在where中或having中都可以，但是，建议在where中
~~~

#### having 和 where对比

从使用范围来看，having更广

如果过滤条件没有， where的效率会跟高

# 09 子查询

