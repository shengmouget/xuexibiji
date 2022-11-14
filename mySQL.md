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

​	将一个查询嵌套在另一个查询语句内部的查询

​	子查询大大增强了select查询的能力

~~~sql
# 查询谁的工资比Abel高 自连接
SELECT e2.last_name,e2.salary
FROM employees e1,employees e2
WHERE e1.last_name = 'Abel'
AND e1.salary < e2.salary
# 方式二 子查询
SELECT last_name ,salary
FROM employees
WHERE salary > (
							SELECT salary
							FROM employees
							WHERE last_name = 'Abel'
);
~~~

#### 称谓的规范：外查询（主查询）、内查询（子查询）

- 子查询在主查询之前一次完成
- 子查询的结果是被主查询使用的
- 子查询要包含在括号内
- 将子查询放在主查询的右侧
- 单行操作符对应单行子查询，多行操作符对应多行子查询

#### 子查询的分类

- 单行子查询 vs 多行查询
- 相关子查询 vs 不相关子查询
  - 内查询是否被执行多次

#### 单行子查询

~~~sql
# 单行子查询
# 单行比较操作符 = > >= <= <>
# 查询工资大于149号员工工资的员工信息
# 子查询编写步骤：从里往外写  从外往里写
SELECT last_name ,salary
FROM employees
WHERE salary > (
					SELECT salary
					FROM employees
					WHERE employee_id = 149
)

SELECT MIN(salary)
FROM employees

# 查询最低工资大于50号部门最低工资的部门id和其他最低工资
SELECT department_id,MIN(salary)
FROM employees
WHERE department_id is NOT NULL
GROUP BY department_id
HAVING MIN(salary) > (
				SELECT MIN(salary)
				FROM employees
				WHERE department_id = 50
)
~~~

#### 多行子查询

多行比较操作符：

- IN 等于列表中的任意一个

- ~~~sql
  SELECT employee_id,last_name,salary
  FROM employees
  WHERE salary IN (SELECT MIN(salary) FROM employees GROUP BY department_id)
  ~~~

- ANY 需要和单行比较操作符一起使用，和子查询返回的某一个值比较

- ALL需要和单行比较操作符一起使用，和子查询返回的所有值比较

- ⚠️null问题

  ~~~sql
  # 返回其他job_id中比job_id为‘IT_PROG’部门任一工资低的员工的员工号、姓名、job_id以及salary
  SELECT employee_id,last_name,job_id,salary
  FROM employees
  WHERE job_id <> 'IT_PROG'
  AND salary < ANY (
  			SELECT salary
  			FROM employees
  			WHERE job_id = 'IT_PROG'
  )
  
  # 返回其他job_id中比job_id为‘IT_PROG’部门所有工资低的员工的员工号、姓名、job_id以及salary
  SELECT employee_id,last_name,job_id,salary
  FROM employees
  WHERE job_id <> 'IT_PROG'
  AND salary < ALL (
  			SELECT salary
  			FROM employees
  			WHERE job_id = 'IT_PROG'
  )
  # 查出平均工资最低的部门
  SELECT department_id
  FROM employees
  GROUP BY department_id
  HAVING AVG(salary) = (
  SELECT MIN(avg_salary)
  FROM(
  				SELECT department_id,AVG(salary) avg_salary
  				FROM employees
  				GROUP BY department_id
  ) t_type_avg_sla
  )
  ~~~

- SOME 实际上是ANY的别名，作用相同，一般常使用ANY

#### 相关子查询

每执行一次外表查询  子查询都要重新计算一次

~~~sql
# 相关子查询
# 查询员工中工资大于本部门平均工资的员工的last_name,salary,department_id
SELECT last_name,salary,department_id
FROM employees e1
WHERE salary > (SELECT AVG(salary) FROM employees e2 WHERE department_id = e1.department_id)
~~~

#### EXISTS 和 NOT EXISTS

~~~sql
# 检查是否存在满足条件的行
SELECT employee_id,last_name,job_id,department_id
FROM employees e1
WHERE EXISTS (SELECT * FROM employees e2 WHERE e1.employee_id = e2.manager_id)
~~~

# 10 创建和管理表

数据存储是处理数据的第一步 

​	创建数据库 --> 确认字段 --> 创建数据表 --> 插入数据

Mysql数据库系统从大到小数据库服务器、数据库、数据表、数据表的行与列

- 创建数据库

  ~~~sql
  # 方式一 使用的是默认字符集
  CREATE DATABASE mytest1  
  SHOW DATABASES
  
  # 方式二 显式指明了要创建
  CREATE DATABASE mytest2 CHARACTER SET 'gbk'
  
  #	方式三 如果要创建的数据库已经存在 则创建不成功 但不会报错 若不存在 则创建成功
  CREATE DATABASE IF NOT EXISTS mytest2 CHARACTER SET 'gbk'
  ~~~

- 管理数据库

  ~~~sql
  # 查看当前连接中的数据库有哪些
  SHOW DATABASES
  
  #切换数据库
  USE mytest1
  
  # 查看当前数据库中保存的数据表
  SHOW TABLES
  
  # 查看当前使用的数据库
  SELECT DATABASE() FROM DUAL
  
  # 查看指定数据库下保存的数据表
  SHOW TABLES FROM mysql
  ~~~

- 修改数据库

  ~~~sql
  # 修改数据库
  SHOW CREATE DATABASE mytest2
  # 修改数据库的编码格式
  ALTER DATABASE mytest2 CHARACTER SET 'gbk'
  ~~~

- 删除数据库

  ~~~sql
  # 方式一
  DROP DATABASE mytest1
  # 方式二 如果数据库存在 则删除成功
  DROP DATABASE IS EXISTS mytest1
  ~~~

- 修改表操作

  ~~~sql
  # 修改表 ALTER TABLE
  ## 添加一个字段
  ALTER TABLE myemp1
  ADD salary DOUBLE(10,2)  # 默认添加到表的最后一个字段
  ## 修改一个字段：数据类型、长度、默认值
  ALTER TABLE myemp1
  MODIFY emp_name VARCHAR(35) DEFAULT 'aaa' # 默认值
  ## 重命名一个字段
  ALTER TABLE myemp1
  CHANGE salary mothly_salary DOUBLE(10,2)
  ## 删除一个字段
  ALTER TABLE myemp1
  DROP COLUMN my_email
  # 重命名表
  RENAME TABLE myemp1
  TO myemp2
  # 删除表
  DROP TABLE IF EXISTS myemp2
  # 清空表
  TRUNCATE TABLE employess_copy
  ~~~

  # 11  数据处理之增删改

  - 添加数据

    ~~~sql
    # 方式一
    INSERT INTO emp1
    VALUES(1,'Tom','2000-12-21',2400)  # 注意 一定要按照声明的字段的先后顺序去添加
    # 方式二
    INSERT INTO emp1(id,hire_data,salary,`name`)
    VALUE(2,'1999-09-09',4000,'jerry')
    ~~~

  - 同时插入多条数据

    ~~~sql
    INSERT INTO emp1
    VALUES
    (1,'Tom','2000-12-21',2400),
    (2,'1999-09-09',4000,'jerry');
    ~~~

  - 更新数据UPDATE ... SET ... WHERE

    ~~~sql
    # 可以实现批量修改数据的
    UPDATE emp1
    SET hire_date = curdate()
    WHERE id = 5;
    ~~~

  - 删除DELETE FROM ... WHERE

    ~~~sql
    DELETE FROM emp1
    WHERE id = 1
    ~~~

# 12 MySQL数据类型精讲

int zerofill 

显示宽度为5，当insert的值不足5位时，使用0填充

unsigned函数

由于DECIMAL数据类型是精准的，在我们的项目中，除了极少数（商品编号）用到整数类型外，其他的都用DECIMAL，原因是 零售行业精度要求很高。

位类型：BIT 类型中存储的是二进制值

#### 日期和时间类型

- YEAR 表示年  1个字节
- DATE 年月日  3
- TIME 时分秒  3
- DATETIME  年月日时分秒  8
- TIMESTAMP  带时区的年月日时分秒 4

#### 文本字符串类型

- char  固定长度 默认一个字符。右侧拿空格填充
- varchar 可变长度

#### mysql中提取json值

可以用 ->或者 -->

~~~sql
select js -> '$.name' AS NAME,js->'$.age' AS age 
~~~

# 13 约束constraint

​		数据完整性是指数据的精确性和可靠性。防止数据库中存在不符合规定的数据和防止因错误信息的输入输出造成无效操作或错误信息而提出的。

为了保证数据的完整性，sql规范以约束的方式对表数据进行额外的条件限制，从一下四个方面考虑：

- 实体完整性：同一个表不能存在两个完全相同无法区分的记录
- 域完整性：年龄范围，性别范围
- 引用完整性：员工所在部门，在部门表中要能找到这个部门
- 用户自定义完整性：用户名唯一，密码不能为空

#### 什么是约束

​	约束是表级的强制规定

​	可以在创建表时规定约束（通过create table）

#### 约束分类：

查询约束：

~~~ sql
SELECT * FROM information_schema.table_constraints
WHERE table_name = 'employees'
~~~

- 角度一：约束的字段的个数

  - 单列约束 vs 多列约束

- 角度二：约束的作用范围

  - 列级约束：声明此约束时，声明在对应字段后面
  - 表级约束：在表中所有字段声明完后，在所有字段后面声明的约束

- 角度三：约束的作用（或功能）

  - not null  非空约束

    - 限制某个字段部位空 不能给组合设置 只能给列设置

    - ~~~sql
      创建约束
      CREATE TABLE test1(
      		id INT NOT NULL, 
      		last_name VARCHAR(15) NOT NULL,
      		email VARCHAR(25),
      		salary DECIMAL(10,2)
      )
      ~~~

    - ~~~sql
      修改约束
      ALTER TABLE test1
      MODIFY email VARCHAR(25) NOT NULL
      ~~~

  - unique 唯一性约束

    - 来限制某个字段不能重复

    - ~~~sql
      CREATE TABLE test2(
      	id INT UNIQUE,  #列级约束
      	last_name VARCHAR(15),
      	email varchar(25),
      	salary DECIMAL(10,2)
      	#表级约束
      	CONSTRAINT uk_test2_email UNIQUE(email)
      )
      ~~~

    - 可以向声明为unique的字段上添加null值

    - 向创建好的表中添加约束

      - ~~~sql
        ALTER TABLE test2
        ADD CONSTRAINT uk_test2_sal UNIQUE(salary)
        ~~~

    - 复合的唯一性约束

      - ~~~sql
        CREATE TABLE user(
        	id INT,
        	name VARCHAR(15),
        	password varchar(25),
        	CONSTRAINT uk_user_name_pwd UNIQUE(name,password)
        )
        ~~~

    - 删除唯一性约束

      - 添加唯一性约束的列上也会自动创建唯一索引

      - 删除唯一约束只能通过删除唯一索引的方式删除

      - 删除时需要指明唯一索引名，唯一索引名就是唯一约束名一样

      - 如果创建唯一约束时未指定名称 如果是单列，就默认和列名相同，如果是组合列，就默认第一个

      - ~~~sql
        ALTER TABLE test2
        DROP INDEX uk_user_name_pwd  
        ~~~

  - primary key 主键约束

    - 唯一约束 + 非空约束的组合 

    - 一个表中只能有一个**主键约束*  

    - 主键索引效率更高 删除主键约束 最好不要删

      ~~~sql
      CREATE TABLE test3(
      	id INT PRIMARY key,  # 列级约束
      	last_name varchar(25),
      	salary DECIMAL(10,2),
      	email varchar(25)
      )
      CREATE TABLE test3(
      	id INT ,  # 列级约束
      	last_name varchar(25),
      	salary DECIMAL(10,2),
      	email varchar(25)
      	constraint pk_test2_id PRIMARY KEY(id)
      )
      # 添加主键约束
      ALTER TABLE test3
      ADD PRIMARY KEY(id)
      # 删除主键约束
      ALTER TABLE test3
      DROP primary KEY
      ~~~

  - foreign key 外键约束

    - 限定某个表的某个字段的引用完整性

    - 手动删除索引

    - ~~~sql
      # 先建主表
      CREATE TABLE dept1(
      	dept_id INT primary key,
      	dept1_name varchar(15)
      )
      # 再建从表
      CREATE TABLE emp1(
      	emp_id INT primary key auto_increment,
      	emp_name varchar(15),
      	departmen_id INT,
      	
      	# 表级约束
      	constraint fk_emp1_dept_id foreign key (deparmen_id) references dept1(dept_id)
      )
      ~~~

      #### 约束等级

      - Cascade方式 ：在父表上updata/delete记录 同步删掉子表
      - Set null 方式：在父表上updata/delete记录，子表上匹配记录设置为null
      - No action方式 ： 如果子表中有匹配记录，则不允许对浮标对应父表进行操作
      - restrict方式 ： 同no action

      #### 删除外键约束

      ~~~sql
      # 删除外键约束
      ALTER TABLE emp1
      DROP FOREIGN KEY fk_emp1_dept_id
      # 再手动删除外键约束对应的普通索引
      show index from emp1
      alter table emp1
      DROP INDEX fk_emp1_dept_id
      ~~~

      

  - check 检查约束

    - 检查某个字段的值是否符合xx要求 一般指的是范围

    - ~~~sql
      CREATE table test10(
      	id int,
      	last_name varchar(15),
      	salary decimal(10,2) check(salary > 2000)
      )
      ~~~

  - default 默认值约束

    - 给某个字段/某列指定默认值，一旦设置默认值，在插入数据时，如果此字段没有显式赋值，这为默认值

    #### 自增列 AUTO_INCREMENT

    - 某个字段的自增

    - 一个表最多只能有一个自增长列

    - 当需要产生唯一标识符或者顺序值时，可设置自增长列

    - 自增长列约束的列必须是键 主键或唯一键

    - 必须是整数类型

    - 开发中一旦主键上声明有AUTO_INCREMENT，则我们在添加数据时，就不用管

    - ~~~sql
      CREATE TABLE test3(
      	id INT PRIMARY KEY AUTO_INCREMENT,
      	last_name varchar(15)
      )
      ~~~

#### 添加约束

​	create table 时 添加约束

​	alter table 时增加约束、删除约束

# 14 视图

- 数据字典 就是系统表 ，存放数据库相关信息的表，系统表的数据通常由数据库系统维护

- 约束 数据的完整性

- 视图  一个或者多个数据表里的数据的逻辑显示

- 索引 用于提高查询的性能 相当于书的目录

- 存储过程 用于完成一次完整的业务处理，没有返回值，可以通过传出参数将多个值传给调用环境

- 存储函数 用于完成一次特定的计算 具有一个返回值

- 触发器 相当于一个事件监听器 当数据库发生特定事件后，触发器被触发，完成相应的处理

  

  #### 视图概述

  是一种虚拟的表 本身不具有数据 占用很少空间 

  视图建立在已有表的基础上，视图依赖建立的这些表称为基表

  视图本身的删除，不会影响基表数据的删除

  视图的应用场景：针对小型项目，不推荐使用视图；针对大型项目，可以考虑使用视图。

  视图优点：简化查询。 控制数据的访问权限

#### 创建视图

~~~sql
# 针对单表
CREATE VIEW vu_emp1
AS
SELECT employee_id,last_name,salary
FROM employees
WHERE salary > 8000
SELECT * FROM vu_emp1
# 方式二
CREATE VIEW vu_emp1(emp_id,name,mothly_sal)
AS
SELECT employee_id,last_name,salary
FROM employees
WHERE salary > 8000
SELECT * FROM vu_emp1
~~~

~~~sql
# 查看视图的属性信息
SHOW TABLE STATUS LIKE 'vu_emp1'
# 查视图的详细定义信息
SHOW create VIEW vu_emp1
~~~

#### 更新视图和删除视图

更新表中的数据也会导致视图中数据的修改

~~~sql
# 方式一 修改视图
CREATE or REPLACE VIEW vu_emp1
AS
SELECT employee_id,last_name,salary,email
FROM employees
WHERE salary > 7000

# 方式二
ALTER VIEW vu_emp1
AS
SELECT employee_id,last_name,salary,email
FROM employees
WHERE salary > 7000

# 删除视图
DROP VIEW 
~~~

#### 总结

- 视图优点：
  - 操作简单
  - 减少数据冗余
  - 数据安全 控制访问权限
  - 适应灵活多变的需求
  - 能够分解复杂的查询逻辑
- 视图不足：
  - 表中的结构变了，视图也要做修改 
  - 视图过多，维护成本很高
  - 在创建视图的时候，要结合实际项目，考虑视图的优点和不足

# 15 存储过程与函数

#### 存储过程概述

​	一组经过预先编译的SQL语句的封装

​	执行过程  存储过程预先存储在mysql服务器上，需要执行的时候，客户端只需要向服务器发出调用存储过程的命令，服务端就可以把预先存储好的sql语句全部执行

- 好处：减少网络传输量 简化操作 减少了sql暴露的风险 提高复用性
- 可以直接在底层操作

#### 分类

- 没有参数
- 仅仅带IN类型
- 仅仅带out类型
- 既有in又有out
- 带inout

~~~sql
# 存储过程与存储函数
delimiter $
create procedure select_all_data()
BEGIN
		select * from employees;
end $
delimiter ;
CALL XXX
~~~

# 16 变量、流程控制和游标

#### 变量

系统变量分为全局系统变量 global 以及会话 session 如果不写默认会话级别	 	

~~~sql
show global variables
show session variables 
show variables
~~~

#### 用户变量

会话用户变量  局部用户变量（使用在存储过程和存储函数当中）

#### 游标

​		能够对结果集中的每一条记录进行定位，并对指向的记录中的数据进行操作的数据结构。游标让sql这种面向集合的语言有了面向过程的开发能力。相当于指针。

​		使用游标步骤：

- 声明游标
  - DECLARE
- 打开游标
  - open
- 使用游标
  - fetch
- 关闭游标
  - close

#### mysql8.0新特性 -- 全局变量的持久化

# 17 触发器

​	在实际开发中，我们经常会遇到：有2个或者多个相关联的表，如商品信息和库存信息 分别放在两个不同的数据表中，如商品信息和库存信息分别放在两个不同的数据表中，我们添加数据时，为了保证数据的完整性，必须同时在库存中添加一条记录。

​	触发器是由事件来触发的某个操作，这些事件包含insert，updata，delete

# 18 mysql8的其他新特性

