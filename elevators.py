class House:
    def __init__(self, address, floors, elevators):
        self.address = address
        self.floors = floors
        self.elevators = elevators
  
class Elevator:
    def __init__(self, capacity, current_floor, direction, destination, load):
        self.capacity = capacity
        self.current_floor = current_floor
        self.direction = direction
        self.destination = destination
        self.load = load
    def display_info(self):
        return f"Информация о лифте: вместимость - {self.capacity}, текущий этаж - {self.current_floor}, направление движения - {self.direction}, назначенный этаж - {self.destination}, загрузка - {self.load}"

class Operator:
    def track_elevator_position(self, elevator):
        print(f"Лифт находится на этаже № {elevator.current_floor}")

    def send_elevator_to_floor(self, elevator, floor):
        if floor > elevator.current_floor:
            elevator.direction = "вверх"
        elif floor < elevator.current_floor:
            elevator.direction = "вниз"
        else:
            elevator.direction = "stationary"
        elevator.current_floor = floor
        print(f"Отправляем лифт на этаж № {floor}")




house1 = House("Шейкмана, 69", 25, 2)
house2 = House("Ленина, 40", 9, 1)
house3 = House("Пушкина, 1", 12, 3)


elevator1 = Elevator(1000, 1, "stationary", 0, 0)
elevator2 = Elevator(800, 1, "stationary", 0, 0)
elevator3 = Elevator(1200, 1, "stationary", 0, 0)
print(elevator1.display_info())


operator = Operator()


operator.track_elevator_position(elevator1)
operator.send_elevator_to_floor(elevator1, 5)
operator.track_elevator_position(elevator1)

operator.track_elevator_position(elevator2)
operator.send_elevator_to_floor(elevator2, 3)
operator.track_elevator_position(elevator2)

operator.track_elevator_position(elevator3)
operator.send_elevator_to_floor(elevator3, 8)
operator.track_elevator_position(elevator3)

