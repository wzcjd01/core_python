#!/usr/bin/env python
__author__ = 'Wang Zhicheng'


def ex0905():
    from corepython import wzc_letter_grade as _grade
    import csv
    reader = csv.reader(open('grade.csv', 'r'), csv.excel_tab)
    for student in reader:
        # todo:
        pass
