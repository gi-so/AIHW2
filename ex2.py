import time
import random

ids = ["935885178", "203609177"]

def neighbors_value_sum(state, row, col):
    count=0.0
    ghost_count=0.0
    if state[row][col] == 11:
        count += 1
    if state[row+1][col] == 11:
        count += 1
    if state[row][col+1] == 11:
        count += 1
    if state[row-1][col] == 11:
        count += 1
    if state[row][col-1] == 11:
        count += 1
    if state[row + 1][col] in (51, 50, 41, 40, 31, 30, 21, 20):
        ghost_count += 1
    if state[row][col + 1] in (51, 50, 41, 40, 31, 30, 21, 20):
        ghost_count += 1
    if state[row - 1][col] in (51, 50, 41, 40, 31, 30, 21, 20):
        ghost_count += 1
    if state[row][col - 1] in (51, 50, 41, 40, 31, 30, 21, 20):
        ghost_count += 1
    ghost_factor=100*ghost_count
    return (count - ghost_factor)



def count_dots(state):
    sum = 0
    for row in state:
        for col in row:
            if state[state.index(row)][row.index(col)] == (11 or 71 or 51 or 41 or 31 or 21):
                sum = sum + 1
    return sum

def find_pacman(state):
    p_row = 0
    p_col = 0
    for row in state:
        for col in row:
            if state[state.index(row)][row.index(col)] == 66:
                p_row = state.index(row)
                p_col = row.index(col)
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


    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a tuple, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        allowed_lst = []
        packman_row, packman_col = find_pacman(state)
        allowed_field = (10,11)



        if state[packman_row + 1][packman_col] in allowed_field:
            allowed_lst.append("D")
        if state[packman_row - 1][packman_col] in allowed_field:
            allowed_lst.append("U")
        if state[packman_row][packman_col + 1] in allowed_field:
            allowed_lst.append("R")
        if state[packman_row][packman_col - 1] in allowed_field:
            allowed_lst.append("L")

        return tuple(allowed_lst)


    def choose_next_action(self, state):
        """Choose next action for pacman controller given the current state.
        Action should be returned in the format described previous parts of the project.
        This method MUST terminate within the specified timeout."""
        # print('COMPLETE choose_next_action')

        allowed_lst = []
        allowed_lst = self.actions(state)
        if not allowed_lst:
            return "reset"
        pacman_row, pacman_col = find_pacman(state)
        value = -100
        action = None
        for act in allowed_lst:
            if act == "R":
                tmp_value = neighbors_value_sum(state,pacman_row,pacman_col + 1)

            if act == "D":
                tmp_value = neighbors_value_sum(state, pacman_row + 1, pacman_col)

            if act == "L":
                tmp_value = neighbors_value_sum(state, pacman_row, pacman_col - 1)

            if act == "U":
                tmp_value = neighbors_value_sum(state, pacman_row - 1, pacman_col)
            if tmp_value>=value:
                value = tmp_value
                action = act
        #action = random.choice(allowed_lst)
        return action