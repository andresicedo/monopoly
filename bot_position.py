class Bot_position:
    def bot_current(self):
        bot_current_position = 0
        if bot_current_position > 44:
            bot_current_position -= 44
            return bot_current_position