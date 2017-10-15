import json

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


if __name__ == '__main__':
    # print today's schedule
    schedule = utils.get_today_week_weekday_from_date()
    [print(lesson) for lesson in search(schedule['weeks'], schedule['weekdays'])]
