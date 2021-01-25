from turn import Turn
class Bot_position:
    def bot_current(self, turn: Turn):
        bot_current_position = turn.bot_roll_history[-1] + turn.bot_roll_history[-2]
        if bot_current_position > 44:
            bot_current_position -= 44
        return bot_current_position