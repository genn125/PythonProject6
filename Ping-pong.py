import arcade


SCREEN_WIDTH = 1200  # ширина
SCREEN_HEIGHT = 600  # высота
SCREEN_TITLE = "Игра Пинг-Понг"  # заголовок

class Game(arcade.Window):

    def on_draw(self):     # отображение элементов на графическом окне
        self. clear((200,200,200))   #  интенсивности каналов RGB






if __name__ == '__main__':

    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()  #  графическое окно