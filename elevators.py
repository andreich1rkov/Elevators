import random

# Класс House включает: адресс, кол-во этажей, кол-во лифтов
class House:
    def __init__(self, address, floors, elevators):
        self.address = address
        self.floors = floors
        self.elevators = elevators
    def house_info(house):
        print(f"Дом находится по адресу: {house.address}, Кол-во этажей: {house.floors}, Кол-во лифтов: {house.elevators}")
  
# Класс Elevator включает: вместимость(грузоподъемность), текущий этаж, направление движения, этаж назначения, состояние дверей (заблок./разблок.) 
class Elevator:
    def __init__(self, capacity, current_floor, direction, destination):
        self.capacity = capacity
        self.current_floor = current_floor
        self.direction = direction
        self.destination = destination
        self.doors = False
    
    def elevator_info(elevator):
        if elevator.direction == "не двигается":
            print(f"Информация о лифте: вместимость - {elevator.capacity}, текущий этаж - {elevator.current_floor}, направление движения - {elevator.direction}")
            print(f"Двери заблокированы: {elevator.doors}")
            print()
        else:
            print(f"Информация о лифте: вместимость - {elevator.capacity}, направление движения - {elevator.direction}, назначенный этаж - {elevator.destination}")
            print(f"Лифт добрался до назначенного этажа {elevator.current_floor}")
            print()
            elevator.direction = "не двигается"   

# Класс Operator включает: функцию отображения состояния лифта, функции управления лифтом (отправление на этаж, управление дверьми, экстренная остановка лифта)
class Operator:
    def send_elevator_to_floor(elevator, floor):
        if elevator.doors == True:
            print("Чтобы отправить лифт на другой этаж, разблокируйте двери")
            print()
            return

        if floor > elevator.current_floor:
            elevator.direction = "вверх"
        elif floor < elevator.current_floor:
            elevator.direction = "вниз"
        else:
            elevator.direction = "не двигается"
        elevator.start_floor = elevator.current_floor
        elevator.current_floor = floor
        elevator.destination = floor
        print(f"Отправляем лифт на этаж № {floor}")
        print()
    
    def elevator_stop(elevator):
        if elevator.direction == "не двигается":
            print("Лифт и так стоит на месте.")
            print()
        else:
            elevator.current_floor = random.randint(elevator.start_floor, elevator.destination)
            elevator.direction = "не двигается"
            print(f"Лифт экстренно остановлен на этаже {elevator.current_floor}")
            print()


    def unblock_doors(elevator):
        elevator.doors = False
        print(f"Двери лифта разблокированы")
        print()
      

    def block_doors(elevator):
        elevator.doors = True
        print(f"Двери лифта заблокированы")
        print()

operator = Operator

# Создаем экземпляры лифтов
elevator1 = Elevator(10, 1, "не двигается", 1)
elevator2 = Elevator(8, 1, "не двигается", 1)
elevator3 = Elevator(4, 1, "не двигается", 1)
elevator4 = Elevator(6, 1, "не двигается", 1)

# Создаем три экземпляра дома
house1 = House("Мира, 40", 10, [elevator1])
house2 = House("Ленина, 69", 8, [elevator2])
house3 = House("Шейкмана, 33", 12, [elevator3, elevator4])

print("Добро пожаловать в программу, моделирующую работу оператора лифтов.")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

while True:
    print("К какому дому обратиться: Мира, 40; Ленина, 69; Шейкмана, 33?")
    n = int(input("Введите соответсвенно 1, 2 или 3: "))

    if n == 1:
        print(f"Информация о доме: {house1.house_info()} ")                             # Error
        while True:
            print("Информация о лифте - 1")
            print("Отправить лифт на этаж - 2")
            print("Остановка лифта - 3")
            print("Заблокировать/разблокировать двери 4")
            print("Выбрать другой дом - 5")
            x = int(input())
            print()
            if x == 1:
                elevator1.elevator_info()  
            elif x == 2:
                m = int(input("на какой этаж (1-10) отправить лифт: "))
                operator.send_elevator_to_floor(elevator1, m)
            elif x == 3:
                operator.elevator_stop(elevator1)
            elif x == 4:
                if elevator1.doors == True:  
                    operator.unblock_doors(elevator1)
                else:
                    operator.block_doors(elevator1)
            elif x == 5:
                break

    elif n == 2:
        print(f"Информация о доме: {house2.house_info()} ")                             # Error
        while True:
            print("Информация о лифте - 1")
            print("Отправить лифт на этаж - 2")
            print("Остановка лифта - 3")
            print("Заблокировать/разблокировать двери 4")
            print("Выбрать другой дом - 5")
            x = int(input())
            print()
            if x == 1:
                elevator2.elevator_info()  
            elif x == 2:
                m = int(input("на какой этаж (1-8) отправить лифт: "))
                operator.send_elevator_to_floor(elevator2, m)
            elif x == 3:
                operator.elevator_stop(elevator2)
            elif x == 4:
                if elevator2.doors == True:  
                    operator.unblock_doors(elevator2)
                else:
                    operator.block_doors(elevator2)
            elif x == 5:
                break
        
    elif n == 4:
        break