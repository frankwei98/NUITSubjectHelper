import json
from fake_useragent import UserAgent
import requests

import utils

import config


def get_timetable_info(semester, week):
    json_url = '{server}/xsbjkbcx!getKbRq.action'.format(
        server=config.SERVER
    )
    url_param = {
        # weird pinyin params by chinese "programmer"
        # System developer is 广州丛师科技有限公司
        'xnxqdm': semester,
        'zc': week
    }
    # Important! Please CHANGE JSESSIONID field before crawl data
    cookie = dict(
        JSESSIONID=config.YOUR_JSESSIONID
    )

    req = requests.get(json_url, params=url_param, cookies=cookie,headers={'User-Agent': UserAgent().random})
    return req.json()


def write_timetable_json(week):
    with open('./weekly_data/{}.json'.format(week), 'w', encoding='utf-8') as f:
        utils.write_json(
            obj=data_translate(
                get_timetable_info(config.SEMESTER, week)
            ),
            fp=f
        )


def data_translate(json_obj):
    return dict(
        lessons=list(map(lessons_translate, json_obj[0])),
        time=list(map(weekday_date_translate, json_obj[1]))
    )


def lessons_translate(lesson):
    return dict(
        name=lesson['kcmc'],
        classRoom=lesson['jxcdmc'],
        weekday=int(lesson['xq']),
        order=int(
            int(
                lesson['jcdm2'].split(',')[1]) / 2
        )
    )


def weekday_date_translate(x):
    # 星期名称 weekday 日期 date
    return {'weekday': int(x['xqmc']), 'date': x['rq']}


if __name__ == '__main__':
    list(map(write_timetable_json, config.WEEKS))
