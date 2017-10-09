from convert import Convert


def search(search_week):
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
    result = list(search(search_week))
    for item in result:
        print(item)

    print('第 {0} 周一共有 {1} 节课'.format(
        search_week,
        len(result)
    ))
