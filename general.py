import os

# Для каждого обработанного сайта своя папка
def creatre_project(directory):
    if not os.path.exists(directory):
        print('New project: ' + directory)
        os.makedirs(directory)

# Создаем очередь и проверенные ссылки (если уже не были созданы)
# project_name -обычно доменное имя(directory)
# base_url - url начальной страницы
def create_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

# создание нового файла и добавление туда инф-и
def write_file(name,base):
    file = open(name, 'x')
    file.write(base)
    file.close()

# добавление инф-и в существующий файл
def append_file(path,data):
    with open(path,'a') as file:
        file.write(data + '\n')
# удаление данных из файла
def delete_content(path):
    with open(path, 'w'):
        pass
# файл -> set
def file_to_set(name):
    res = set()
    with open(name,'rt') as f:
        for line in f:
            res.add(line.replace('\n',''))
    return res
# set -> файл
def set_to_file(links,file):
    delete_content(file)
    for link in sorted(links):
        append_file(file,link)
