"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В
базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за
приём оргтехники на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""


from abc import ABC, abstractmethod


class OfficeTechnics(ABC):
    __ID = ''     # тип оргтехники
    attachment = ''  # к какому подразделению компании принадлежит

    def __init__(self, name):
        self.name = name

    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, tmp):
        self.__ID = tmp

    def __str__(self):
        return self.ID + ' ' + self.name + ' ' + self.attachment

    @abstractmethod
    def do_work(self, arg: str) -> str:
        pass


class Store:
    __store_items = dict()
    # список комманд пользователя для управления складом
    commands = ('add',
                'get',
                'del',
                'view',
                )

    def add(self, tech: OfficeTechnics):
        items = self.__store_items.get(tech.ID)
        if items:
            items.append(tech)
            self.__store_items.update({tech.ID: items})
        else:
            self.__store_items.update({tech.ID: [tech]})
        tech.attachment = 'Store'

    def get(self, tech, division):
        for i, item in enumerate(self.__store_items.get(tech.ID)):
            if tech.name == item.name:
                self.__store_items.get(tech.ID).pop(i)
        tech.attachment = division
        return tech

    @property
    def store_items(self):
        res = ''
        for key, itm in self.__store_items.items():
            items = ''
            for i in itm:
                items += str(i) + '; '
            res += key + ': ' + items + '\n'
        return res[:-2]

    def user_cmd(self, lst: list, cmd, name):
        # функция взаимодействия с пользователем на основе его команд
        if not len(lst) and not cmd.isdigit:
            print('List of elements is empty')
            return 0
        if cmd not in self.commands:
            print('Wrong command')
            return 0
        if cmd == self.commands[len(self.commands)-1]:  # print technics in store
            print(self.store_items)
        else:
            for i, el in enumerate(lst):
                print(i+1, ' - ', el)
            num = input('Enter technics number: ')
            if num.isdigit():
                if int(num) in range(len(lst)+1):
                    if cmd == self.commands[0]:
                        self.add(lst[int(num) - 1])     # добавление элемента на склад
                    else:
                        if lst[int(num) - 1].attachment == 'Store' and cmd == self.commands[1]:
                            self.get(lst[int(num) - 1], name)   # перемещение элемента в другой отдел
                        elif cmd == self.commands[2]:           # удаление элемента
                            if lst[int(num) - 1].attachment == 'Store':
                                self.get(lst[int(num) - 1], '')
                            lst.pop(int(num) - 1)
                else:
                    print('Wrong number')
            else:
                print('Wrong number')


class Printer(OfficeTechnics):
    def __init__(self, name):
        super().__init__(name)
        self.ID = 'Printer'

    def do_work(self, arg: str) -> str:
        return str(self) + 'Printing:' + arg


class Scanner(OfficeTechnics):

    def __init__(self, name):
        super().__init__(name)
        self.ID = 'Scanner'

    def do_work(self, arg: str) -> str:
        return str(self) + 'Scanning:' + arg


class Copier(OfficeTechnics):

    def __init__(self, name):
        super().__init__(name)
        self.ID = 'Copier'

    def do_work(self, arg: str) -> str:
        return str(self) + 'Coping:' + arg


if __name__ == '__main__':

    technics = {'1': [],
                '2': [],
                '3': [],
                }
    store = Store()

    print('Available commands:\n'
          '+ - create new technics\n'
          'add - adding technics to store\n'
          'get - moving technics to department\n'
          'del - delete technics\n'
          'view - print all elements in store\n'
          'or press Enter to exit')
    while True:
        inp = input('Enter command: ')
        if inp == '+':
            typ = input('Enter type of technics (1 - printer, 2 - scanner, 3 - copier): ')
            if typ == '1':
                technics[typ].append(Printer(input('Enter name of your printer: ')))
            elif typ == '2':
                technics[typ].append(Scanner(input('Enter name of your scanner: ')))
            elif typ == '3':
                technics[typ].append(Copier(input('Enter name of your copier: ')))
            else:
                print('Wrong command')
        elif inp == store.commands[len(store.commands)-1]:
            store.user_cmd(technics['1'], inp, '')
        elif inp in store.commands[:len(store.commands)-1]:
            name_dep = ''
            if inp == store.commands[1]:
                name_dep = input('Enter destination department: ')
            typ = input('Enter type of technics (1 - printer, 2 - scanner, 3 - copier): ')
            if typ in technics.keys():
                store.user_cmd(technics[typ], inp, name_dep)
        elif not inp:
            break
        else:
            print('Wrong command')

