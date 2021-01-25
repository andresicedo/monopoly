# from turn import Turn
class Position:
    def current(self, turn):
        current_position = turn.roll_history[-1] + turn.roll_history[-2]
        if current_position > 44:
            current_position -= 44
        return current_position
        