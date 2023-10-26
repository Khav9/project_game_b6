import tkinter as tk
from tkinter import *
from PIL import Image , ImageTk
import winsound
import random
from random import randrange

#-_____________________________________CONSTANT_________________________________________

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 740
root = tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
root.title('Super runner')
canvas = tk.Canvas(root)
#-------------------
GRAVITY_FORCE = 9
JUMP_FORCE = 30
SPEED = 15
TIMED_LOOP = 10

# _________________________________________Images______________________________

icon = tk.PhotoImage(file='image/hero.png')
root.iconphoto(True,icon)
root.resizable(0,0)

game_play = tk.PhotoImage(file="image/background.png")
game_level2 = tk.PhotoImage(file="image/background_l2.png")
game_level3 = tk.PhotoImage(file="image/background_l3.png")

game_start = tk.PhotoImage(file="image/game_start.png")
win_page = tk.PhotoImage(file="image/win_page.png")
game_help = tk.PhotoImage(file="image/help.png")
game_over = tk.PhotoImage(file="image/game_over.png")
#_________Scrolling image background________
original_image = Image.open("image/background_l3.png")
image_resize = original_image.resize((SCREEN_WIDTH, SCREEN_HEIGHT))
background_image = ImageTk.PhotoImage(image_resize)
sum_score = tk.PhotoImage(file="image/total_score.png")
#__________hero________
hero = tk.PhotoImage(file="image/hero.png")
hero_left = tk.PhotoImage(file="image/hero_left.png")

#_______________
cash_img = tk.PhotoImage(file="image/cash.png")
heard = tk.PhotoImage(file="image/heard.png")
heard_black = tk.PhotoImage(file="image/heard_black.png")

btn_start_game = tk.PhotoImage(file="image/btn_start_game.png")
btn_exit_game = tk.PhotoImage(file="image/btn_exit_game.png")
btn_help_game = tk.PhotoImage(file="image/btn_help_game.png")
btn_back = tk.PhotoImage(file="image/btn_back.png")
btn_back_new = tk.PhotoImage(file="image/back.png")
btn_back_win = tk.PhotoImage(file="image/back_win.png")
btn_replay = tk.PhotoImage(file="image/btn_replay.png")
btn_retry = tk.PhotoImage(file="image/btn_retry.png")
btn_exit_lp = tk.PhotoImage(file="image/btn_exit_lp.png")
btn_next_level = tk.PhotoImage(file="image/next_level.png")

boom_file = Image.open("image/bom.png")
boom_size = boom_file.resize((60, 60))
boom_img = ImageTk.PhotoImage(boom_size)
fire_image = tk.PhotoImage(file="image/fire.png")

#friuts____________________________
apple_img = tk.PhotoImage(file='image/apple.png')
bery_img = tk.PhotoImage(file='image/bery.png')
chery_img = tk.PhotoImage(file='image/chery.png')
mango_img = tk.PhotoImage(file='image/mango.png')

fruits = [apple_img, bery_img, chery_img, mango_img]
#___live___

heard = tk.PhotoImage(file="image/heard.png")
heard_white_img = tk.PhotoImage(file="image/heard_white.png")

#______btn-level_______

level_page = tk.PhotoImage(file='image/levels_page.png')
btn_level1 = tk.PhotoImage(file='image/btn_level1.png')
btn_level2 = tk.PhotoImage(file='image/btn_level2.png')
btn_level3 = tk.PhotoImage(file='image/btn_level3.png')
#___________________________
way_player =tk.PhotoImage(file='image/road.png')
way_player_l2 =tk.PhotoImage(file='image/road_l2.png')
way_player_l3 =tk.PhotoImage(file='image/road_l3.png')
way_car =tk.PhotoImage(file='image/car.png')
parash =tk.PhotoImage(file='image/parash.png')

#_______________________________Variable_____________________________________

player_X = 150
player_Y = 360
enamy_x = 1400
listOfLives = []
listOfCash = []
listOfBom = []
canLive = 6
toConfig = 0
totalCash = 0
totalBom = 0
isStart = True

count_create_fruit = 0
count_create_bom = 0
keyPressed = []
# ______________________________ Game Process _________________________________
def processGame():  
    if totalCash > 100 :
        win_game()
    if totalBom > 5:
        gameOver()
    canvas.after(100, processGame)

# ____________________________________ Game Show ______________________________________
def gameShow(event):
    canvas.delete("all")
    canvas.create_image(680, 372, image=game_start)
    canvas.create_image(680,280, image=btn_start_game, tags="startgame")
    canvas.create_image(680,410,image=btn_exit_game, tags="exit")
    canvas.create_image(680,540,image=btn_help_game, tags="help")
    
#__________________Chose levels______________________

def chose_levels(event):
    global player_X,player_Y,canLive,toConfig,totalCash,totalBom,isStart,listOfLives,listOfCash,listOfBom,player,displayTotalCash
    isStart = True
    player_X = 150
    player_Y = 450
    canLive = 6
    toConfig = 0
    totalCash = 0
    totalBom = 0
    listOfLives = []
    listOfCash = []
    listOfBom = []
    canvas.delete("all")
    # interface page level
    canvas.create_image(680, 372, image=level_page)
    canvas.create_image(1250,70,image=btn_exit_lp, tags="exit")
    canvas.create_image(140, 70, image=btn_back, tags="back_to_show_game")
    #chose
    canvas.create_image(680,250,image=btn_level1, tags="level_1")
    canvas.create_image(680,400,image=btn_level2, tags="level_2")
    canvas.create_image(680,550,image=btn_level3, tags="level_3")

# ___________________________________ Game Start_________________________________

def level_one(event):
    global player, displayTotalCash,totalCash
    canvas.delete("all")
    canvas.create_image(680, 372,  image=game_play)
    player = canvas.create_image(player_X, player_Y, image=hero)
    canvas.create_image(150, 780, image=way_player,tags="PLATFORM")
    canvas.create_image(700, 780, image=way_player,tags="PLATFORM")
    displayTotalCash = canvas.create_text(1200, 75, text=totalCash, font=("serif", 18 ,'bold'), fill="black")
    for i in range(6):
        lives = canvas.create_image(80 + i * 100, 70, image=heard)
        listOfLives.append(lives)
    create_fruit()
    create_bom()
    gravity()
    winsound.PlaySound("sound/start.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)