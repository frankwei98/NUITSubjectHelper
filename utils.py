import json
from datetime import date, timedelta
import config

order_to_time = {
    1: '08:40-10:00',
    3: '14:10-15:30',
    4: '15:50-17:10',
    5: '18:30-19:50',
    2: '10:20-11:40',
    6: '20:10-21:30',
}


def int2cn(s):
    d = {
        '1': '一',
        '2': '二',
        '3': '三',
        '4': '四',
        '5': '五',
        '6': '六',
        '7': '七',
    }
    return d[s]


def get_time(array_of_order):
    actual_order = int(array_of_order[1] / 2)
    return order_to_time[actual_order]


def get_date_from_week(week=0, weekday=0):
    """

    :param week: the weekly_data that need located
    :param weekday: the day start from monday
    :return: A date object indicate the date itself
    """
    week_diff = config.timedelta(weeks=week - 1, days=weekday)  # because weekly_data start from 0, not 1
    return config.FIRST_DAY + week_diff


def get_today_week_weekday_from_date():
    return get_week_weekday_from_date(config.TODAY)


def get_week_weekday_from_date(_date):
    week_diff = _date - date(2017, 9, 18)
    weeks = int(week_diff.days /7) + 1
    days = (week_diff.days % 7) + 1
    return {'weeks': weeks, 'weekdays':days}


def diff_from_today(week=0, weekday=0):
    return config.date.today() - config.timedelta(weeks=week - 1, days=weekday)


def get_simple(lesson):
    """

    :param lesson: a lesson
    :return: User-reading-friendly information about lesson
    """
    return {
        '课程名称': lesson['name'],
        '教室': lesson['classRoom'],
        '星期': int2cn(str(lesson['weekday'])),
        '时间': order_to_time[lesson['order']],
    }


def write_json(obj, fp):
    """
    :param obj: A dictionary or something that can serialize into json
    :param fp: file obj
    """
    json.dump(
        obj=obj,
        fp=fp,
        ensure_ascii=False,  # No Unicode
        sort_keys=True,
        indent=2  # beautify json
    )
    return True


def days_left():
    """

    :return: A countdown message
    """
    return '距离最后一节课还有 {} 天'.format(
        (config.LAST_DAY - config.TODAY).days
    )


# for test
if __name__ == '__main__':
    print(get_date_from_week(week=4, weekday=5).weekday())  # 4 weeks later
    print(get_date_from_week(week=4, weekday=1))  # 4 weeks later
    print(config.LAST_DAY)
    print(days_left())
