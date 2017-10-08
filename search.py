from convert import Convert

if __name__ == '__main__':
    search_week = int(input('请输入第几周(阿拉伯数字)'))
    data = Convert('data.json').get_data()
    for item in data:
        for week in item['开课周']:
            if week == search_week:
                print(item)
