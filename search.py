from convert import Convert


def search(week):
    # result = []
    data = Convert('data.json').get_data()
    for lesson in data:
        for week in lesson['开课周']:
            if week == search_week:
                yield lesson
                break
    # return result


if __name__ == '__main__':
    search_week = int(input('请输入第几周(阿拉伯数字)'))
    for item in list(search(search_week)):
        print(item)
