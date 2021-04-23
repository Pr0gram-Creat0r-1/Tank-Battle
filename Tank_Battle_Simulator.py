import time
import random
from tkinter import *
import winsound
from pygame import mixer
mixer.init()
randlist=['simpleattack', 'simpleattack', 'simpleattack', 'point', 'destructo_attack', 'shield', 'deactivate_shield', 'moveleft', 'moveright', 'moveup', 'movedown', 'trackplayer']
is_shield=0
tk=Tk()
tk.title('Tank Battle Simulator')
tk.resizable(0, 0)
canvas=Canvas(tk, width=800, height=800)
canvas.pack()
battleground=canvas.create_rectangle(0, 0, 800, 800, fill='yellow', outline='')
player_body=canvas.create_rectangle(25, 390, 75, 405, fill='blue', outline='')
player_back_wheel=canvas.create_oval(25, 400, 37.5, 412.5, fill='dark gray', outline='')
player_front_wheel=canvas.create_oval(62.5, 400, 75, 412.5, fill='dark gray', outline='')
player_parallel_neck=canvas.create_polygon(52.5, 390, 57.5, 375, 52.5, 375, 47.5, 390, fill='yellow', outline='')
player_neck=canvas.create_polygon(47.5, 390, 37.5, 375, 42.5, 375, 52.5, 390, fill='blue', outline='')
player_parallel_head=canvas.create_polygon(65, 380, 42.5, 380, 42.5, 375, 30, 375, 30, 372, 42.5, 372, 42.5, 370, 65, 370, 65, 380, fill='yellow', outline='')
player_head=canvas.create_polygon(35, 380, 57.5, 380, 57.5, 375, 70, 375, 70, 372, 57.5, 372, 57.5, 370, 35, 370, 35, 380, fill='blue', outline='')
player_antenna=canvas.create_polygon(40, 370, 37.5, 362.5, 40, 362.5, 42.5, 370, fill='blue', outline='')
player_parallel_antenna=canvas.create_polygon(60, 370, 62.5, 362.5, 60, 362.5, 57.5, 370, fill='yellow', outline='')
player_shield=canvas.create_polygon(80, 370, 85, 370, 87.5, 390, 85, 410, 80, 410, 82.5, 390, 70, 390, 70, 385, 82.5, 385, 80, 370, fill='yellow', outline='')
player_parallel_shield=canvas.create_polygon(20, 370, 15, 370, 12.5, 390, 15, 410, 20, 410, 17.5, 390, 30, 390, 30, 385, 17.5, 385, 20, 370, fill='yellow', outline='')
enemy_body=canvas.create_rectangle(725, 390, 775, 405, fill='red', outline='')
enemy_back_wheel=canvas.create_oval(725, 400, 737.5, 412.5, fill='dark gray', outline='')
enemy_front_wheel=canvas.create_oval(762.5, 400, 775, 412.5, fill='dark gray', outline='')
enemy_parallel_neck=canvas.create_polygon(747.5, 390, 737.5, 375, 742.5, 375, 752.5, 390, fill='yellow', outline='')
enemy_parallel_head=canvas.create_polygon(735, 380, 757.5, 380, 757.5, 375, 770, 375, 770, 372, 757.5, 372, 757.5, 370, 735, 370, 735, 380, fill='yellow', outline='')
enemy_parallel_antenna=canvas.create_polygon(740, 370, 737.5, 362.5, 737.5, 362.5, 742.5, 370, fill='yellow', outline='')
enemy_neck=canvas.create_polygon(762.5, 375, 752.5, 390, 747.5, 390, 757.5, 375, fill='red', outline='')
enemy_head=canvas.create_polygon(765, 380, 742.5, 380, 742.5, 375, 730, 375, 730, 372, 742.5, 372, 742.5, 370, 765, 370, 765, 380, fill='red', outline='')
enemy_antenna=canvas.create_polygon(760, 370, 762.5, 362.5, 760, 362.5, 757.5, 370, fill='red', outline='')
enemy_shield=canvas.create_polygon(720, 370, 715, 370, 712.5, 390, 715, 410, 720, 410, 717.5, 390, 730, 390, 730, 385, 717.5, 385, 720, 370, fill='yellow', outline='')
enemy_parallel_shield=canvas.create_polygon(780, 370, 785, 370, 787.5, 390, 785, 410, 780, 410, 782.5, 390, 770, 390, 770, 385, 782.5, 385, 780, 370, fill='yellow', outline='')
enemy_hit_square=canvas.create_rectangle(680, 20, 780, 40, fill='yellow', outline='')
player_hit_square=canvas.create_rectangle(20, 20, 120, 40, fill='yellow', outline='')
the_yeet_square=canvas.create_rectangle(200, 125, 600, 225, fill='green', outline='')
instructions_one=canvas.create_text(400, 150, text='''TANK BATTLE SIMULATOR''', font=('Calibri', 24), fill='black')
instructions_two=canvas.create_text(400, 200, text='''Press ENTER to start''', font=('Calibri', 16), fill='black')
enemy_hp=50
player_hp=10
timer=0
ammo=80
ammo_text=canvas.create_text(100, 50, text='Remaining Ammo: %s' % ammo, font=('Calibri', 12))
player_hp_text=canvas.create_text(70, 25, text='Your HP: %s' % player_hp, font=('Calibri', 12))
enemy_hp_text=canvas.create_text(725, 25, text='Enemy HP: %s' % enemy_hp, font=('Calibri', 12))
def controls(keys):
    global enemy_hit_square
    global player_hit_square
    global timer
    global is_shield
    global enemy_hp
    global player_hp
    global player_hp_text
    global enemy_hp_text
    global ammo
    global ammo_text
    if player_hp>0 and enemy_hp>0:
        if keys.keysym=='Right':
            canvas.tkraise(player_neck)
            canvas.tkraise(player_head)
            canvas.tkraise(player_antenna)
            canvas.tkraise(player_shield)
            canvas.itemconfig(player_neck, fill='blue')
            canvas.itemconfig(player_head, fill='blue')
            canvas.itemconfig(player_antenna, fill='blue')
            canvas.itemconfig(player_parallel_neck, fill='yellow')
            canvas.itemconfig(player_parallel_head, fill='yellow')
            canvas.itemconfig(player_parallel_antenna, fill='yellow')
            canvas.itemconfig(player_parallel_shield, fill='yellow')
            if is_shield==1:
                canvas.itemconfig(player_shield, fill='blue')
                tk.update()
            if canvas.coords(player_body)[2]<=800:
                canvas.move(player_body, 10, 0)
                canvas.move(player_back_wheel, 10, 0)
                canvas.move(player_front_wheel, 10, 0)
                canvas.move(player_neck, 10, 0)
                canvas.move(player_head, 10, 0)
                canvas.move(player_antenna, 10, 0)
                canvas.move(player_parallel_neck, 10, 0)
                canvas.move(player_parallel_head, 10, 0)
                canvas.move(player_parallel_antenna, 10, 0)
                canvas.move(player_parallel_shield, 10, 0)
                canvas.move(player_shield, 10, 0)
            tk.update()
        if keys.keysym=='Left':
            canvas.tkraise(player_parallel_neck)
            canvas.tkraise(player_parallel_head)
            canvas.tkraise(player_parallel_antenna)
            canvas.tkraise(player_parallel_shield)
            canvas.itemconfig(player_neck, fill='yellow')
            canvas.itemconfig(player_head, fill='yellow')
            canvas.itemconfig(player_shield, fill='yellow')
            canvas.itemconfig(player_antenna, fill='yellow')
            canvas.itemconfig(player_parallel_neck, fill='blue')
            canvas.itemconfig(player_parallel_head, fill='blue')
            canvas.itemconfig(player_parallel_antenna, fill='blue')
            if is_shield==1:
                canvas.itemconfig(player_parallel_shield, fill='blue')
                tk.update()
            if canvas.coords(player_body)[0]>=0:
                canvas.move(player_body, -10, 0)
                canvas.move(player_back_wheel, -10, 0)
                canvas.move(player_front_wheel, -10, 0)
                canvas.move(player_neck, -10, 0)
                canvas.move(player_head, -10, 0)
                canvas.move(player_antenna, -10, 0)
                canvas.move(player_parallel_neck, -10, 0)
                canvas.move(player_parallel_head, -10, 0)
                canvas.move(player_parallel_antenna, -10, 0)
                canvas.move(player_parallel_shield, -10, 0)
                canvas.move(player_shield, -10, 0)
            tk.update()
        if keys.keysym=='Up':
            if canvas.coords(player_head)[1]>=25:
                canvas.move(player_body, 0, -10)
                canvas.move(player_back_wheel, 0, -10)
                canvas.move(player_front_wheel, 0, -10)
                canvas.move(player_neck, 0, -10)
                canvas.move(player_head, 0, -10)
                canvas.move(player_antenna, 0, -10)
                canvas.move(player_parallel_neck, 0, -10)
                canvas.move(player_parallel_head, 0, -10)
                canvas.move(player_parallel_antenna, 0, -10)
                canvas.move(player_parallel_shield, 0, -10)
                canvas.move(player_shield, 0, -10)
            tk.update()
        if keys.keysym=='Down':
            if canvas.coords(player_body)[3]<=800:
                canvas.move(player_body, 0, 10)
                canvas.move(player_back_wheel, 0, 10)
                canvas.move(player_front_wheel, 0, 10)
                canvas.move(player_neck, 0, 10)
                canvas.move(player_head, 0, 10)
                canvas.move(player_antenna, 0, 10)
                canvas.move(player_parallel_neck, 0, 10)
                canvas.move(player_parallel_head, 0, 10)
                canvas.move(player_parallel_antenna, 0, 10)
                canvas.move(player_parallel_shield, 0, 10)
                canvas.move(player_shield, 0, 10)
            tk.update()
        if keys.keysym=='q':
            if canvas.itemcget(player_shield, 'fill')=='yellow' and canvas.itemcget(player_parallel_shield, 'fill')=='yellow':
                if canvas.itemcget(player_head, 'fill')=='blue':
                    canvas.tkraise(player_shield)
                    canvas.itemconfig(player_shield, fill='blue')
                    is_shield=1
                    tk.update()
                elif canvas.itemcget(player_head, 'fill')=='yellow':
                    canvas.tkraise(player_parallel_shield)
                    canvas.itemconfig(player_parallel_shield, fill='blue')
                    is_shield=1
                    tk.update()
            elif canvas.itemcget(player_shield, 'fill')=='blue' or canvas.itemcget(player_parallel_shield, 'fill')=='blue':
                canvas.itemconfig(player_shield, fill='yellow')
                canvas.itemconfig(player_parallel_shield, fill='yellow')
                is_shield=0
                tk.update()
        if keys.keysym=='space':
            if ammo>0:
                canvas.unbind_all('<KeyPress-space>')
                if canvas.itemcget(player_shield, 'fill')=='yellow' and canvas.itemcget(player_parallel_shield, 'fill')=='yellow':
                    colores=canvas.itemcget(player_head, 'fill')
                    mixer.Channel(1).play(mixer.Sound(r"C:\Tank_Battle_Simulator\Laser Blaster-SoundBible.com-1388608841.mp3"))
                    if colores=='blue':
                        laser=canvas.create_rectangle(canvas.coords(player_head)[4], canvas.coords(player_head)[5]-1.5, canvas.coords(player_head)[4]+400, canvas.coords(player_head)[5]-2, fill='green', outline='')
                        tk.update()
                        if canvas.itemcget(enemy_shield, 'fill')=='yellow' and canvas.coords(player_body)[2]<canvas.coords(enemy_body)[0] and canvas.coords(laser)[2]-20>=canvas.coords(enemy_head)[0] and canvas.coords(laser)[3]<=canvas.coords(enemy_body)[3] and canvas.coords(laser)[3]+6.5>=canvas.coords(enemy_head)[3]:
                            canvas.itemconfig(enemy_hit_square, fill='red')
                            enemy_hp-=1
                            canvas.delete(enemy_hp_text)
                            enemy_hp_text=canvas.create_text(725, 25, text='Enemy HP: %s' % enemy_hp, font=('Calibri', 12))
                            tk.update()
                            if enemy_hp>0:
                                mixer.Channel(4).play(mixer.Sound(r"C:\Tank_Battle_Simulator\Minecraft-death-sound.mp3"))
                            elif enemy_hp<=0:
                                mixer.pause()
                                mixer.Channel(4).play(mixer.Sound(r"C:\Tank_Battle_Simulator\zapsplat_explosions_double_large_explosion_some_very_light_distortion_63287.mp3"))  
                                explosion_img=PhotoImage(file=r"C:\Tank_Battle_Simulator\explosion.png")
                                real_img=explosion_img.subsample(4, 4)
                                real_real=canvas.create_image(canvas.coords(enemy_head)[0], canvas.coords(enemy_head)[1], image=real_img)
                                tk.update()
                                time.sleep(5)
                                canvas.delete('all')
                                you_win=canvas.create_rectangle(0,0,800,800, fill='green', outline='')
                                you_win_text=canvas.create_text(400, 200, text='VICTORY', font=('Calibri', 24), fill='red')
                                score_text=canvas.create_text(400, 400, text='''Results:\n\nPoints Earned: %s\nTime Bonus: %s\nTotal Score: %s''' % ((1000-(10-player_hp)-(80-ammo)), (200-timer), (1000-(10-player_hp)-(80-ammo))+(200-timer)), font=('Calibri', 12), fill='red')
                                tk.clipboard_append('''Results (game won):\n\nPoints Earned: %s\nTime Bonus: %s\nTotal Score: %s''' % ((1000-(10-player_hp)-(80-ammo)), (200-timer), (1000-(10-player_hp)-(80-ammo))+(200-timer)))
                                tk.update()
                        time.sleep(0.1)
                        canvas.delete(laser)
                        canvas.itemconfig(enemy_hit_square, fill='yellow')
                        tk.update()
                    elif colores=='yellow':
                        laser=canvas.create_rectangle(canvas.coords(player_parallel_head)[0], canvas.coords(player_parallel_head)[7]-1.5, canvas.coords(player_parallel_head)[0]-400, canvas.coords(player_parallel_head)[7]-2, fill='green', outline='')
                        tk.update()
                        if canvas.itemcget(enemy_parallel_shield, 'fill')=='yellow' and canvas.coords(player_body)[0]>canvas.coords(enemy_body)[2] and canvas.coords(laser)[0]+20<=canvas.coords(enemy_parallel_head)[4] and canvas.coords(laser)[3]<=canvas.coords(enemy_body)[3] and canvas.coords(laser)[3]+6.5>=canvas.coords(enemy_parallel_head)[3]:
                            canvas.itemconfig(enemy_hit_square, fill='red')
                            enemy_hp-=1                            
                            canvas.delete(enemy_hp_text)
                            enemy_hp_text=canvas.create_text(725, 25, text='Enemy HP: %s' % enemy_hp, font=('Calibri', 12))
                            tk.update()
                            if enemy_hp>0:
                                mixer.Channel(4).play(mixer.Sound(r"C:\Tank_Battle_Simulator\Minecraft-death-sound.mp3"))
                            elif enemy_hp<=0:
                                mixer.pause()
                                mixer.Channel(4).play(mixer.Sound(r"C:\Tank_Battle_Simulator\zapsplat_explosions_double_large_explosion_some_very_light_distortion_63287.mp3"))
                                explosion_img=PhotoImage(file=r"C:\Tank_Battle_Simulator\explosion.png")
                                real_img=explosion_img.subsample(4, 4)
                                real_real=canvas.create_image(canvas.coords(enemy_head)[0], canvas.coords(enemy_head)[1], image=real_img)
                                tk.update()
                                time.sleep(5)
                                canvas.delete('all')
                                you_win=canvas.create_rectangle(0,0,800,800, fill='green', outline='')
                                you_win_text=canvas.create_text(400, 200, text='VICTORY', font=('Calibri', 24), fill='red')
                                score_text=canvas.create_text(400, 400, text='''Results (game won):\n\nPoints Earned: %s\nTime Bonus: %s\nTotal Score: %s''' % ((1000-(10-player_hp)-(80-ammo)), (200-timer), (1000-(10-player_hp)-(80-ammo))+(200-timer)), font=('Calibri', 12), fill='red')
                                tk.clipboard_append('''Results:\n\nPoints Earned: %s\nTime Bonus: %s\nTotal Score: %s''' % ((1000-(10-player_hp)-(80-ammo)), (200-timer), (1000-(10-player_hp)-(80-ammo))+(200-timer)))
                                tk.update()
                        time.sleep(0.1)
                        canvas.delete(laser)
                        canvas.itemconfig(enemy_hit_square, fill='yellow')
                        tk.update()
                ammo-=1
                canvas.delete(ammo_text)
                ammo_text=canvas.create_text(100, 50, text='Remaining Ammo: %s' % ammo, font=('Calibri', 12))
                tk.update()
                canvas.bind_all('<KeyPress-space>', controls)
def track_time():
    global timer
    timer+=1
    tk.after(1000, track_time)
def play_za_sound():
    global player_hp
    global enemy_hp
    mixer.init()
    mixer.set_num_channels(10)
    if player_hp>0 and enemy_hp>0:
        mixer.Channel(0).play(mixer.Sound(r"C:\Tank_Battle_Simulator\1-09. Battle (Shrine)- Original Soundtrack Ver..mp3"))
    tk.after(105000, play_za_sound)
def start(key):
    global enemy_hit_square
    global player_hit_square
    global player_hp
    global enemy_hp
    global player_hp_text
    global enemy_hp_text
    if key.keysym=='Return':
        canvas.unbind_all('<KeyPress-Return>')
        play_za_sound()
        canvas.delete(instructions_one)
        canvas.delete(instructions_two)
        tk.update()
        three=canvas.create_text(400, 150, text='3', font=('Calibri', 24))
        tk.update()
        winsound.Beep(489, 300)
        time.sleep(0.64)
        canvas.delete(three)
        tk.update()
        two=canvas.create_text(400, 150, text='2', font=('Calibri', 24))
        tk.update()
        winsound.Beep(489, 300)
        time.sleep(0.64)
        canvas.delete(two)
        tk.update()
        one=canvas.create_text(400, 150, text='1', font=('Calibri', 24))
        tk.update()
        winsound.Beep(489, 300)
        time.sleep(0.64)
        canvas.delete(one)
        tk.update()
        go=canvas.create_text(400, 150, text='GO!', font=('Calibri', 24))
        tk.update()
        winsound.Beep(1000, 1000)
        time.sleep(0.64)
        canvas.delete(go)
        canvas.delete(the_yeet_square)
        tk.update()
        canvas.bind_all('<KeyPress-Right>', controls)
        canvas.bind_all('<KeyPress-Left>', controls)
        canvas.bind_all('<KeyPress-Up>', controls)
        canvas.bind_all('<KeyPress-Down>', controls)
        canvas.bind_all('<KeyPress-space>', controls)
        canvas.bind_all('<KeyPress-q>', controls)
        tk.after(1000, track_time)
        def ai_code():
            global enemy_hit_square
            global player_hit_square
            global timer
            global player_hp
            global enemy_hp
            global player_hp_text
            global enemy_hp_text
            if enemy_hp>0 and player_hp>0:
                choice=random.choice(randlist)
                if choice=='moveup':
                    for b in range(0, random.randint(1, 80)):
                        if canvas.coords(enemy_head)[3]+10>=50:
                            canvas.move(enemy_body, 0, -10)
                            canvas.move(enemy_front_wheel, 0, -10)
                            canvas.move(enemy_back_wheel, 0, -10)
                            canvas.move(enemy_neck, 0, -10)
                            canvas.move(enemy_head, 0, -10)
                            canvas.move(enemy_antenna, 0, -10)
                            canvas.move(enemy_shield, 0, -10)
                            canvas.move(enemy_parallel_shield, 0, -10)
                            canvas.move(enemy_parallel_head, 0, -10)
                            canvas.move(enemy_parallel_neck, 0, -10)
                            canvas.move(enemy_parallel_antenna, 0, -10)
                            tk.update()
                            time.sleep(0.01)
                elif choice=='movedown':
                    for a in range(0, random.randint(1, 80)):
                        if canvas.coords(enemy_body)[3]-5<=750:
                            canvas.move(enemy_body, 0, 10)
                            canvas.move(enemy_front_wheel, 0, 10)
                            canvas.move(enemy_back_wheel, 0, 10)
                            canvas.move(enemy_neck, 0, 10)
                            canvas.move(enemy_head, 0, 10)
                            canvas.move(enemy_antenna, 0, 10)
                            canvas.move(enemy_shield, 0, 10)
                            canvas.move(enemy_parallel_shield, 0, 10)
                            canvas.move(enemy_parallel_head, 0, 10)
                            canvas.move(enemy_parallel_neck, 0, 10)
                            canvas.move(enemy_parallel_antenna, 0, 10)
                            tk.update()
                            time.sleep(0.01)
                elif choice=='moveleft':
                    for z in range(0, random.randint(1, 80)):
                        if canvas.coords(enemy_body)[0]>=50:
                            canvas.tkraise(enemy_head)
                            canvas.tkraise(enemy_neck)
                            canvas.tkraise(enemy_antenna)
                            canvas.tkraise(enemy_shield)
                            canvas.itemconfig(enemy_head, fill='red')
                            canvas.itemconfig(enemy_neck, fill='red')
                            canvas.itemconfig(enemy_antenna, fill='red')
                            canvas.itemconfig(enemy_parallel_head, fill='yellow')
                            canvas.itemconfig(enemy_parallel_neck, fill='yellow')
                            canvas.itemconfig(enemy_parallel_antenna, fill='yellow')
                            canvas.itemconfig(enemy_parallel_shield, fill='yellow')
                            canvas.move(enemy_body, -10, 0)
                            canvas.move(enemy_front_wheel, -10, 0)
                            canvas.move(enemy_back_wheel, -10, 0)
                            canvas.move(enemy_neck, -10, 0)
                            canvas.move(enemy_head, -10, 0)
                            canvas.move(enemy_antenna, -10, 0)
                            canvas.move(enemy_shield, -10, 0)
                            canvas.move(enemy_parallel_shield, -10, 0)
                            canvas.move(enemy_parallel_head, -10, 0)
                            canvas.move(enemy_parallel_neck, -10, 0)
                            canvas.move(enemy_parallel_antenna, -10, 0)
                            tk.update()
                            time.sleep(0.01)
                elif choice=='moveright':
                    for y in range(0, random.randint(1, 80)):
                        if canvas.coords(enemy_body)[2]<=750:
                            canvas.tkraise(enemy_parallel_head)
                            canvas.tkraise(enemy_parallel_neck)
                            canvas.tkraise(enemy_parallel_antenna)
                            canvas.tkraise(enemy_parallel_shield)
                            canvas.itemconfig(enemy_parallel_head, fill='red')
                            canvas.itemconfig(enemy_parallel_neck, fill='red')
                            canvas.itemconfig(enemy_parallel_antenna, fill='red')
                            canvas.itemconfig(enemy_head, fill='yellow')
                            canvas.itemconfig(enemy_neck, fill='yellow')
                            canvas.itemconfig(enemy_antenna, fill='yellow')
                            canvas.itemconfig(enemy_shield, fill='yellow')
                            canvas.move(enemy_body, 10, 0)
                            canvas.move(enemy_front_wheel, 10, 0)
                            canvas.move(enemy_back_wheel, 10, 0)
                            canvas.move(enemy_neck, 10, 0)
                            canvas.move(enemy_head, 10, 0)
                            canvas.move(enemy_antenna, 10, 0)
                            canvas.move(enemy_shield, 10, 0)
                            canvas.move(enemy_parallel_shield, 10, 0)
                            canvas.move(enemy_parallel_head, 10, 0)
                            canvas.move(enemy_parallel_neck, 10, 0)
                            canvas.move(enemy_parallel_antenna, 10, 0)
                            tk.update()
                            time.sleep(0.01)
                elif choice=='simpleattack':
                    if canvas.coords(enemy_body)[2]<canvas.coords(player_body)[0]:
                        canvas.tkraise(enemy_parallel_head)
                        canvas.tkraise(enemy_parallel_neck)
                        canvas.tkraise(enemy_parallel_antenna)
                        canvas.tkraise(enemy_parallel_shield)
                        canvas.itemconfig(enemy_parallel_head, fill='red')
                        canvas.itemconfig(enemy_parallel_neck, fill='red')
                        canvas.itemconfig(enemy_parallel_antenna, fill='red')
                        canvas.itemconfig(enemy_head, fill='yellow')
                        canvas.itemconfig(enemy_neck, fill='yellow')
                        canvas.itemconfig(enemy_antenna, fill='yellow')
                        canvas.itemconfig(enemy_shield, fill='yellow')
                        tk.update()
                    elif canvas.coords(enemy_body)[0]>canvas.coords(player_body)[2]:
                        canvas.tkraise(enemy_head)
                        canvas.tkraise(enemy_neck)
                        canvas.tkraise(enemy_antenna)
                        canvas.tkraise(enemy_shield)
                        canvas.itemconfig(enemy_head, fill='red')
                        canvas.itemconfig(enemy_neck, fill='red')
                        canvas.itemconfig(enemy_antenna, fill='red')
                        canvas.itemconfig(enemy_parallel_head, fill='yellow')
                        canvas.itemconfig(enemy_parallel_neck, fill='yellow')
                        canvas.itemconfig(enemy_parallel_antenna, fill='yellow')
                        canvas.itemconfig(enemy_parallel_shield, fill='yellow')
                        tk.update()
                    if canvas.itemcget(enemy_shield, 'fill')=='yellow' and canvas.itemcget(enemy_parallel_shield, 'fill')=='yellow':
                        if canvas.itemcget(enemy_head, 'fill')=='red':
                            enemy_laser=canvas.create_rectangle(canvas.coords(enemy_head)[0], canvas.coords(enemy_head)[7]-1.5, canvas.coords(enemy_head)[0]-400, canvas.coords(enemy_head)[7]-2, fill='purple', outline='')
                            mixer.Channel(2).play(mixer.Sound(r"C:\Tank_Battle_Simulator\Laser Blaster-SoundBible.com-1388608841.mp3"))
                            tk.update()
                            if canvas.coords(enemy_body)[0]>canvas.coords(player_body)[2] and canvas.itemcget(player_shield, 'fill')=='yellow' and canvas.coords(enemy_laser)[0]+20<=canvas.coords(player_head)[4] and canvas.coords(enemy_laser)[3]<=canvas.coords(player_body)[3] and canvas.coords(enemy_laser)[3]+6.5>=canvas.coords(player_head)[1]:
                                canvas.itemconfig(player_hit_square, fill='red')
                                player_hp-=1
                                canvas.delete(player_hp_text)
                                player_hp_text=canvas.create_text(75, 25, text='Your HP: %s' % player_hp, font=('Calibri', 12))
                                tk.update()
                                if player_hp>0:
                                    mixer.Channel(3).play(mixer.Sound(r"C:\Tank_Battle_Simulator\Minecraft-death-sound.mp3"))
                                elif player_hp<=0:
                                    mixer.pause()
                                    mixer.Channel(3).play(mixer.Sound(r"C:\Tank_Battle_Simulator\zapsplat_explosions_double_large_explosion_some_very_light_distortion_63287.mp3"))
                                    explosion_img=PhotoImage(file=r"C:\Tank_Battle_Simulator\explosion.png")
                                    real_img=explosion_img.subsample(4, 4)
                                    real_real=canvas.create_image(canvas.coords(player_head)[0], canvas.coords(player_head)[1], image=real_img)
                                    tk.update()
                                    time.sleep(5)
                                    canvas.delete('all')
                                    you_lose=canvas.create_rectangle(0,0,800,800, fill='black', outline='')
                                    you_lose_text=canvas.create_text(400, 200, text='DEFEAT', font=('Calibri', 24), fill='white')
                                    score_text=canvas.create_text(400, 400, text='''Results:\n\nPoints Earned: %s\nTime Bonus: %s\nTotal Score: %s''' % ((50-enemy_hp), (200-timer), ((50-enemy_hp)+(200-timer))), font=('Calibri', 12), fill='white')
                                    tk.clipboard_append('''Results (game lost):\n\nPoints Earned: %s\nTime Bonus: %s\nTotal Score: %s''' % ((50-enemy_hp), (200-timer), ((50-enemy_hp)+(200-timer))))
                                    tk.update()
                            time.sleep(0.1)
                            canvas.delete(enemy_laser)
                            canvas.itemconfig(player_hit_square, fill='yellow')
                            tk.update()
                        elif canvas.itemcget(enemy_head, 'fill')=='yellow':
                            enemy_laser=canvas.create_rectangle(canvas.coords(enemy_parallel_head)[4], canvas.coords(enemy_parallel_head)[5]-1.5, canvas.coords(enemy_parallel_head)[4]+400, canvas.coords(enemy_parallel_head)[5]-2, fill='purple', outline='')
                            mixer.Channel(2).play(mixer.Sound(r"C:\Tank_Battle_Simulator\Laser Blaster-SoundBible.com-1388608841.mp3"))
                            tk.update()
                            if canvas.coords(enemy_body)[2]<canvas.coords(player_body)[0] and canvas.itemcget(player_parallel_shield, 'fill')=='yellow' and canvas.coords(enemy_laser)[2]-20>=canvas.coords(player_head)[0] and canvas.coords(enemy_laser)[3]<=canvas.coords(player_body)[3] and canvas.coords(enemy_laser)[3]+6.5>=canvas.coords(player_head)[1]:
                                canvas.itemconfig(player_hit_square, fill= 'red')
                                player_hp-=1
                                canvas.delete(player_hp_text)
                                player_hp_text=canvas.create_text(75, 25, text='Your HP: %s' % player_hp, font=('Calibri', 12))
                                tk.update()
                                if player_hp>0:
                                    mixer.Channel(3).play(mixer.Sound(r"C:\Tank_Battle_Simulator\Minecraft-death-sound.mp3"))
                                elif player_hp<=0:
                                    mixer.pause()
                                    mixer.Channel(3).play(mixer.Sound(r"C:\Tank_Battle_Simulator\zapsplat_explosions_double_large_explosion_some_very_light_distortion_63287.mp3"))
                                    explosion_img=PhotoImage(file=r"C:\Tank_Battle_Simulator\explosion.png")
                                    real_img=explosion_img.subsample(4, 4)
                                    real_real=canvas.create_image(canvas.coords(player_head)[0], canvas.coords(player_head)[1], image=real_img)
                                    tk.update()
                                    time.sleep(5)
                                    canvas.delete('all')
                                    you_lose=canvas.create_rectangle(0,0,800,800, fill='black', outline='')
                                    you_lose_text=canvas.create_text(400, 200, text='DEFEAT', font=('Calibri', 24), fill='white')
                                    score_text=canvas.create_text(400, 400, text='''Results:\n\nPoints Earned: %s\nTime Bonus: %s\nTotal Score: %s''' % ((50-enemy_hp), (200-timer), ((50-enemy_hp)+(200-timer))), font=('Calibri', 12), fill='white')
                                    tk.clipboard_append('''Results (game lost):\n\nPoints Earned: %s\nTime Bonus: %s\nTotal Score: %s''' % ((50-enemy_hp), (200-timer), ((50-enemy_hp)+(200-timer))))
                                    tk.update()
                            time.sleep(0.1)
                            canvas.delete(enemy_laser)
                            canvas.itemconfig(player_hit_square, fill='yellow')
                            tk.update()
                elif choice=='shield':
                    if canvas.itemcget(enemy_head, 'fill')=='red':
                        canvas.itemconfig(enemy_shield, fill='red')
                        tk.update()
                    elif canvas.itemcget(enemy_head, 'fill')=='yellow':
                        canvas.itemconfig(enemy_parallel_shield, fill='red')
                        tk.update()
                elif choice=='deactivate_shield':
                    sure=random.randint(1, 2)
                    if sure==1:
                        canvas.itemconfig(enemy_shield, fill='yellow')
                        canvas.itemconfig(enemy_parallel_shield, fill='yellow')
                        tk.update()
                    elif sure==2:
                        pass
                elif choice=='trackplayer':
                    if canvas.coords(player_body)[2]+50<=canvas.coords(enemy_body)[0]:
                        while canvas.coords(player_body)[2]+50<=canvas.coords(enemy_body)[0]:
                            canvas.tkraise(enemy_head)
                            canvas.tkraise(enemy_neck)
                            canvas.tkraise(enemy_antenna)
                            canvas.tkraise(enemy_shield)
                            canvas.itemconfig(enemy_head, fill='red')
                            canvas.itemconfig(enemy_neck, fill='red')
                            canvas.itemconfig(enemy_antenna, fill='red')
                            canvas.itemconfig(enemy_parallel_head, fill='yellow')
                            canvas.itemconfig(enemy_parallel_neck, fill='yellow')
                            canvas.itemconfig(enemy_parallel_antenna, fill='yellow')
                            canvas.itemconfig(enemy_parallel_shield, fill='yellow')
                            canvas.move(enemy_body, -10, 0)
                            canvas.move(enemy_front_wheel, -10, 0)
                            canvas.move(enemy_back_wheel, -10, 0)
                            canvas.move(enemy_neck, -10, 0)
                            canvas.move(enemy_head, -10, 0)
                            canvas.move(enemy_antenna, -10, 0)
                            canvas.move(enemy_shield, -10, 0)
                            canvas.move(enemy_parallel_shield, -10, 0)
                            canvas.move(enemy_parallel_head, -10, 0)
                            canvas.move(enemy_parallel_neck, -10, 0)
                            canvas.move(enemy_parallel_antenna, -10, 0)
                            tk.update()
                            time.sleep(0.01)
                    elif canvas.coords(player_body)[2]-50>=canvas.coords(enemy_body)[0]:
                        while canvas.coords(player_body)[2]-50>=canvas.coords(enemy_body)[0]:
                            canvas.tkraise(enemy_parallel_head)
                            canvas.tkraise(enemy_parallel_neck)
                            canvas.tkraise(enemy_parallel_antenna)
                            canvas.tkraise(enemy_parallel_shield)
                            canvas.itemconfig(enemy_parallel_head, fill='red')
                            canvas.itemconfig(enemy_parallel_neck, fill='red')
                            canvas.itemconfig(enemy_parallel_antenna, fill='red')
                            canvas.itemconfig(enemy_head, fill='yellow')
                            canvas.itemconfig(enemy_neck, fill='yellow')
                            canvas.itemconfig(enemy_antenna, fill='yellow')
                            canvas.itemconfig(enemy_shield, fill='yellow')
                            canvas.move(enemy_body, 10, 0)
                            canvas.move(enemy_front_wheel, 10, 0)
                            canvas.move(enemy_back_wheel, 10, 0)
                            canvas.move(enemy_neck, 10, 0)
                            canvas.move(enemy_head, 10, 0)
                            canvas.move(enemy_antenna, 10, 0)
                            canvas.move(enemy_shield, 10, 0)
                            canvas.move(enemy_parallel_shield, 10, 0)
                            canvas.move(enemy_parallel_head, 10, 0)
                            canvas.move(enemy_parallel_neck, 10, 0)
                            canvas.move(enemy_parallel_antenna, 10, 0)
                            tk.update()
                            time.sleep(0.01)
                    if canvas.coords(enemy_body)[3]<=canvas.coords(player_body)[1]:
                        while canvas.coords(enemy_body)[3]<=canvas.coords(player_body)[1]:
                            canvas.move(enemy_body, 0, 10)
                            canvas.move(enemy_front_wheel, 0, 10)
                            canvas.move(enemy_back_wheel, 0, 10)
                            canvas.move(enemy_neck, 0, 10)
                            canvas.move(enemy_head, 0, 10)
                            canvas.move(enemy_antenna, 0, 10)
                            canvas.move(enemy_shield, 0, 10)
                            canvas.move(enemy_parallel_shield, 0, 10)
                            canvas.move(enemy_parallel_head, 0, 10)
                            canvas.move(enemy_parallel_neck, 0, 10)
                            canvas.move(enemy_parallel_antenna, 0, 10)
                            tk.update()
                            time.sleep(0.01)
                    elif canvas.coords(enemy_body)[1]>=canvas.coords(player_body)[3]:
                        while canvas.coords(enemy_body)[1]>=canvas.coords(player_body)[3]:
                            canvas.move(enemy_body, 0, -10)
                            canvas.move(enemy_front_wheel, 0, -10)
                            canvas.move(enemy_back_wheel, 0, -10)
                            canvas.move(enemy_neck, 0, -10)
                            canvas.move(enemy_head, 0, -10)
                            canvas.move(enemy_antenna, 0, -10)
                            canvas.move(enemy_shield, 0, -10)
                            canvas.move(enemy_parallel_shield, 0, -10)
                            canvas.move(enemy_parallel_head, 0, -10)
                            canvas.move(enemy_parallel_neck, 0, -10)
                            canvas.move(enemy_parallel_antenna, 0, -10)
                            tk.update()
                            time.sleep(0.01)
                elif choice=='point':
                    if canvas.coords(enemy_body)[0]>=canvas.coords(player_body)[2]:
                        canvas.tkraise(enemy_head)
                        canvas.tkraise(enemy_neck)
                        canvas.tkraise(enemy_antenna)
                        canvas.tkraise(enemy_shield)
                        canvas.itemconfig(enemy_head, fill='red')
                        canvas.itemconfig(enemy_neck, fill='red')
                        canvas.itemconfig(enemy_antenna, fill='red')
                        canvas.itemconfig(enemy_parallel_head, fill='yellow')
                        canvas.itemconfig(enemy_parallel_neck, fill='yellow')
                        canvas.itemconfig(enemy_parallel_antenna, fill='yellow')
                        canvas.itemconfig(enemy_parallel_shield, fill='yellow')
                        tk.update()
                    elif canvas.coords(enemy_body)[2]<=canvas.coords(player_body)[0]:
                        canvas.tkraise(enemy_parallel_head)
                        canvas.tkraise(enemy_parallel_neck)
                        canvas.tkraise(enemy_parallel_antenna)
                        canvas.tkraise(enemy_parallel_shield)
                        canvas.itemconfig(enemy_parallel_head, fill='red')
                        canvas.itemconfig(enemy_parallel_neck, fill='red')
                        canvas.itemconfig(enemy_parallel_antenna, fill='red')
                        canvas.itemconfig(enemy_head, fill='yellow')
                        canvas.itemconfig(enemy_neck, fill='yellow')
                        canvas.itemconfig(enemy_antenna, fill='yellow')
                        canvas.itemconfig(enemy_shield, fill='yellow')
                        tk.update()
                elif choice=='destructo_attack':
                    for x in range(0, 20):
                        if canvas.coords(enemy_body)[2]<canvas.coords(player_body)[0]:
                            canvas.tkraise(enemy_parallel_head)
                            canvas.tkraise(enemy_parallel_neck)
                            canvas.tkraise(enemy_parallel_antenna)
                            canvas.tkraise(enemy_parallel_shield)
                            canvas.itemconfig(enemy_parallel_head, fill='red')
                            canvas.itemconfig(enemy_parallel_neck, fill='red')
                            canvas.itemconfig(enemy_parallel_antenna, fill='red')
                            canvas.itemconfig(enemy_head, fill='yellow')
                            canvas.itemconfig(enemy_neck, fill='yellow')
                            canvas.itemconfig(enemy_antenna, fill='yellow')
                            canvas.itemconfig(enemy_shield, fill='yellow')
                            tk.update()
                        elif canvas.coords(enemy_body)[0]>canvas.coords(player_body)[2]:
                            canvas.tkraise(enemy_head)
                            canvas.tkraise(enemy_neck)
                            canvas.tkraise(enemy_antenna)
                            canvas.tkraise(enemy_shield)
                            canvas.itemconfig(enemy_head, fill='red')
                            canvas.itemconfig(enemy_neck, fill='red')
                            canvas.itemconfig(enemy_antenna, fill='red')
                            canvas.itemconfig(enemy_parallel_head, fill='yellow')
                            canvas.itemconfig(enemy_parallel_neck, fill='yellow')
                            canvas.itemconfig(enemy_parallel_antenna, fill='yellow')
                            canvas.itemconfig(enemy_parallel_shield, fill='yellow')
                            tk.update()
                        direction=random.randint(1, 2)
                        if direction==1:
                            if canvas.coords(enemy_body)[1]>=50:
                                canvas.move(enemy_body, 0, -10)
                                canvas.move(enemy_front_wheel, 0, -10)
                                canvas.move(enemy_back_wheel, 0, -10)
                                canvas.move(enemy_neck, 0, -10)
                                canvas.move(enemy_head, 0, -10)
                                canvas.move(enemy_antenna, 0, -10)
                                canvas.move(enemy_shield, 0, -10)
                                canvas.move(enemy_parallel_shield, 0, -10)
                                canvas.move(enemy_parallel_head, 0, -10)
                                canvas.move(enemy_parallel_neck, 0, -10)
                                canvas.move(enemy_parallel_antenna, 0, -10)
                                tk.update()
                                time.sleep(0.02)
                        elif direction==2:
                            if canvas.coords(enemy_body)[3]<=750:
                                canvas.move(enemy_body, 0, 10)
                                canvas.move(enemy_front_wheel, 0, 10)
                                canvas.move(enemy_back_wheel, 0, 10)
                                canvas.move(enemy_neck, 0, 10)
                                canvas.move(enemy_head, 0, 10)
                                canvas.move(enemy_antenna, 0, 10)
                                canvas.move(enemy_shield, 0, 10)
                                canvas.move(enemy_parallel_shield, 0, 10)
                                canvas.move(enemy_parallel_head, 0, 10)
                                canvas.move(enemy_parallel_neck, 0, 10)
                                canvas.move(enemy_parallel_antenna, 0, 10)
                                tk.update()
                                time.sleep(0.02)
                        if canvas.itemcget(enemy_shield, 'fill')=='yellow' and canvas.itemcget(enemy_parallel_shield, 'fill')=='yellow':
                            if canvas.itemcget(enemy_head, 'fill')=='red':
                                enemy_laser=canvas.create_rectangle(canvas.coords(enemy_head)[0], canvas.coords(enemy_head)[7]-1.5, canvas.coords(enemy_head)[0]-400, canvas.coords(enemy_head)[7]-2, fill='purple', outline='')
                                mixer.Channel(2).play(mixer.Sound(r"C:\Tank_Battle_Simulator\Laser Blaster-SoundBible.com-1388608841.mp3"))
                                tk.update()
                                if canvas.coords(enemy_body)[0]>canvas.coords(player_body)[2] and canvas.itemcget(player_shield, 'fill')=='yellow' and canvas.coords(enemy_laser)[0]+20<=canvas.coords(player_head)[4] and canvas.coords(enemy_laser)[3]<=canvas.coords(player_body)[3] and canvas.coords(enemy_laser)[3]+6.5>=canvas.coords(player_head)[1]:
                                    canvas.itemconfig(player_hit_square, fill='red')
                                    player_hp-=1
                                    canvas.delete(player_hp_text)
                                    player_hp_text=canvas.create_text(75, 25, text='Your HP: %s' % player_hp, font=('Calibri', 12))
                                    tk.update()
                                    if player_hp>0:
                                        mixer.Channel(3).play(mixer.Sound(r"C:\Tank_Battle_Simulator\Minecraft-death-sound.mp3"))
                                    elif player_hp<=0:
                                        mixer.pause()
                                        mixer.Channel(3).play(mixer.Sound(r"C:\Tank_Battle_Simulator\zapsplat_explosions_double_large_explosion_some_very_light_distortion_63287.mp3"))
                                        explosion_img=PhotoImage(file=r"C:\Tank_Battle_Simulator\explosion.png")
                                        real_img=explosion_img.subsample(4, 4)
                                        real_real=canvas.create_image(canvas.coords(player_head)[0], canvas.coords(player_head)[1], image=real_img)
                                        tk.update()
                                        time.sleep(5)
                                        canvas.delete('all')
                                        you_lose=canvas.create_rectangle(0,0,800,800, fill='black', outline='')
                                        you_lose_text=canvas.create_text(400, 200, text='DEFEAT', font=('Calibri', 24), fill='white')
                                        score_text=canvas.create_text(400, 400, text='''Results:\n\nPoints Earned: %s\nTime Bonus: %s\nTotal Score: %s''' % ((50-enemy_hp), (200-timer), ((50-enemy_hp)+(200-timer))), font=('Calibri', 12), fill='white')
                                        tk.clipboard_append('''Results (game lost):\n\nPoints Earned: %s\nTime Bonus: %s\nTotal Score: %s''' % ((50-enemy_hp), (200-timer), ((50-enemy_hp)+(200-timer))))
                                        tk.update()
                                time.sleep(0.1)
                                canvas.delete(enemy_laser)
                                canvas.itemconfig(player_hit_square, fill='yellow')
                                tk.update()
                            elif canvas.itemcget(enemy_head, 'fill')=='yellow':
                                enemy_laser=canvas.create_rectangle(canvas.coords(enemy_parallel_head)[4], canvas.coords(enemy_parallel_head)[5]-1.5, canvas.coords(enemy_parallel_head)[4]+400, canvas.coords(enemy_parallel_head)[5]-2, fill='purple', outline='')
                                mixer.Channel(2).play(mixer.Sound(r"C:\Tank_Battle_Simulator\Laser Blaster-SoundBible.com-1388608841.mp3"))
                                tk.update()
                                if canvas.coords(enemy_body)[2]<canvas.coords(player_body)[0] and canvas.itemcget(player_parallel_shield, 'fill')=='yellow' and canvas.coords(enemy_laser)[2]-20>=canvas.coords(player_head)[0] and canvas.coords(enemy_laser)[3]<=canvas.coords(player_body)[3] and canvas.coords(enemy_laser)[3]+6.5>=canvas.coords(player_head)[1]:
                                    canvas.itemconfig(player_hit_square, fill='red')
                                    player_hp-=1
                                    canvas.delete(player_hp_text)
                                    player_hp_text=canvas.create_text(75, 25, text='Your HP: %s' % player_hp, font=('Calibri', 12))
                                    tk.update()
                                    if player_hp>0:
                                        mixer.Channel(3).play(mixer.Sound(r"C:\Tank_Battle_Simulator\Minecraft-death-sound.mp3"))
                                    elif player_hp<=0:
                                        mixer.pause()
                                        mixer.Channel(3).play(mixer.Sound(r"C:\Tank_Battle_Simulator\zapsplat_explosions_double_large_explosion_some_very_light_distortion_63287.mp3"))
                                        explosion_img=PhotoImage(file=r"C:\Tank_Battle_Simulator\explosion.png")
                                        real_img=explosion_img.subsample(4, 4)
                                        real_real=canvas.create_image(canvas.coords(player_head)[0], canvas.coords(player_head)[1], image=real_img)
                                        tk.update()
                                        time.sleep(5)
                                        canvas.delete('all')
                                        you_lose=canvas.create_rectangle(0,0,800,800, fill='black', outline='')
                                        you_lose_text=canvas.create_text(400, 200, text='DEFEAT', font=('Calibri', 24), fill='white')
                                        score_text=canvas.create_text(400, 400, text='''Results:\n\nPoints Earned: %s\nTime Bonus: %s\nTotal Score: %s''' % ((50-enemy_hp), (200-timer), ((50-enemy_hp)+(200-timer))), font=('Calibri', 12), fill='white')
                                        tk.clipboard_append('''Results (game lost):\n\nPoints Earned: %s\nTime Bonus: %s\nTotal Score: %s''' % ((50-enemy_hp), (200-timer), ((50-enemy_hp)+(200-timer))))
                                        tk.update()
                                    time.sleep(0.1)
                                canvas.delete(enemy_laser)
                                canvas.itemconfig(player_hit_square, fill='yellow')
                                tk.update()
            tk.after(100, ai_code)
        tk.after(100, ai_code)
canvas.bind_all('<KeyPress-Return>', start)
