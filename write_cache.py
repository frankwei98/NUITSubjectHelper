import json


def write(week, weekday):
    file_name = '{wk} {wkday}'.format(
        wk=week, wkday=weekday
    )
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump()
