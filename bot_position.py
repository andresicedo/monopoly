class Bot_Position:
    bot_location = 0
    def bot_position(self, bot_location):
        if bot_location > 44:
            bot_location -= 44
        return bot_location