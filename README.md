# FlagList
本项目为我的考核作业，展示了一个使用 Django 搭建的 ~~FlagList~~ TodoList ，由于 JS 还没学 ... 前后端尚未分离。

题目要求在可视化 API 中均已实现，前后耦合的代码有待改进。

在事项列表界面用 React & webpack 尝试导入了 API 中的数据。

## Requirements
* Django (1.8.18)
* djangorestframework (3.6.3)
* django-filter (1.0.4)
* django-webpack-loader (0.2.4)
* coreapi (2.3.1)
* Python (2.7.13)
* Bootstrap (3.3.7)
* npm (npm install --save-dev jquery react react-dom webpack webpack-bundle-tracker babel-loader babel-core babel-preset-es2015 babel-preset-react)
* 待添加 ……

## API
API Root: 127.0.0.1:8000/api

Schema: 127.0.0.1:8000/schema

## 图片展示
![index](https://github.com/helsonxiao/flaglist/blob/master/display/index.png)

GIF 链接：

https://cl.ly/lfqx, https://cl.ly/lgFo

https://cl.ly/lfyS, https://cl.ly/lfVX

https://cl.ly/lfVN, https://cl.ly/lg4c

https://cl.ly/lfzo, https://cl.ly/lg5P

## 注意事项
请于 127.0.0.1:8000/admin 登陆后再进行操作，因为前端登陆界面还没写出来。。。

账号密码：admin - 123456

## 已实现功能
* 增加一个待办事项
* 删除一个待办事项
* 标记一个待办事项为已完成
* 编辑一个待办事项的具体内容
* 列出所有的待办事项
* 列出已办事项
* 列出未办事项
* 分用户显示事件
* 待办事项可以设置 priority (尚未在列表中显示)
* 待办事项可以设置 expire date (尚未在列表中显示)
* 列表界面支持翻页

## Todo
* 支持按照不同的方式排序，如优先级，expire date
* 前端注册及登陆
* 炫酷的界面
* 更换 ProgreSQL
* Deploy
* **前后端分离**
* 增加错误检查