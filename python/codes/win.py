import random
import threading
import os
import time
from tkinter import *
from tkinter import messagebox
from tkinter_label import Get_label
from playsound import playsound
from PIL import Image

"""
im1 = Image.open(r"./testimg.png")
print(im1.getpixel((0,0)))
"""

img_path = os.path.join(os.getcwd(), "../../images")


class Win:
    def __init__(self):
        self.win = Tk()
        self.win.title("틀린 그림 찾기")
        # self.win.iconbitmap() > 아이콘
        self.win.geometry("1300x700")
        self.bind = False

        music_thread = threading.Thread(target=self.main_music)
        music_thread.daemon = True
        music_thread.start()

        self.main_menu()
        self.win.mainloop()

    def main_music(self):
        while True:
            playsound("../../musics/peppermint.mp3")
            time.sleep(1)

    def random_stage(self):
        self.stages = [i for i in range(1, 25)]
        random.shuffle(self.stages)
        self.stages.append(25)
        self.orders = []

    def main_menu(self):
        self.bind = False
        self.random_stage()
        self.stage_num = 0
        self.life = 5
        Main_menu_background = Get_label.image_label(
            self.win, "background/main_menu_bg.png", 0, 0
        )
        Start_btn = Get_label.image_button(
            self.win,
            "button/start_btn.png",
            860,
            360,
            lambda: self.intro(),
        )
        End_btn = Get_label.image_button(
            self.win,
            "button/end_btn.png",
            1065,
            360,
            lambda: self._quit(),
        )

    def intro(self):
        self.bind = False
        Intro_background = Get_label.image_label(
            self.win, "background/intro_bg.png", 0, 0
        )
        Start_btn = Get_label.image_button(
            self.win,
            "button/start_btn.png",
            545,
            605,
            lambda: self.next_game(),
        )

    def next_game(self):
        if self.orders:
            self.order = self.orders.pop(0)
        else:
            self.stage_num += 1
            self.stage = self.stages.pop(0)
            self.orders = [1, 2]
            random.shuffle(self.orders)
            self.order = self.orders.pop(0)
        self.game()

    def game(self):
        print(self.stages)
        print(len(self.stages))
        self.win.bind("<Button 1>", self.callback)
        self.bind = True
        Game_background = Get_label.image_label(
            self.win, "background/game_bg.png", 0, 0
        )
        Stage_label = Get_label.image_label_text(
            self.win,
            "label/stage_label.png",
            75,
            25,
            f"STAGE {self.stage_num}",
            "White",
            ("Algerian", 40),
        )
        Life_label = Get_label.image_label_text(
            self.win,
            "label/life_label.png",
            680,
            25,
            "LIFE " + "♡" * (5 - self.life) + "♥" * (self.life),
            "White",
            ("Algerian", 40),
        )
        self.Photo1_label = Get_label.image_label(
            self.win, f"original/original{self.stage}.png", 73, 121
        )
        self.Photo2_label = Get_label.image_label(
            self.win,
            f"change{self.order}/change{self.stage}-{self.order}.png",
            678,
            121,
        )

    def callback(self, pointer):
        x = pointer.x
        y = pointer.y
        if self.bind:
            image1 = Image.open(
                os.path.join(img_path, f"original/original{self.stage}.png")
            )
            image2 = Image.open(
                os.path.join(
                    img_path, f"change{self.order}/change{self.stage}-{self.order}.png"
                )
            )
            image1_color = image1.getpixel((x, y))
            image2_color = image2.getpixel((x, y))
            if (
                image1_color[0] == image2_color[0]
                and image1_color[1] == image2_color[1]
                and image1_color[2] == image2_color[2]
            ):
                self.life -= 1
                if self.life <= 0:
                    self.gameover()
                else:
                    self.wrong()
            else:
                self.correct()

    def correct(self):
        playsound("../../musics/correct.mp3")
        self.Photo1_label.destroy()
        self.Photo2_label.destroy()
        self.win.after(200, self.next_game)

    def wrong(self):
        playsound("../../musics/wrong.mp3")
        self.game()

    def gameover(self):
        self.bind = False
        playsound("../../musics/wrong.mp3")
        Gameover_background = Get_label.image_label(
            self.win, "background/gameover_bg.png", 0, 0
        )
        Retart_btn = Get_label.image_button(
            self.win,
            "button/restart_btn.png",
            565,
            525,
            lambda: self.main_menu(),
        )

    def gameclear(self):
        self.bind = False
        Gameclear_background = Get_label.image_label(
            self.win, "background/gameclear_bg.png", 0, 0
        )
        Score_label = Get_label.image_label_text(
            self.win,
            "label/score_label.png",
            530,
            475,
            f"기록 : XXX초",
            "White",
            ("HY나무M", 18),
        )
        Reset_btn = Get_label.image_button(
            self.win,
            "button/reset_btn.png",
            555,
            555,
            lambda: self.main_menu(),
        )

    def _quit(self):
        answer = messagebox.askyesno("확인", "정말 종료하시겠습니까?")
        if answer == True:
            self.win.quit()
            self.win.destroy()
            exit()


game_start = Win()
