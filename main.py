import json
import os
import sys
import jsonschema
import pandas


files_json = os.listdir('task_folder/event/')
files_schema = os.listdir('task_folder/schema/')
print(files_json, '\n', files_schema)
new_list = [['Не валидный файл', 'Тип ошибки', 'Назавние ошибки\\ошибок']]

for i in files_json:
    with open("task_folder/event/" + i, "r") as read_file:
        data1 = json.load(read_file)
        if data1 is None or data1 == {}:
            new_list.append([i, 'Ошибка в Json файле', 'Либо файл.json пустой, либо json пустой'])
            continue
        else:
            event = data1["event"]
            try:
                None
            except KeyError:
                new_list.append([i, 'Ошибка в Json файле', 'В json не указана схема для проверки валидности,'
                                                           'либо указана неправильная схема'])
                continue
        # data = dict(data1["data"])
    if event+'.schema' in files_schema:
        with open("task_folder/schema/" + event + ".schema", "r") as read_file:
            schema = json.load(read_file)
        for idx, item in enumerate(data1):
            try:
                None
            except jsonschema.exceptions.ValidationError as ve:
                # sys.stderr.write("Record #{}: ERROR\n".format(idx))
                u = sys.stderr.write(str(ve.message) + "; ")
                new_list.append([i, 'Ошибка в Json файле', u])
    else:
        new_list.append([i, 'Ошибка в Json файле', 'В json не указана схема для проверки валидности, '
                                                   'либо указана неправильная схема'])
df = pandas.DataFrame(new_list)
html = df.to_html(classes='Attendance', index=False, header=False)
print(html)
Html_file = open("README.html", "w", encoding='UTF-8')
Html_file.write(html)
Html_file.close
