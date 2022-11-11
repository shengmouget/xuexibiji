## Linux 基本配置

### 三种网络连接模式

- 桥接模式：虚拟系统可以和外部系统通讯，但是容易造成IP冲突
- NAT模式：网络地址转换模式，虚拟系统可以和外部系统通讯，而且不造成IP冲突
- 主机模式：独立的系统

## 虚拟机克隆

- 方式一 ：直接拷贝一份安装好的虚拟机

- 方式二：使用vmware的克隆操作 （⚠️ 克隆时 要关闭Linux）

## Linux目录结构

​	root 	home	bin	etc	boot(Linux启动相关文件)

## 远程登录Linux

安装好以后，[ssh](https://so.csdn.net/so/search?q=ssh&spm=1001.2101.3001.7020) server应该已经开始运行了，可以用下面的命令检查ssh server的状态

> systemctl status sshd

另外，需要的时候，还可以利用systemctl命令打开(start)/关闭(stop)/重启(restart)ssh server，例如下面的命令就可以用来重启ssh server服务

> sudo systemctl restart ssh

利用Ubuntu自带的ufw 修改防火墙状态

>首先开启防火墙
>
>sudo ufw enable
>
>打开传输ssh的端口（默认22） 
>
>sudo ufw allow ssh
>
>设置ssh server开机启动 
>
>sudo systemctl enable ssh wb

## vim/vi

一般模式——i或者a——>编辑模式

一般模式——：或者/——>命令模式 	在命令行下 :wq(保存退出) :q（退出） :q!（强制退出并且不保存）

## 基本指令

> shutdown -h now   立刻关机
>
> shutdown -h 1 1分钟后关机
>
> shutdown -r now 现在重启计算机
>
> halt 关机
>
> reboot 现在重启计算机
>
> sync 把内存数据同步到磁盘

​	登录时尽量少使用root账号登录 因为他是系统管理员 最大权限 

> logout  切换用户  su -   ⚠️ 这个只能是无界面环境下用

## 用户管理

- 添加用户 	useradd 用户名 	添加一个用户milan 默认用户在 /home/milan

  > 细节说明：也可以通过useradd -d指定目录 新的用户名，给新创建用户添加目录

- 指定/修改密码  基本语法 passwd 用户名
- 显示当前用户所在的目录 pwd
- 删除用户  userdel 用户名
- 当前用户信息 who am i
- 修改用户的组 useradd -g wudangXX XXX
- 切换分组 usermod -g XXX组 XXX人

 ## 常用指令

> pwd 当前目录绝对路径
>
> ls -a/-l（以列表的形式显示）
>
> cd 切换到指定目录 cd～ 回到当前目录的家目录  cd ..返回上一级目录
>
> mkdir 用于创建目录  -p创建多级目录
>
> rmdir  删除目录 删除的是空目录。如果需要删除非空 需要使用 rm -rf
>
> touch 创建一个空文件
>
> cp 拷贝
>
> mv移动文件于目录或者重命名
>
> less 用来分屏查看文件 
>
> echo 输出环境变量
>
> history 显示最近的指令 如需限定条数 只需要加个数字就行

### 软连接（符号连接）

​	ln -s [源文件] [软连接]

## 时间日期类

> date指令-显示当前日期
>
> date  当前时间
>
> date %Y 年份m d  ⚠️ 加引号
>
> cal 指令

## 搜索查找类

>find [搜索范围] -name 	按指定的文件名
>
>find [搜索范围] -user
>
>locate 可以快速定位文件路径  第一次运行前 必须使用updatedb指令创建locate数据库
>
>grep指令和管道符号｜ 一起使用 表示将前一个命令的处理结果输出传递给后面的命令处理 eg：cat xxx |grep "XXX "

## 压缩文件

> gzip/gunzip  前者为压缩文件。后者为解压文件
>
> gzip 文件
>
> gunzip 文件.gz
>
> zip/unzip  前者为压缩文件 后者解压
>
> zip [选项] XXX.zip 将要压缩的内容  选项 -r 递归解压。 
>
> unzip -d<目录> xxx.zip
>
> tar指令 

## 定时调度

> crontab -r 终止任务调度
>
> crontab -l 列出当前的任务调度
>
> service crond restart [启动任务调度]

at定时任务

at是一次性定时计划任务 at的守护进程atd会以后台模式运行 检查作业队列来进行。一定要保证atd进程启动

>ps -ef ｜ grep atd //可以检测atd是否在运行
