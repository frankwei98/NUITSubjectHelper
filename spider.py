import json

import requests


def get_timetable_info(semester, week):
    json_url = 'http://172.13.1.32/xsbjkbcx!getKbRq.action'
    url_param = {
        # weird pinyin params by chinese "programmer"
        # System developer is 广州丛师科技有限公司
        'xnxqdm': semester,
        'zc': week
    }
    # Important! Please CHANGE JSESSIONID field before crawl data
    cookie = dict(
        JSESSIONID='ENTER YOUR JSESSIONID'
    )

    req = requests.get(json_url, params=url_param, cookies=cookie)
    return req.json()


if __name__ == '__main__':
    weeks = range(1, 17)
    for week in weeks:
        with open('./week/{}.json'.format(week), 'w', encoding='utf-8') as f:
            json.dump(get_timetable_info(20171, week), f, ensure_ascii=False, sort_keys=True, indent=2)
