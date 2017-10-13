import json
from functools import reduce

import utils


def search(week, weekday):
    """

    :param week: the order of week, like 1 to 16
    :param weekday: the order of weekday, like Mon is 1, Sun is 7
    :return: lessons schedule
    """
    with open(
            './weekly_data/{}.json'.format(week),
            'r',
            encoding='utf-8'
    ) as f:
        file = json.load(f)
        lessons = file['lessons']

        def filter_lesson(lesson):
            """
            对 lessons 的元素 lesson 做 filter_lesson(),
            若成立则进入filtered_result
            :param lesson: lessons 的元素 lesson
            :return: Boolean: True or False
            """
            return weekday == lesson['weekday']

        filtered_result = filter(
            filter_lesson,
            lessons
        )

    return sorted(
        filtered_result,
        key=lambda l: l['order']
    )


def get_msg_of_the_day(week, weekday):
    """

    :param week: week
    :param weekday: weekday
    :return: The message that user-reading-friendly
    """
    result = list(
        search(week, weekday)
    )
    if not result:
        # For sequences, (strings, lists, tuples),
        # use the fact that empty sequences are false.
        return_str = '今天星期{} 没课! 一起出去耍吧～'.format(weekday)
    else:
        return_str = '今天第{}周 星期{} 一共有{}节课，{} 课程如下\n'.format(
            week,
            utils.int2cn(str(weekday)),
            len(result),
            utils.days_left()
        )
        lessons_str = reduce(lambda x, y: '{}\n{}'.format(
            x, y), map(utils.get_simple, result))
        return_str += lessons_str

    return return_str


if __name__ == '__main__':
    # search_week = int(input('请输入第几周(阿拉伯数字)'))
    # search_weekday = int(input('请输入星期几(阿拉伯数字)'))
    # print(get_msg_of_the_day(search_week, search_weekday))
    # print today's schedule
    schedule = utils.get_today_week_weekday_from_date()
    print(get_msg_of_the_day(schedule['weeks'], schedule['weekdays']))
