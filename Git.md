## Git

​	是一个分布式版本控制工具，快速处理从小到大的各种项目。

​	廉价的本地库，优于其他的版本控制器

	### 版本控制

​	版本控制工具：

- 集中式版本控制工具  svn  看的都是同一个项目  缺点：中央服务器的单点故障，如果服务器宕机一小时 那么在这一小时 谁都提交不了代码。

- 分布式版本控制工具 git 版本控制是在本地进行

  写代码 -->工作区 -git add- > 暂存区 -git commit ->本地库

  ​											 临时存储					历史版本（删不掉）

  ### Git和代码托管中心

  - 代码托管中心是基于网络服务器的远程代码仓库 一般简单称为远程库
    - 局域网	GitLab
    - 互联网    GitHub（外网） Gitee（国内网站）

  ### Git常用命令

  - git config --global（全局） user.name   设置用户签名
  - git config --global user.email   设置用户签名   ⚠️ 第一次使用必须设置签名 否则无法提交代码
  - git init  初始化本地库。获取目录的管理权
  - git status 查看状态
  - git add XXX  添加至暂存区
  - 提交本地库 形成历史版本  git commit -m “版本信息”  hello.txt
  - git reflog 查看版本信息
  - git log 日志信息

### 查看历史版本信息

- git reset --hard 版本号  切换版本

### Git分支

​	好处：并行推进多个功能开发  如果一个分支开发失败，不会影响其他的程序

#### 分支操作

- git branch 分支名   创建分支
- git branch -v。查看分支
- git chechout 分支名。切换分支
- git merge 分支名。把制定的分支合并到当前分支
- 代码冲突问题：两个分支在同一个文件的同一个位置两套完全不同的修改，必需得人为决定新代码的内容

#### Git团队协作机制

- 团队协作  本地库 push 到代码托管中心  clone 到本地库 修改push到远程库。（需要将人加到团队里面才能push）
- 跨团队协作  fork 本地库 修改 （pull request）上传到别人的远程库

## GitHub

- 创建远程仓库名称

  - git remote -v 查看当前所有远程地址别名

  - git remote add 别名 远程地址

  - >git-demo	https://github.com/shengmouget/git-demo.git (fetch) 拉取
    >
    >git-demo	https://github.com/shengmouget/git-demo.git (push) 推送

  - git push 别名 分支 将代码推送

  - git pull  别名 分支 将代码拉取

- git clone

- token 

- >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

## Git_IDEA集成Git环境

​	配置忽略文件，与项目实际功能无关，不参与服务器上部署运行，把他们忽略能够屏蔽IDE工具之间的差异

​	怎么忽略？

>1. 创建忽略文件 XXX.ignore  建议是git.ignore 
>2. 有模板
>3. 打开IDEA 配置文件

## Gitee码云

 	开源中国推出的Git托管服务平台

## Gitlab

​	Gitlab由乌克兰程序员用Ruby语言写的，之后改用Go重写