from datetime import date, timedelta

order_to_time = {
    1: '08:40-10:00',
    2: '10:20-11:40',
    3: '14:10-15:30',
    4: '15:50-17:10',
    5: '18:30-19:50',
    6: '20:10-21:30',
}


def get_time(array_of_order):
    actual_order = int(array_of_order[1] / 2)
    print('{ja} 是实际上的第 {ao} 节课，在 {t_str} 时段上课'.format(
        ja=array_of_order,
        ao=actual_order,
        t_str=order_to_time[actual_order]
    ))
    return order_to_time[actual_order]


def get_date_from_week(week=0, weekday=0):
    """

    :param week: the week that need located
    :param weekday: the day start from monday
    :return: A date object indicate the date itself
    """
    monday_in_the_first_week = date(2017, 9, 18)
    week_diff = timedelta(weeks=week - 1, days=weekday)  # because week start from 0, not 1
    return monday_in_the_first_week + week_diff


if __name__ == '__main__':
    print(get_date_from_week(week=4, weekday=0).weekday())  # 4 weeks later
    print(get_date_from_week(week=4, weekday=1))  # 4 weeks later
