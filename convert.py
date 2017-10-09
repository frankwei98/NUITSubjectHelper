import json


class Convert:
    def __init__(self, filename):
        self.filename = filename

    def read_json(self):
        """
        :return: Raw JSON
        """
        with open(self.filename, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get_data(self):
        """
        :return: A list with dict in Chinese Keyword
        """
        return list(map(translate_pinyin_attribute, self.read_json()))


        # def what_cal_need(self):
        #     # TODO do this in future
        #     result = []
        #     for class_item in self.get_data():
        #         _ics_title = class_item['课程名称'] + class_item['授课老师'] + class_item['教室']
        #         _ics_location = class_item['教室']
        #         _ics_date = class_item['星期']
        #         result.append(
        #             dict(
        #                 节次=self.split_int_in_string_into_list(class_item['jcdm2']),
        #                 开课周=self.split_int_in_string_into_list(class_item['zcs']),
        #                 星期=class_item['xq'])
        #         )
        #     return result


def split_int_in_string_into_list(str_of_ints):
    """

    :param str_of_ints: A list of int in str format
    :return: A *sorted* list of the int
    """
    return sorted([int(x) for x in str_of_ints.split(',')])


def translate_pinyin_attribute(lesson):
    return dict(课程编号=lesson['kcbh'],
                班级=lesson['jxbmc'],
                节次=split_int_in_string_into_list(lesson['jcdm2']),
                开课周=split_int_in_string_into_list(lesson['zcs']),
                星期=lesson['xq'],
                课程名称=lesson['kcmc'],
                教室=lesson['jxcdmcs'],
                授课老师=lesson['teaxms'])
