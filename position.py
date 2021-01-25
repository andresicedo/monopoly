class Position:
    def current(self):
        current_position = 0
        if current_position > 44:
            current_position -= 44
            return current_position
        