import json
from functools import reduce

import utils
from convert import Convert


def search(week, weekday):
    with open('./weekly_data/{}.json'.format(week), 'r', encoding='utf-8') as f:
        file = json.load(f)
        lessons = file['lessons']

        # 对 lessons 的元素 lesson 做 weekday == lesson['weekday'],若成立则进入filtered_result
        filtered_result = filter(
            # Use lambda to check if 'weekday' was equals to lesson's weekday or not,
            # so that we can filtered right the lessons in provided lambda exp.
            lambda lesson: weekday == lesson['weekday'],
            lessons
        )

    return sorted(
        filtered_result,
        key=lambda l: l['order']
    )


def get_msg_of_the_day(week, weekday):
    result = list(
        search(week, weekday)
    )
    if len(result) == 0:
        return '今天星期{} 没课! 一起出去耍吧～'.format(weekday)
    else:
        return_str = '今天第{}周 星期{} 一共有{}节课，{} 课程如下\n'.format(
            week,
            utils.int2cn(str(weekday)),
            len(result),
            utils.days_left()
        )

        res = reduce(lambda x, y: '{}\n{}'.format(x, y), map(utils.get_simple, result))

        return return_str + res


if __name__ == '__main__':
    search_week = int(input('请输入第几周(阿拉伯数字)'))
    search_weekday = int(input('请输入星期几(阿拉伯数字)'))
    print(get_msg_of_the_day(search_week, search_weekday))
    # print today's schedule
    today = utils.get_today_week_weekday_from_date()
    print(get_msg_of_the_day(today['weeks'], today['weekdays']))
