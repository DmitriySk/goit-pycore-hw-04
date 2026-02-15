
def create_file():
    with open('task_1.txt', 'w+') as file:
        file.write('\n'.join([
            'Alex Korp,3000',
            'Nikita Borisenko,2000',
            'Sitarama Raju,1000'
        ]))

def total_salary(path: str = 'task_1.txt'):
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print('File not found!')
        return [0, 0]


    total, average = 0, 0.0
    for line in lines:
        name, salary = line.split(',')
        if salary.isdecimal():
            total += int(salary)
    average = round(total / len(lines), 2)
    return [total, average]

create_file()
total, average = total_salary('task_1.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")