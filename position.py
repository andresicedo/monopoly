class Position:
    location = 0
    def position(self, location):
        if location > 44:
            location -= 44
        return location
    