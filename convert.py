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
        result = []
        for class_item in self.read_json():
            result.append(
                dict(课程编号=class_item['kcbh'],
                     班级=class_item['jxbmc'],
                     节次=self.split_int_in_string_into_list(class_item['jcdm2']),
                     开课周=self.split_int_in_string_into_list(class_item['zcs']),
                     星期=class_item['xq'],
                     课程名称=class_item['kcmc'],
                     教室=class_item['jxcdmcs'],
                     授课老师=class_item['teaxms'])
            )
        return result

    @staticmethod
    def split_int_in_string_into_list(str_of_ints):
        """

        :param str_of_ints: A list of int in str format
        :return: A *sorted* list of the int
        """
        return sorted([int(x) for x in str_of_ints.split(',')])

    def what_cal_need(self):
        # TODO do this in future
        result = []
        for class_item in self.get_data():
            _ics_title = class_item['课程名称'] + class_item['授课老师'] + class_item['教室']
            _ics_location = class_item['教室']
            _ics_date = class_item['星期']
            result.append(
                dict(
                    节次=self.split_int_in_string_into_list(class_item['jcdm2']),
                    开课周=self.split_int_in_string_into_list(class_item['zcs']),
                    星期=class_item['xq'])
            )
        return result


