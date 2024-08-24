class Bus:
    def __init__(self, speed=0, max_passengers=50, max_speed=100):
        self.speed = speed
        self.max_passengers = max_passengers
        self.max_speed = max_speed
        self.passenger_list = []
        self.has_free_seats = True
        self.seats = {i: None for i in range(1, max_passengers + 1)}

    def board(self, surnames):
        if isinstance(surnames, str):
            surnames = [surnames]
        for surname in surnames:
            if len(self.passenger_list) < self.max_passengers:
                self.passenger_list.append(surname)
                for seat_number in self.seats:
                    if self.seats[seat_number] is None:
                        self.seats[seat_number] = surname
                        break
                if len(self.passenger_list) == self.max_passengers:
                    self.has_free_seats = False
            else:
                print("Нет свободных мест!")

    def alight(self, surnames):
        if isinstance(surnames, str):
            surnames = [surnames]
        for surname in surnames:
            if surname in self.passenger_list:
                self.passenger_list.remove(surname)
                for seat_number, occupant in self.seats.items():
                    if occupant == surname:
                        self.seats[seat_number] = None
                        break
                self.has_free_seats = True
            else:
                print(f"Пассажир {surname} не найден!")

    def increase_speed(self, increment):
        self.speed = min(self.speed + increment, self.max_speed)

    def decrease_speed(self, decrement):
        self.speed = max(self.speed - decrement, 0)

    def __contains__(self, surname):
        return surname in self.passenger_list

    def __iadd__(self, surname):
        self.board(surname)
        return self

    def __isub__(self, surname):
        self.alight(surname)
        return self

    def __str__(self):
        return (f"Скорость: {self.speed} км/ч, "
                f"Максимальное количество мест: {self.max_passengers}, "
                f"Максимальная скорость: {self.max_speed} км/ч, "
                f"Пассажиры: {', '.join(self.passenger_list)}, "
                f"Свободные места: {self.has_free_seats}")

bus = Bus(speed=60, max_passengers=3, max_speed=100)
bus += "Иванов"
bus += "Петров"
print(bus)
bus -= "Иванов"
print(bus)
bus.board(["Сидоров", "Кузнецов"])
print(bus)
bus.increase_speed(20)
print(bus)
bus.decrease_speed(30)
print(bus)
