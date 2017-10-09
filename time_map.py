order_to_time = {
    1: '08:40-10:00',
    2: '10:20-11:40',
    3: '14:10-15:30',
    4: '15:50-17:10',
    5: '18:30-19:50',
    6: '20:10-21:30',
}


def get_time(jieci_array):
    actual_order = int(jieci_array[1] / 2)
    print('{ja} 是实际上的第 {ao} 节课，在 {t_str} 时段上课'.format(
        ja=jieci_array,
        ao=actual_order,
        t_str=order_to_time[actual_order]
    ))
    return order_to_time[actual_order]


if __name__ == '__main__':
    get_time([3, 4])  # for test
