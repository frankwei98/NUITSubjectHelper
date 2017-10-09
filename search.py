from convert import Convert

data = Convert('data.json').get_data()


def search(week):
    # result = []
    def search_by_week(lesson):
        return week in lesson['开课周']

    result = filter(
        search_by_week,
        data
    )

    # def sort_lesson_by_weekday(lesson):
    #     return lesson['星期']

    return sorted(
        result,
        key=lambda l: l['星期']
    )


def get_simple(x):
    return {
        '课程名称': x['课程名称'],
        '教室': x['教室']
    }


if __name__ == '__main__':
    search_week = int(input('请输入第几周(阿拉伯数字)'))
    result = search(search_week)
    # result = list(map(get_simple, result))
    for item in result:
        print(item)

    print('第 {0} 周一共有 {1} 节课'.format(
        search_week,
        len(result)
    ))
