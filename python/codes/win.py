

from tkinter import *
from tkinter import messagebox
from tkinter_label import Get_label


class Win:
    def __init__(self):
        self.win = Tk()
        self.win.title("틀린 그림 찾기")
        # self.win.iconbitmap() > 아이콘
        self.win.geometry("1300x700")
        def callback(e):
            x = e.x
            y = e.y
            print("Pointer is currently at %d, %d" %(x,y))
        self.win.bind('<Button 1>',callback)
        self.main_menu()
        self.win.mainloop()
    
    def main_menu(self):
        Main_menu_background = Get_label.image_label(
            self.win, "main_menu_bg.png", 0, 0
        )
        Start_btn = Get_label.image_button(
            self.win,
            "start_btn.png",
            860,
            360,
            lambda: self.intro(),
        )
        End_btn = Get_label.image_button(
            self.win,
            "end_btn.png",
            1065,
            360,
            lambda: self._quit(),
        )
    
    def intro(self):
        pass
    
    def game(self):
        pass
    
    def gameover(self):
        pass
    
    def gameclear(self):
        pass
    
    
    
    
    
    def _quit(self):
        answer = messagebox.askyesno("확인", "정말 종료하시겠습니까?")
        if answer == True:
            self.win.quit()
            self.win.destroy()
            exit()

game_start = Win()