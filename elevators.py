import random

class House:
    def __init__(self, address, floors, elevators):
        self.address = address
        self.floors = floors
        self.elevators = elevators
  
class Elevator:
    def __init__(self, capacity, current_floor, direction, destination):
        self.capacity = capacity
        self.current_floor = current_floor
        self.direction = direction
        self.destination = destination
        self.doors = False

class Operator:
    def elevator_info(self, elevator):
        if elevator.direction == "не двигается":
            print(f"Информация о лифте: вместимость - {elevator.capacity}, текущий этаж - {elevator.current_floor}, направление движения - {elevator.direction}")
            print(f"Двери заблокированы: {elevator.doors}")
        else:
            print(f"Информация о лифте: вместимость - {elevator.capacity}, направление движения - {elevator.direction}, назначенный этаж - {elevator.destination}")
            print(f"Лифт добрался до назначенного этажа {elevator.current_floor}")
            elevator.direction = "не двигается"   

    def send_elevator_to_floor(self, elevator, floor):
        if elevator.doors == True:
            print("Чтобы отправить лифт на другой этаж, разблокируйте двери")
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
    
    def elevator_stop(self, elevator):
        if elevator.direction == "не двигается":
            print("Лифт и так стоит на месте.")
        else:
            elevator.current_floor = random.randint(elevator.start_floor, elevator.destination)
            elevator.direction = "не двигается"
            print(f"Лифт экстренно остановлен на этаже {elevator.current_floor}")


    def unblock_doors(self, elevator):
        elevator.doors = False
        print("Двери разблокированы")
      

    def block_doors(self, elevator):
        elevator.doors = True
        elevator.direction = "не двигается"
        print("Двери заблокированы")





house1 = House("Шейкмана, 69", 25, 2)
house2 = House("Ленина, 40", 9, 1)
house3 = House("Пушкина, 1", 12, 3)


elevator1 = Elevator(1000, 1, "не двигается", 1)
elevator2 = Elevator(800, 1, "не двигается", 1)
elevator3 = Elevator(1200, 1, "не двигается", 1)


operator = Operator()

operator.elevator_info(elevator1)
operator.send_elevator_to_floor(elevator1, 5)
operator.elevator_stop(elevator1)
operator.elevator_info(elevator1)
operator.elevator_info(elevator1)
print()

operator.block_doors(elevator1)
operator.send_elevator_to_floor(elevator1, 6)
operator.elevator_info(elevator1)
print()

operator.unblock_doors(elevator1)
operator.elevator_info(elevator1)
operator.send_elevator_to_floor(elevator1, 1)
operator.elevator_info(elevator1)

