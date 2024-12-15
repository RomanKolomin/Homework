from os import times_result


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

# Переделал исходя из времени прохождения трассы
    def start(self):
        finishers = {}
        time_results = {}
        for participant in self.participants:
            time_results.update({(self.full_distance / participant.speed): participant})
        place = 1
        while len(time_results) > 0:
            participant = time_results[min(time_results)]
            finishers.update({place: participant})
            place += 1
            del time_results[min(time_results)]
        return finishers
