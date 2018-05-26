import time
import random

ids = ["935885178", "203609177"]


def count_dots(state):
    sum = 0
    for row in state:
        for col in row:
            if state[row][col] == (11 or 71 or 51 or 41 or 31 or 21):
                sum = sum + 1
    return sum

def find_pacman(state):
    p_row = 0
    p_col = 0
    sum = 0
    for row in state:
        for col in row:
            if state[row][col] == 66:
                p_row = row
                p_col = col
    return p_row, p_col

class PacmanController:
    """This class is a controller for a pacman agent."""

    def __init__(self, state, steps):
        """Initialize controller for given the initial setting.
        This method MUST terminate within the specified timeout."""
        # print('COMPLETE init ')
        self.state = state
        self.steps = steps
        self.dot_sum = count_dots(state)
        self.pacman_row, self.pacman_col = find_pacman(state)

    def choose_next_action(self, state):
        """Choose next action for pacman controller given the current state.
        Action should be returned in the format described previous parts of the project.
        This method MUST terminate within the specified timeout."""
        # print('COMPLETE choose_next_action')

        dots = count_dots(state)
        r0 = self.dot_sum - dots
        discount = 0.9
        actions = ["R","D","L","U"]
        policy = {}

        for i in actions:
            tmp_steps = 1
            v = []
            v.append(r0)
            while tmp_steps <= self.steps:
                r_action = v[tmp_steps - 1] + discount *
                v[tmp_steps] = v[tmp_steps - 1] + max()
                tmp_steps = tmp_steps + 1







