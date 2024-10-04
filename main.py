import csv
import json
from datetime import datetime


database = [{'ФИО': 'Иванов Иван Иванович', 'Должность': 'Менеджер', 'Дата найма': '22.10.2013', 'Оклад': 250000,
             'Пол': 'муж'},
            {'ФИО': 'Сорокина Екатерина Матвеевна', 'Должность': 'Аналитик', 'Дата найма': '12.03.2020',
             'Оклад': 75000, 'Пол': 'жен'},
            {'ФИО': 'Струков Иван Сергеевич', 'Должность': 'Старший программист', 'Дата найма': '23.04.2012',
             'Оклад': 150000, 'Пол': 'муж'},
            {'ФИО': 'Корнеева Анна Игоревна', 'Должность': 'Ведущий программист', 'Дата найма': '22.02.2015',
             'Оклад': 120000, 'Пол': 'жен'},
            {'ФИО': 'Старчиков Сергей Анатольевич', 'Должность': 'Младший программист', 'Дата найма': '12.11.2021',
             'Оклад': 50000, 'Пол': 'муж'},
            {'ФИО': 'Бутенко Артем Андреевич', 'Должность': 'Архитектор', 'Дата найма': '12.02.2010', 'Оклад': 200000,
             'Пол': 'муж'},
            {'ФИО': 'Савченко Алина Сергеевна', 'Должность': 'Старший аналитик', 'Дата найма': '13.04.2016',
             'Оклад': 100000, 'Пол': 'жен'}]


def bonus(database):
    for i in database:
        if 'программист' in i['Должность']:
            bonus_sum = str(int(i['Оклад'] * 0.03))
            print(f"{i['ФИО']} получит премию {bonus_sum} рублей.")


def holidays(database):
    for i in database:
        if i['Пол'] == 'муж':
            print(f"{i['ФИО']} получит премию 2000 рублей к 23 февраля.")
        elif i['Пол'] == 'жен':
            print(f"{i['ФИО']} получит премию 2000 рублей к 8 марта.")


def indexation(database):
    current_year = datetime.now().year
    for i in database:
        hire_date = datetime.strptime(i['Дата найма'], '%d.%m.%Y')
        years_worked = current_year - hire_date.year
        if years_worked > 10:
            indexation = int(round(i['Оклад'] * 0.07))
            newsalary = i['Оклад'] + indexation
            print(f"{i['ФИО']} получит новую зарпату размером {newsalary} рублей с учетом индексации равной "
                  f"{indexation} рублей (7%)")
        else:
            indexation = int(round(i['Оклад'] * 0.05))
            newsalary = i['Оклад'] + indexation
            print(f"{i['ФИО']} получит новую зарпату размером {newsalary} рублей с учетом индексации равной "
                  f"{indexation} рублей (5%)")
            

def otpusk(database):
    current_date = datetime.now()
    otpuskl = []
    for i in database:
        hire_date = datetime.strptime(i['Дата найма'], '%d.%m.%Y')
        months = (current_date.year - hire_date.year) * 12 + (current_date.month - hire_date.month)
        if months > 6:
            otpuskl.append(i['ФИО'])
    print("Сотрудники, отработавшие более 6 месяцев:")
    for j in otpuskl:
        print(j)
    return otpuskl


def to_csv(file_name, database):
    with open(file_name, 'w', newline='') as file:
        fields = ['ФИО', 'Должность', 'Дата найма', 'Оклад', 'Пол']
        file_writer = csv.DictWriter(file, fieldnames=fields)
        file_writer.writeheader()
        for item in database:
            file_writer.writerow(item)


def to_json(file_name, database):
    with open(file_name, 'w') as file:
        json.dump(database, file)


# bonus(database)
# holidays(database)
# indexation(database)
# otpusk(database)
# to_csv('metod1.csv', database)
# to_json('metod2.json', database)
