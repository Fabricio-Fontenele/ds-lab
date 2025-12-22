import random


class Gym:
    def __init__(self):
        self.dumbbells = [
            i for i in range(10, 36) if i % 2 == 0
        ]  # Halteres de 10kg a 35kg, apenas pares
        self.dumbbell_rack = {}
        self.start_new_day()

    def start_new_day(self):
        self.dumbbell_rack = {i: i for i in self.dumbbells}

    def list_active_dumbbells(self):
        return [i for i in self.dumbbell_rack.values() if i != 0]

    def listar_espacos(self):
        return [i for i, j in self.dumbbell_rack.items() if j == 0]

    def get_dumbbell(self, weight):
        dumbbell_index = list(self.dumbbell_rack.values()).index(weight)
        dumbbell_key = list(self.dumbbell_rack.keys())[dumbbell_index]
        self.dumbbell_rack[dumbbell_key] = 0
        return weight

    def return_dumbbell(self, index, peso):
        self.dumbbell_rack[index] = peso

    def evaluate_rack_discrepancy(self):
        discrepant_dumbbells = [i for i, j in self.dumbbell_rack.items() if i != j]
        return len(discrepant_dumbbells) / len(self.dumbbell_rack)


class User:
    def __init__(self, membership_type, gym: Gym):
        self.membership_type = membership_type
        self.gym = gym
        self.current_weight = 0

    def start_training(self):
        dumbbell_options = self.gym.list_active_dumbbells()
        self.current_weight = random.choice(dumbbell_options)
        self.gym.get_dumbbell(self.current_weight)

    def stop_training(self):
        active_dumbbells = self.gym.listar_espacos()

        if self.membership_type == 1:
            if self.current_weight in active_dumbbells:
                self.gym.return_dumbbell(self.current_weight, self.current_weight)
            else:
                index = random.choice(active_dumbbells)
                self.gym.return_dumbbell(index, self.current_weight)

        if self.membership_type == 2:
            index = random.choice(active_dumbbells)
            self.gym.return_dumbbell(index, self.current_weight)
        self.peso = 0


gym1 = Gym()

users = [User(1, gym1) for i in range(10)]
users += [User(2, gym1) for i in range(1)]
random.shuffle(users)

for i in range(10):
    random.shuffle(users)
    for user in users:
        user.start_training()
    for user in users:
        user.stop_training()

gym1.dumbbell_rack
print(gym1.evaluate_rack_discrepancy())
