def create_file():
    with open('task_2.txt', 'w+') as file:
        file.write('\n'.join([
            '60b90c1c13067a15887e1ae1,Tayson,3',
            '60b90c2413067a15887e1ae2,Vika,1',
            '60b90c2e13067a15887e1ae3,Barsik,2',
            '60b90c3b13067a15887e1ae4,Simon,12',
            '60b90c4613067a15887e1ae5,Tessi,5',
        ]))

def get_cats_info(path: str = 'task_2.txt'):
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print('File not found!')
        return []

    info = []
    for line in lines:
        id, name, age = line.strip().split(',')
        info.append({'id': id, 'name': name, 'age': age})

    return info

create_file()
cats_info = get_cats_info('task_2.txt')
for cat in cats_info:
    print(cat)