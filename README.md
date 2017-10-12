# NUIT Schedule Helper 📅

## 一些点子

* 微信🤖️ 推送新一天的课程安排 (只需要和 WXPY 整合)

* 模拟登陆教务网

## 安装依赖

命令行🖥️运行以下命令：

> pip install -r requirements.txt

## Todo List

### WeChat Bot

 - [ ] 集成事务管理 `schedule`

 - [ ] 集成 [wxpy](https://github.com/youfou/wxpy) 微信机器人 🤖️ , 按天推送提醒课程安排

### 爬虫

 - [ ] 自动从教务网抓取课表 (涉及到🕷️)

### Worked for Apple

 - [ ] 转化为 📅 iCalender 日历所用的 `.ics` 日历文件


## 提案

* 按天为单位，以时间为顺序的课表体系

Example: 

> ```json
> {
>   "date": "2017-09-18",
>   "weekday": 1,
>   "lessons": [
>     {
>       "name": "Java",
>       "isOptional": false,
>       // get_time func provided
>       "time": "1",
>       "teacher": "xulin",
>       "location": "A123"
>     },
>     {
>       "name": "PHP",
>       "isOptional": true,
>       // get_time func provided
>       "time": "2",
>       "teacher": "xulin",
>       "location": "F321"
>     }
>   ]
> }
> ```



* 挖掘到新接口 直接返回json 

  > http://172.13.1.32/xsbjkbcx!getKbRq.action
  >
  > URL参数：
  >
  > xnxqdm={学期番号}
  >
  > zc={周次}
  
  
### How to write?

每周为一次调用，每周写7个文件对应一周中的7天