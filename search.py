import utils
from convert import Convert

data = Convert('data.json').get_data()


def search(week):
    return sorted(
        filter(
            # Use lambda to check if 'week' was in list 'weeks' or not,
            # so that we can filtered the lessons needed in providing week
            lambda lesson: week in lesson['开课周'],
            data
        ),
        key=lambda l: l['星期']
    )


if __name__ == '__main__':
    search_week = int(input('请输入第几周(阿拉伯数字)'))
    result = list(
        map(utils.get_simple,
            search(search_week)
            )
    )
    [print(item) for item in result]  # list comprehension!!!

    print('第 {0} 周一共有 {1} 节课'.format(
        search_week,
        len(result)
    ))
