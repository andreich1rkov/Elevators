import random

# Класс House включает: адресс, кол-во этажей, кол-во лифтов
class House:
    def __init__(self, address, floors, elevators):
        self.address = address
        self.floors = floors
        self.elevators = elevators
  
# Класс Elevator включает: вместимость(грузоподъемность), текущий этаж, направление движения, этаж назначения, состояние дверей (заблок./разблок.) 
class Elevator:
    def __init__(self, capacity, current_floor, direction, destination):
        self.capacity = capacity
        self.current_floor = current_floor
        self.direction = direction
        self.destination = destination
        self.doors = False

# Класс Operator включает: функцию отображения состояния лифта, функции управления лифтом (отправление на этаж, управление дверьми, экстренная остановка лифта)
class Operator:
    def elevator_info(self, elevator):
        if elevator.direction == "не двигается":
            print(f"Информация о лифте: вместимость - {elevator.capacity}, текущий этаж - {elevator.current_floor}, направление движения - {elevator.direction}")
            print(f"Двери заблокированы: {elevator.doors}")
            print()
        else:
            print(f"Информация о лифте: вместимость - {elevator.capacity}, направление движения - {elevator.direction}, назначенный этаж - {elevator.destination}")
            print(f"Лифт добрался до назначенного этажа {elevator.current_floor}")
            print()
            elevator.direction = "не двигается"   

    def send_elevator_to_floor(self, elevator, floor):
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
    
    def elevator_stop(self, elevator):
        if elevator.direction == "не двигается":
            print("Лифт и так стоит на месте.")
            print()
        else:
            elevator.current_floor = random.randint(elevator.start_floor, elevator.destination)
            elevator.direction = "не двигается"
            print(f"Лифт экстренно остановлен на этаже {elevator.current_floor}")
            print()


    def unblock_doors(self, elevator):
        elevator.doors = False
        print("Двери разблокированы")
        print()
      

    def block_doors(self, elevator):
        elevator.doors = True
        print("Двери заблокированы")
        print()






import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.quit_button = tk.Button(self, text="Quit", command=self.master.destroy)
        self.quit_button.pack(side="bottom")

        self.context_menu = tk.Menu(self, tearoff=0)
        self.context_menu.add_command(label="Отобразить информацию о лифте", command=self.show_elevator_info)
        self.context_menu.add_command(label="Отправить лифт на этаж", command=self.send_elevator)

        self.bind_context_menu(self.quit_button)

    def show_context_menu(self, event):
        self.context_menu.post(event.x_root, event.y_root)
    
    def bind_context_menu(self, widget):
        widget.bind("<Button-3>", self.show_context_menu)

    def show_elevator_info(self):
        pass# Ваш код для отображения информации о лифте

    def send_elevator(self):
        pass# Ваш код для отправки лифта на этаж

root = tk.Tk()
app = Application(master=root)
app.mainloop()