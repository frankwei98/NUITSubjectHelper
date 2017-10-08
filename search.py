from convert import Convert


def search(week):
    # result = []
    data = Convert('data.json').get_data()
    for item in data:
        for week in item['开课周']:
            if week == search_week:
                yield item
                break
    # return result


if __name__ == '__main__':
    search_week = int(input('请输入第几周(阿拉伯数字)'))
    for item in list(search(search_week)):
        print(item)
