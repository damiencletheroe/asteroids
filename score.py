from constants import ASTEROID_MIN_RADIUS

class Score:
    POINTS_VALUES = {
        1: 1000,    # small asteroid
        2: 500,     # medium asteroid
        3: 20       # large asteroid
    }
    def __init__(self):
        self.current_score = 0

    def calculate_points(self, asteroid):
        size = asteroid.radius // ASTEROID_MIN_RADIUS
        return self.POINTS_VALUES[size]

    def add_points(self, asteroid):
        points = self.calculate_points(asteroid)
        self.current_score += points