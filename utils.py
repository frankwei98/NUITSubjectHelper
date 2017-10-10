from datetime import date, timedelta

# 第一天上课和最后一天的上课时间
FIRST_DAY = date(2017, 9, 18)
LAST_DAY = FIRST_DAY + timedelta(
    weeks=16 - 1,
    days=5 - 1
)
TODAY = date.today()

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
    }
    return d[s]


def get_time(array_of_order):
    actual_order = int(array_of_order[1] / 2)
    return order_to_time[actual_order]


def get_date_from_week(week=0, weekday=0):
    """

    :param week: the week that need located
    :param weekday: the day start from monday
    :return: A date object indicate the date itself
    """
    week_diff = timedelta(weeks=week - 1, days=weekday)  # because week start from 0, not 1
    return FIRST_DAY + week_diff


def days_since_first_day():
    return '你已经上课了 {} 天'.format(
        (TODAY - FIRST_DAY).days
    )


def days_left():
    return '距离最后一节课还有 {} 天'.format(
        (LAST_DAY - TODAY).days
    )


if __name__ == '__main__':
    print(get_date_from_week(week=4, weekday=5).weekday())  # 4 weeks later
    print(get_date_from_week(week=4, weekday=1))  # 4 weeks later
    print(days_since_first_day())
    print(LAST_DAY)
    print(days_left())
