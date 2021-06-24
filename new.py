# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 18:03:49 2020

@author: Harsh Chaudhary
"""
import tkinter as tk
import tkinter.ttk as ttk
import sys
import json
import random


json_file = json.load(open(r'D:\updated_files\excelfirstlinedata.json', 'r'))

slot_details = {}
DICT = {'innings': 1}
batsman_selected = False
bowler_selected = False
outZoneCode = {1: 'OFF 1',
               2: 'OFF BACK 1',
               3: 'LEG BACK 2',
               4: 'OFF 2',
               5: 'ST 4',
               6: 'LEG 1',
               7: 'OFF 3',
               8: 'ST 6',
               9: 'LEG 2'}


font9 = "-family {Segoe UI Black} -size 24 -weight bold"
_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9' # X11 color: 'gray85'
_ana1color = '#d9d9d9' # X11 color: 'gray85'
_ana2color = '#ececec' # Closest X11 color: 'gray92'
style = ttk.Style()
if sys.platform == "win32":
    style.theme_use('winnative')
style.configure('.',background=_bgcolor)
style.configure('.',foreground=_fgcolor)
style.configure('.',font="TkDefaultFont")
style.map('.',background=
    [('selected', _compcolor), ('active',_ana2color)])


style.configure('TNotebook.Tab', background=_bgcolor)
style.configure('TNotebook.Tab', foreground=_fgcolor)
style.map('TNotebook.Tab', background=
    [('selected', _compcolor), ('active',_ana2color)])

            
def _1_and_2():
    top = tk.Tk()
    top.geometry("1366x768+637+218")
    
    top.resizable(0, 0)
    top.title("New Toplevel")
    top.configure(background="#d9d9d9")
    
    notebook = ttk.Notebook(top)
    notebook.place(relx=0, rely=0, relheight=1.0, relwidth=1.0)
    
    otp_pane = tk.Frame(notebook)
    
    notebook.add(otp_pane)
    notebook.tab(0, text="ENTER OTP",compound="left",underline="-1",)
    
    team_view_pane = tk.Frame(notebook)
    toss_pane = tk.Frame(notebook)
    decesion_pane = tk.Frame(notebook)
    
    def makeKeyboard():
        def pressed(x):
            if x=='BACK':
                box.delete(1.0, tk.END)
            elif x=='CONFIRM':
                if box.get(1.0, tk.END) in [json_file['booking_data']['prev1_time_slot']['otp_web'], json_file['booking_data']['prev2_time_slot']['otp_web'],
                                            json_file['booking_data']['curr_time_slot']['otp_web']]:
                    validateOtp(int(box.get(1.0, tk.END)), box)
                else:
                    box.delete(1.0, tk.END)
                      
            else:
                box.insert(tk.INSERT, x)
        box = tk.Text(otp_pane, width = 152)
        box.grid(row=0, column=0, columnspan=10)
        buttons = ['A', 'B', 'C', 'D', 'E', 'F', '1', '2', '3',
                   'G', 'H', 'I', 'J', 'K', 'L', '4', '5', '6',
                   'M', 'N', 'O', 'P', 'Q', 'R', '7', '8', '9',
                   'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0',
                   'BACK', 'CONFIRM']
        varRow = 5
        varColumn = 0
        for button in buttons:
            command = lambda x = button:pressed (x)
            if varRow < 9:
                tk.Button(otp_pane, text=button, width = 20, bg='black', fg='white',command=command).grid(row=varRow, column=varColumn)
                varColumn += 1
                if varColumn>8:
                    varColumn=0
                    varRow+=1
            else:
                tk.Button(otp_pane, text=button, width = 192, bg='black', fg='white',command=command).grid(columnspan=9, row=varRow, column=0)
                varRow+=1
    
    def winnerIsBatting():
        DICT['toss_decision'] = 1
        if DICT['toss_winner'] == 1:
            DICT['batting_team'] = 1
        else:
            DICT['batting_team'] = 2
        
    
    def winnerIsBowling():
        DICT['toss_decision'] = 2
        if DICT['toss_winner'] == 1:
            DICT['batting_team'] = 2
        else:
            DICT['batting_team'] = 1

    
    def showDecesionPane():
        notebook.add(decesion_pane)
        notebook.tab(3, text='CHOOSE BAT OR BOWL')
        notebook.hide(2)
    
        batting_button = tk.Button(decesion_pane, command=winnerIsBatting)
        batting_button.place(relx=0.301, rely=0.231, height=93, width=606)
        batting_button.configure(font=font9)
        batting_button.configure(text='''BATTING''')
    
        bowling_button = tk.Button(decesion_pane, command=winnerIsBowling)
        bowling_button.place(relx=0.301, rely=0.395, height=93, width=606)
        bowling_button.configure(font=font9)
        bowling_button.configure(text='''BOWLING''')
    
    
    def openTossPane():
        notebook.add(toss_pane)
        notebook.tab(2, text='TOSS')
        notebook.hide(1)
        winnerteam = tk.Label(toss_pane)
        winnerteam.place(relx=0.400, rely=0.163, height=50, width=299)
        winnerteam.configure(background="#d9d9d9")
        winnerteam.configure(disabledforeground="#a3a3a3")
        winnerteam.configure(font=font9)
        winnerteam.configure(foreground="#000000")
        winner = random.choice(['TEAM A', 'TEAM B'])
        winnerteam.configure(text=winner)
        if winner=='TEAM A':
            DICT['toss_winner'] = 1
        else:
            DICT['toss_winner'] = 2
        wonthetoss = tk.Label(toss_pane)
        wonthetoss.place(relx=0.380, rely=0.271, height=66, width=359)
        wonthetoss.configure(background="#d9d9d9")
        wonthetoss.configure(disabledforeground="#a3a3a3")
        wonthetoss.configure(font=font9)
        wonthetoss.configure(foreground="#000000")
        wonthetoss.configure(text='''WON THE TOSS''')
        
        take_decesion = tk.Button(toss_pane, text='NEXT', width=100, height=5, command=showDecesionPane)
        take_decesion.place(relx = 0.250, rely = 0.4)
    
    def showTeamInfo():
        notebook.add(team_view_pane)
        notebook.tab(1, text="TEAM INFO",compound="left",underline="-1",)
        Label2 = tk.Label(team_view_pane)
        Label2.place(relx=0.11, rely=0.054, height=80, width=336)
        Label2.configure(background="#d9d9d9")
        Label2.configure(disabledforeground="#a3a3a3")
        Label2.configure(font=font9)
        Label2.configure(foreground="#000000")
        Label2.configure(text='''TEAM A''')
    
        Label3 = tk.Label(team_view_pane)
        Label3.place(relx=0.595, rely=0.054, height=80, width=337)
        Label3.configure(background="#d9d9d9")
        Label3.configure(disabledforeground="#a3a3a3")
        Label3.configure(font=font9)
        Label3.configure(foreground="#000000")
        Label3.configure(text='''TEAM B''')
    
        label_p1 = tk.Label(team_view_pane)
        label_p1.place(relx=0.095, rely=0.312, height=50, width=401)
        label_p1.configure(background="#d9d9d9")
        label_p1.configure(disabledforeground="#a3a3a3")
        label_p1.configure(font=font9)
        label_p1.configure(foreground="#000000")
    
    
        label_p2 = tk.Label(team_view_pane)
        label_p2.place(relx=0.095, rely=0.448, height=50, width=401)
        label_p2.configure(activebackground="#f9f9f9")
        label_p2.configure(activeforeground="black")
        label_p2.configure(background="#d9d9d9")
        label_p2.configure(disabledforeground="#a3a3a3")
        label_p2.configure(font="-family {Segoe UI Black} -size 24 -weight bold -slant roman -underline 0 -overstrike 0")
        label_p2.configure(foreground="#000000")
        label_p2.configure(highlightbackground="#d9d9d9")
        label_p2.configure(highlightcolor="black")
    
    
        label_p3 = tk.Label(team_view_pane)
        label_p3.place(relx=0.095, rely=0.583, height=50, width=401)
        label_p3.configure(activebackground="#f9f9f9")
        label_p3.configure(activeforeground="black")
        label_p3.configure(background="#d9d9d9")
        label_p3.configure(disabledforeground="#a3a3a3")
        label_p3.configure(font="-family {Segoe UI Black} -size 24 -weight bold -slant roman -underline 0 -overstrike 0")
        label_p3.configure(foreground="#000000")
        label_p3.configure(highlightbackground="#d9d9d9")
        label_p3.configure(highlightcolor="black")
    
    
        label_p4 = tk.Label(team_view_pane)
        label_p4.place(relx=0.573, rely=0.312, height=50, width=401)
        label_p4.configure(activebackground="#f9f9f9")
        label_p4.configure(activeforeground="black")
        label_p4.configure(background="#d9d9d9")
        label_p4.configure(disabledforeground="#a3a3a3")
        label_p4.configure(font="-family {Segoe UI Black} -size 24 -weight bold -slant roman -underline 0 -overstrike 0")
        label_p4.configure(foreground="#000000")
        label_p4.configure(highlightbackground="#d9d9d9")
        label_p4.configure(highlightcolor="black")
    
    
        label_p5 = tk.Label(team_view_pane)
        label_p5.place(relx=0.573, rely=0.448, height=50, width=401)
        label_p5.configure(activebackground="#f9f9f9")
        label_p5.configure(activeforeground="black")
        label_p5.configure(background="#d9d9d9")
        label_p5.configure(disabledforeground="#a3a3a3")
        label_p5.configure(font="-family {Segoe UI Black} -size 24 -weight bold -slant roman -underline 0 -overstrike 0")
        label_p5.configure(foreground="#000000")
        label_p5.configure(highlightbackground="#d9d9d9")
        label_p5.configure(highlightcolor="black")
    
    
        label_p6 = tk.Label(team_view_pane)
        label_p6.place(relx=0.573, rely=0.583, height=50, width=401)
        label_p6.configure(activebackground="#f9f9f9")
        label_p6.configure(activeforeground="black")
        label_p6.configure(background="#d9d9d9")
        label_p6.configure(disabledforeground="#a3a3a3")
        label_p6.configure(font="-family {Segoe UI Black} -size 24 -weight bold -slant roman -underline 0 -overstrike 0")
        label_p6.configure(foreground="#000000")
        label_p6.configure(highlightbackground="#d9d9d9")
        label_p6.configure(highlightcolor="black")
        
        team_confirm_button = tk.Button(team_view_pane, command=openTossPane)
        team_confirm_button.place(relx=0.396, rely=0.787, height=83, width=266)
        team_confirm_button.configure(text='''Team Confirmed''')
        
        if slot_details['no_of_players']>=2:
            label_p1.configure(text=slot_details['team1']['player1']['player_name'])
            label_p4.configure(text=slot_details['team2']['player1']['player_name'])
        if slot_details['no_of_players']>=4:
            label_p2.configure(text=slot_details['team1']['player2']['player_name'])
            label_p5.configure(text=slot_details['team2']['player2']['player_name'])
        if slot_details['no_of_players']==6:
            label_p3.configure(text=slot_details['team1']['player3']['player_name'])
            label_p6.configure(text=slot_details['team2']['player3']['player_name'])
        notebook.hide(0)
    
    def validateOtp(otp, box):
        global slot_details
        if otp == json_file['booking_data']['prev1_time_slot']['otp_web']:
            slot_details = json_file['booking_data']['prev1_time_slot']
        elif otp == json_file['booking_data']['prev2_time_slot']['otp_web']:
            slot_details = json_file['booking_data']['prev2_time_slot']
        elif otp == json_file['booking_data']['curr_time_slot']['otp_web']:
            slot_details = json_file['booking_data']['curr_time_slot']

        showTeamInfo()
    
    makeKeyboard()
    tk.mainloop()

def _3_4_and_5():
    top = tk.Tk()
    top.geometry("1366x768+637+218")
    
    top.resizable(0, 0)
    top.title("New Toplevel")
    top.configure(background="#d9d9d9")
    
    notebook = ttk.Notebook(top)
    notebook.place(relx=0, rely=0, relheight=1.0, relwidth=1.0)
    notebook.add(tk.Frame(notebook))
            
    batsman_selection_pane = tk.Frame(notebook)
    bowler_selection_pane = tk.Frame(notebook)
    outzone_pane = tk.Frame(notebook)
    screensaver = tk.Frame(notebook)
    
    def screenSaver():
        notebook.add(screensaver, text='GAME ON')
        
        label = tk.Label(screensaver)
        label.place(relx=0.251, rely=0.500, height=96, width=602)
        label.configure(font=font9)
        label.configure(text='''GAME ON''')
    
    def outZoneSelected(id):
        DICT['current_out_zone'] = outZoneCode[id]
        DICT['previously_selected_out_zones'] = DICT.get('previously_selected_out_zones', []) + [outZoneCode[id]]
        notebook.forget(notebook.select())
        screenSaver()
    
    
    def selectOutZone():
        notebook.add(outzone_pane, text='SELECT OUT ZONE')
        notebook.forget(notebook.select())
        
        Button2 = tk.Button(outzone_pane, command=lambda: outZoneSelected(1))
        Button2.place(relx=0.169, rely=0.136, height=83, width=196)
        Button2.configure(activebackground="#ececec")
        Button2.configure(activeforeground="#000000")
        Button2.configure(background="#d9d9d9")
        Button2.configure(disabledforeground="#a3a3a3")
        Button2.configure(foreground="#000000")
        Button2.configure(highlightbackground="#d9d9d9")
        Button2.configure(highlightcolor="black")
        Button2.configure(pady="0")
        Button2.configure(text='''OFF 1''')
    
        Button2_1 = tk.Button(outzone_pane, command=lambda: outZoneSelected(2))
        Button2_1.place(relx=0.419, rely=0.136, height=83, width=196)
        Button2_1.configure(activebackground="#ececec")
        Button2_1.configure(activeforeground="#000000")
        Button2_1.configure(background="#d9d9d9")
        Button2_1.configure(disabledforeground="#a3a3a3")
        Button2_1.configure(foreground="#000000")
        Button2_1.configure(highlightbackground="#d9d9d9")
        Button2_1.configure(highlightcolor="black")
        Button2_1.configure(pady="0")
        Button2_1.configure(text='''OFF BACK 1''')
    
        Button2_2 = tk.Button(outzone_pane, command=lambda: outZoneSelected(3))
        Button2_2.place(relx=0.675, rely=0.136, height=83, width=196)
        Button2_2.configure(activebackground="#ececec")
        Button2_2.configure(activeforeground="#000000")
        Button2_2.configure(background="#d9d9d9")
        Button2_2.configure(disabledforeground="#a3a3a3")
        Button2_2.configure(foreground="#000000")
        Button2_2.configure(highlightbackground="#d9d9d9")
        Button2_2.configure(highlightcolor="black")
        Button2_2.configure(pady="0")
        Button2_2.configure(text='''LEG BACK 2''')
    
        Button2_3 = tk.Button(outzone_pane, command=lambda: outZoneSelected(4))
        Button2_3.place(relx=0.172, rely=0.305, height=83, width=196)
        Button2_3.configure(activebackground="#ececec")
        Button2_3.configure(activeforeground="#000000")
        Button2_3.configure(background="#d9d9d9")
        Button2_3.configure(disabledforeground="#a3a3a3")
        Button2_3.configure(foreground="#000000")
        Button2_3.configure(highlightbackground="#d9d9d9")
        Button2_3.configure(highlightcolor="black")
        Button2_3.configure(pady="0")
        Button2_3.configure(text='''OFF 2''')
    
        Button2_4 = tk.Button(outzone_pane, command=lambda: outZoneSelected(5))
        Button2_4.place(relx=0.42, rely=0.297, height=83, width=196)
        Button2_4.configure(activebackground="#ececec")
        Button2_4.configure(activeforeground="#000000")
        Button2_4.configure(background="#d9d9d9")
        Button2_4.configure(disabledforeground="#a3a3a3")
        Button2_4.configure(foreground="#000000")
        Button2_4.configure(highlightbackground="#d9d9d9")
        Button2_4.configure(highlightcolor="black")
        Button2_4.configure(pady="0")
        Button2_4.configure(text='''ST 4''')
    
        Button2_5 = tk.Button(outzone_pane, command=lambda: outZoneSelected(6))
        Button2_5.place(relx=0.675, rely=0.292, height=83, width=196)
        Button2_5.configure(activebackground="#ececec")
        Button2_5.configure(activeforeground="#000000")
        Button2_5.configure(background="#d9d9d9")
        Button2_5.configure(disabledforeground="#a3a3a3")
        Button2_5.configure(foreground="#000000")
        Button2_5.configure(highlightbackground="#d9d9d9")
        Button2_5.configure(highlightcolor="black")
        Button2_5.configure(pady="0")
        Button2_5.configure(text='''LEG 1''')
    
        Button2_6 = tk.Button(outzone_pane, command=lambda: outZoneSelected(7))
        Button2_6.place(relx=0.173, rely=0.469, height=83, width=196)
        Button2_6.configure(activebackground="#ececec")
        Button2_6.configure(activeforeground="#000000")
        Button2_6.configure(background="#d9d9d9")
        Button2_6.configure(disabledforeground="#a3a3a3")
        Button2_6.configure(foreground="#000000")
        Button2_6.configure(highlightbackground="#d9d9d9")
        Button2_6.configure(highlightcolor="black")
        Button2_6.configure(pady="0")
        Button2_6.configure(text='''OFF 3''')
    
        Button2_7 = tk.Button(outzone_pane, command=lambda: outZoneSelected(8))
        Button2_7.place(relx=0.421, rely=0.465, height=83, width=196)
        Button2_7.configure(activebackground="#ececec")
        Button2_7.configure(activeforeground="#000000")
        Button2_7.configure(background="#d9d9d9")
        Button2_7.configure(disabledforeground="#a3a3a3")
        Button2_7.configure(foreground="#000000")
        Button2_7.configure(highlightbackground="#d9d9d9")
        Button2_7.configure(highlightcolor="black")
        Button2_7.configure(pady="0")
        Button2_7.configure(text='''ST 6''')
    
        Button2_8 = tk.Button(outzone_pane, command=lambda: outZoneSelected(9))
        Button2_8.place(relx=0.676, rely=0.459, height=83, width=196)
        Button2_8.configure(activebackground="#ececec")
        Button2_8.configure(activeforeground="#000000")
        Button2_8.configure(background="#d9d9d9")
        Button2_8.configure(disabledforeground="#a3a3a3")
        Button2_8.configure(foreground="#000000")
        Button2_8.configure(highlightbackground="#d9d9d9")
        Button2_8.configure(highlightcolor="black")
        Button2_8.configure(pady="0")
        Button2_8.configure(text='''LEG 2''')
    
    def bowlerSelected():
        global bowler_selected
        bowler_selected = True
        if not batsman_selected:
            chooseBatsman()
        else:
            selectOutZone()
    def batsmanSelected():
        global batsman_selected
        batsman_selected = True
        if not bowler_selected:
            chooseBowler()
        else:
            selectOutZone()
    
    def batsman1Selected():
        print('Clicked')
        batsman_1['state'] = 'disabled'
        DICT['current_batsman'] = batsman_1['text']
        batsmanSelected()
    def batsman2Selected():
        batsman_2['state'] = 'disabled'
        DICT['current_batsman'] = batsman_2['text']
        batsmanSelected()
    def batsman3Selected():
        batsman_3['state'] = 'disabled'
        DICT['current_batsman'] = batsman_3['text']
        batsmanSelected()
    
    def bowler1Selected():
        print('Clicked')
        bowler_1['state'] = 'disabled'
        bowler_2['state'] = 'normal'
        bowler_3['state'] = 'normal'
        DICT['current_bowler'] = bowler_1['text']
        bowlerSelected()
    def bowler2Selected():
        bowler_1['state'] = 'normal'
        bowler_2['state'] = 'disabled'
        bowler_3['state'] = 'normal'
        DICT['current_bowler'] = bowler_2['text']
        bowlerSelected()
    def bowler3Selected():
        bowler_1['state'] = 'normal'
        bowler_2['state'] = 'normal'
        bowler_3['state'] = 'disabled'
        DICT['current_bowler'] = bowler_3['text']
        bowlerSelected()
    
    batsman_1 = tk.Button(batsman_selection_pane, command=batsman1Selected)
    batsman_1.place(relx=0.301, rely=0.271, height=93, width=606)
    batsman_1.configure(font=font9)
    
    
    batsman_2 = tk.Button(batsman_selection_pane, command=batsman2Selected)
    batsman_2.place(relx=0.301, rely=0.407, height=93, width=606)
    batsman_2.configure(font=font9)
    
    
    batsman_3 = tk.Button(batsman_selection_pane, command=batsman3Selected)
    batsman_3.place(relx=0.301, rely=0.543, height=93, width=606)
    batsman_3.configure(font="-family {Segoe UI Black} -size 24 -weight bold -slant roman -underline 0 -overstrike 0")
    
    
    bowler_1 = tk.Button(bowler_selection_pane, command=bowler1Selected)
    bowler_1.place(relx=0.301, rely=0.271, height=93, width=606)
    bowler_1.configure(font=font9)
    
    
    bowler_2 = tk.Button(bowler_selection_pane, command=bowler2Selected)
    bowler_2.place(relx=0.301, rely=0.407, height=93, width=606)
    bowler_2.configure(font=font9)
    
    
    bowler_3 = tk.Button(bowler_selection_pane, command=bowler3Selected)
    bowler_3.place(relx=0.301, rely=0.543, height=93, width=606)
    bowler_3.configure(font="-family {Segoe UI Black} -size 24 -weight bold -slant roman -underline 0 -overstrike 0")
    
    def chooseBatsman():
        notebook.add(batsman_selection_pane, text='BOWLING TEAM')
        notebook.forget(notebook.select())
        
        Label1 = tk.Label(batsman_selection_pane)
        Label1.place(relx=0.301, rely=0.054, height=96, width=602)
        Label1.configure(font=font9)
        Label1.configure(text='''SELECT A PLAYER TO BAT''')

            
    
    def chooseBowler():
        notebook.add(bowler_selection_pane, text='BOWLING TEAM')
        notebook.forget(notebook.select())
        
        Label1 = tk.Label(bowler_selection_pane)
        Label1.place(relx=0.301, rely=0.054, height=96, width=602)
        Label1.configure(font=font9)
        Label1.configure(text='SELECT A PLAYER TO BOWL')
    
    def setNameOnButtons():
        if slot_details['no_of_players']>=2:
            if DICT['batting_team']==1:
                batsman_2.configure(text=slot_details['team1']['player1']['player_name'])
                bowler_2.configure(text=slot_details['team2']['player1']['player_name'])
            else:
                batsman_2.configure(text=slot_details['team2']['player1']['player_name'])
                bowler_2.configure(text=slot_details['team1']['player1']['player_name'])
        if slot_details['no_of_players']>=4:
            if DICT['batting_team']==1:
                batsman_3.configure(text=slot_details['team1']['player2']['player_name'])
                bowler_3.configure(text=slot_details['team2']['player2']['player_name'])
            else:
                batsman_3.configure(text=slot_details['team2']['player2']['player_name'])
                bowler_3.configure(text=slot_details['team1']['player2']['player_name'])
        if slot_details['no_of_players']==6:
            if DICT['batting_team']==1:
                batsman_1.configure(text=slot_details['team1']['player3']['player_name'])
                bowler_1.configure(text=slot_details['team2']['player3']['player_name'])
            else:
                batsman_1.configure(text=slot_details['team2']['player3']['player_name'])
                bowler_1.configure(text=slot_details['team1']['player3']['player_name'])
    
    setNameOnButtons()
    if slot_details['no_of_players']<6:
        batsman_1.place_forget()
        bowler_1.place_forget()
    if slot_details['no_of_players']<4:
        batsman_3.place_forget()
        bowler_3.place_forget()
    
    if DICT['batting_team'] == 1:
        chooseBatsman()
    else:
        chooseBowler()
        
    tk.mainloop()
    
    
_1_and_2()
_3_4_and_5()