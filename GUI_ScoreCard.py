import tkinter as tk
import tkinter.ttk as ttk
import time

import json


font15 = "-family {Segoe UI Black} -size 24 -weight bold"
font17 = "-family {Segoe UI Black} -size 15 -weight bold"

        
top = tk.Tk()
top.geometry("1307x650+321+188")
top.minsize(148, 1)
top.maxsize(1924, 1055)
top.resizable(1, 1)
top.title("Scorecard")
top.configure(background="#ffffff")


# def hide():
#     Label1.configure(text='')
    
# def show():
#     global top
#     Label1.configure(text='Clicked !')
#     top.after(2000, unclick)

import yaml
#Enter file location here
file = open(r'D:\updated_files\done_sample.yaml', 'r')
obj = yaml.load(file, Loader=yaml.FullLoader)
#read current slot
currentSlot = obj['info']['slots'][-1]

#open json and collect player details
json_file = json.load(open(r'D:\updated_files\excelfirstlinedata.json', 'r'))

slot_details = {}

if currentSlot == json_file['booking_data']['prev1_time_slot']['otp_web']:
    slot_details = json_file['booking_data']['prev1_time_slot']
elif currentSlot == json_file['booking_data']['prev2_time_slot']['otp_web']:
    slot_details = json_file['booking_data']['prev2_time_slot']
else:
    slot_details = json_file['booking_data']['curr_time_slot']

team_1 = {slot_details['team1']['player1']['player_id']: slot_details['team1']['player1']['player_name'],
          slot_details['team1']['player2']['player_id']: slot_details['team1']['player2']['player_name']}

team_2 = {slot_details['team2']['player1']['player_id']: slot_details['team2']['player1']['player_name'],
          slot_details['team2']['player2']['player_id']: slot_details['team2']['player2']['player_name']}   

#pointers for batting and bowling team
bat_team = None
bowl_team = None

#finding out the innings
innings = obj['info']['innings']
if innings == 1:
    innings_info = obj['innings']['first_innings']
elif innings == 2:
    innings_info = obj['innings']['second_innings']
elif innings == 3:
    innings_info = obj['innings']['third_innings']
else:
    innings_info = obj['innings']['fourth_innings']
 
# variables to hold scores and wickets and deliveries
score = list(innings_info['deliveries'][-1].values())[0]['score_after']
wickets = list(innings_info['deliveries'][-1].values())[0]['wic_after']
deliveries = list(innings_info['deliveries'][-1].values())[0]['valid_ball_no']


bat_team_name = ""
bowl_team_name = ''

#knowing the batting team and setting bat team name
batting_team_no = innings_info['batteam']
if batting_team_no == '1':
    bat_team_name += slot_details['team1']['player1']['player_name'][0:2] + slot_details['team1']['player2']['player_name'][0:2]
    bat_team = team_1
    bowl_team = team_2
else:
    bat_team_name += slot_details['team2']['player1']['player_name'][0:2] + slot_details['team2']['player2']['player_name'][0:2]
    bat_team = team_2
    bowl_team = team_1


#knowing batsman and bowler name
curr_batsman = None
curr_bowler = None

if list(innings_info['deliveries'][-1].values())[0]['batsman_player_id'] in team_1:
    curr_batsman = team_1[list(innings_info['deliveries'][-1].values())[0]['batsman_player_id']]
else:
    curr_batsman = team_2[list(innings_info['deliveries'][-1].values())[0]['batsman_player_id']]

if list(innings_info['deliveries'][-1].values())[0]['bowler_player_id'] in team_1:
    curr_bowler = team_1[list(innings_info['deliveries'][-1].values())[0]['bowler_player_id']]
else:
    curr_bowler = team_2[list(innings_info['deliveries'][-1].values())[0]['bowler_player_id']]

runs_scored_by_curr_batsman = 0
bowls_faced_by_curr_batsman = 0

runs_given_by_current_bowler = 0
deliveries_done_by_current_bowler = 0

curr_bowl_id = list(innings_info['deliveries'][-1].values())[0]['bowler_player_id']
curr_batsman_id = list(innings_info['deliveries'][-1].values())[0]['batsman_player_id']

#loop for batsman'stats
i=-1
total_deliveries = len(innings_info['deliveries'])
while i>=-total_deliveries and list(innings_info['deliveries'][-1].values())[0]['batsman_player_id'] == list(innings_info['deliveries'][i].values())[0]['batsman_player_id']:
    if list(innings_info['deliveries'][i].values())[0]['valid_ball_no']>0:
        deliveries_done_by_current_bowler +=1
    runs_given_by_current_bowler += list(innings_info['deliveries'][i].values())[0]['runs']['total']
    
    i-=1

#loop for bowler's runs
i=-1
total_deliveries = len(innings_info['deliveries'])
while i>=-total_deliveries and list(innings_info['deliveries'][-1].values())[0]['bowler_player_id'] == list(innings_info['deliveries'][i].values())[0]['bowler_player_id']:
    bowls_faced_by_curr_batsman +=1
    runs_scored_by_curr_batsman += list(innings_info['deliveries'][i].values())[0]['runs']['batsman']
    
    i-=1    

runsWicket = tk.Label(top)
runsWicket.place(relx=0.004, rely=0.0, height=276, width=336)
runsWicket.configure(activebackground="#0080c0")
runsWicket.configure(activeforeground="white")
runsWicket.configure(activeforeground="#ffffff")
runsWicket.configure(background="#0080c0")
runsWicket.configure(disabledforeground="#a3a3a3")
runsWicket.configure(font="-family {Segoe UI Black} -size 85 -weight bold")
runsWicket.configure(foreground="#ffffff")
runsWicket.configure(text=str(score) + "/" + str(wickets))

teamName = tk.Label(top)
teamName.place(relx=0.265, rely=0.0, height=139, width=552)
teamName.configure(background="#0080c0")
teamName.configure(disabledforeground="#a3a3a3")
teamName.configure(font="-family {Segoe UI Black} -size 50 -weight bold")
teamName.configure(foreground="#ffffff")
teamName.configure(text=bat_team_name+' (Inn ' +str(innings) +')')

overs = tk.Label(top)
overs.place(relx=0.265, rely=0.22, height=132, width=552)
overs.configure(activebackground="#f9f9f9")
overs.configure(activeforeground="black")
overs.configure(background="#b6cdcf")
overs.configure(disabledforeground="#3c3c3c")
overs.configure(font="-family {Segoe UI Black} -size 24 -weight bold -slant roman -underline 0 -overstrike 0")
overs.configure(foreground="#383838")
overs.configure(highlightbackground="#d9d9d9")
overs.configure(highlightcolor="black")
overs.configure(text='                 overs ('+ str(obj['info']['overs']) +')')

ovr = tk.Label(overs)
ovr.place(relx=0.120, rely=0.05, height=100, width=190)
ovr.configure(background="#b6cdcf")
ovr.configure(font="-family {Segoe UI Black} -size 90 -weight bold -slant roman -underline 0 -overstrike 0")
ovr.configure(foreground="#383838")
ovr.configure(text = str(deliveries//6) + "." + str(deliveries%6))

Bt1 = tk.Label(top)
Bt1.place(relx=0.159, rely=0.431, height=95, width=690)
Bt1.configure(background="#e0e0e0")
Bt1.configure(disabledforeground="#a3a3a3")
Bt1.configure(font=font15)
Bt1.configure(foreground="#383838")
Bt1.configure(text=curr_batsman + " " + str(runs_scored_by_curr_batsman) +" ("+str(bowls_faced_by_curr_batsman) + ')')

Bt2 = tk.Label(top)
Bt2.place(relx=0.159, rely=0.585, height=95, width=691)
Bt2.configure(activebackground="#f9f9f9")
Bt2.configure(activeforeground="black")
Bt2.configure(background="#c7d5d8")
Bt2.configure(disabledforeground="#a3a3a3")
Bt2.configure(font="-family {Segoe UI Black} -size 24 -weight bold -slant roman -underline 0 -overstrike 0")
Bt2.configure(foreground="#383838")
Bt2.configure(highlightbackground="#d9d9d9")
Bt2.configure(highlightcolor="black")
Bt2.configure(text=curr_bowler +" " + str(deliveries_done_by_current_bowler//6) +'.' + str(deliveries_done_by_current_bowler%6) +" ("+str(runs_given_by_current_bowler) + ')')

on_last_bowl = list(innings_info['deliveries'][-1].values())[0]['runs']['total'] 
lastbowl = tk.Label(top)
lastbowl.place(relx=0.692, rely=0.288, height=230, width=396)
lastbowl.configure(background="#000000")
lastbowl.configure(disabledforeground="#a3a3a3")
lastbowl.configure(font="-family {Segoe UI Black} -size 105 -weight bold")
lastbowl.configure(foreground="#ab0321")
lastbowl.configure(text=str(on_last_bowl))

prevBowl = tk.Label(top)
prevBowl.place(relx=0.692, rely=0.645, height=56, width=395)
prevBowl.configure(background="#0080c0")
prevBowl.configure(disabledforeground="#a3a3a3")
prevBowl.configure(font=font17)
prevBowl.configure(foreground="#ffffff")
prevBowl.configure(text='''Previous Bowl''')

    

innings_1 = tk.Label(top)
innings_1.place(relx=0.691, rely=0.003, height=57, width=399)
innings_1.configure(background="#c7d5d8")
innings_1.configure(disabledforeground="#a3a3a3")
innings_1.configure(font="-family {Segoe UI Black} -size 14 -weight bold -slant roman -underline 0 -overstrike 0")
innings_1.configure(foreground="#383838")

    

innings_2 = tk.Label(top)
innings_2.place(relx=0.691, rely=0.098, height=58, width=399)
innings_2.configure(activebackground="#f9f9f9")
innings_2.configure(activeforeground="black")
innings_2.configure(background="#d9d9d9")
innings_2.configure(disabledforeground="#a3a3a3")
innings_2.configure(font="-family {Segoe UI Black} -size 14 -weight bold -slant roman -underline 0 -overstrike 0")
innings_2.configure(foreground="#383838")
innings_2.configure(highlightbackground="#d9d9d9")
innings_2.configure(highlightcolor="black")


innings_3 = tk.Label(top)
innings_3.place(relx=0.691, rely=0.194, height=57, width=399)
innings_3.configure(activebackground="#f9f9f9")
innings_3.configure(activeforeground="black")
innings_3.configure(background="#c7d5d8")
innings_3.configure(disabledforeground="#a3a3a3")
innings_3.configure(font="-family {Segoe UI Black} -size 14 -weight bold -slant roman -underline 0 -overstrike 0")
innings_3.configure(foreground="#383838")
innings_3.configure(highlightbackground="#d9d9d9")
innings_3.configure(highlightcolor="black")

def findBatTeamName(innings):
    if innings == 1:
        batting_team_no = obj['innings']['first_innings']['batteam']
        if batting_team_no == '1':
            return slot_details['team1']['player1']['player_name'][0:2] + slot_details['team1']['player2']['player_name'][0:2]
        else:
            return slot_details['team2']['player1']['player_name'][0:2] + slot_details['team2']['player2']['player_name'][0:2]
    elif innings == 2:
        batting_team_no = obj['innings']['second_innings']['batteam']
        if batting_team_no == '1':
            return slot_details['team1']['player1']['player_name'][0:2] + slot_details['team1']['player2']['player_name'][0:2]
        else:
            return slot_details['team2']['player1']['player_name'][0:2] + slot_details['team2']['player2']['player_name'][0:2]
    else:
        batting_team_no = obj['innings']['third_innings']['batteam']
        if batting_team_no == '1':
            return slot_details['team1']['player1']['player_name'][0:2] + slot_details['team1']['player2']['player_name'][0:2]
        else:
            return slot_details['team2']['player1']['player_name'][0:2] + slot_details['team2']['player2']['player_name'][0:2]

def findInningScore(innings):
    if innings == 1:
        return list(obj['innings']['first_innings']['deliveries'][-1].values())[0]['score_after']
    elif innings == 2:
        return list(obj['innings']['second_innings']['deliveries'][-1].values())[0]['score_after']
    else:
        return list(obj['innings']['third_innings']['deliveries'][-1].values())[0]['score_after']

def findInningWickets(innings):
    if innings == 1:
        return list(obj['innings']['first_innings']['deliveries'][-1].values())[0]['wic_after']
    elif innings == 2:
        return list(obj['innings']['second_innings']['deliveries'][-1].values())[0]['wic_after']
    else:
        return list(obj['innings']['third_innings']['deliveries'][-1].values())[0]['wic_after']

def findInningOvers(innings):
    if innings == 1:
        return str( list(obj['innings']['first_innings']['deliveries'][-1].values())[0]['valid_ball_no']//6) + '.' + str(list(obj['innings']['first_innings']['deliveries'][-1].values())[0]['valid_ball_no']%6)
    elif innings == 2:
        return str(list(obj['innings']['second_innings']['deliveries'][-1].values())[0]['valid_ball_no']//6) + '.' + str(list(obj['innings']['second_innings']['deliveries'][-1].values())[0]['valid_ball_no']%6)
    else:
        return str(list(obj['innings']['third_innings']['deliveries'][-1].values())[0]['valid_ball_no']//6) + '.' + str(list(obj['innings']['third_innings']['deliveries'][-1].values())[0]['valid_ball_no']%6)

#setting innings scores!
if innings == 1:
    innings_1.configure(text='''Innings 1: On going...''')
    innings_2.configure(text='''Innings 2: Upcoming''')
    innings_3.configure(text='''Innings 3: Upcoming''')
elif innings == 2:
    innings_1.configure(text='Innings 1: ' + findBatTeamName(1) +' ' + str(findInningScore(1)) + "/" + str(findInningWickets(1)) + ' ' + '(' +findInningOvers(1) +')')
    innings_2.configure(text='Innings 2: On going...')
    innings_3.configure(text='''Innings 3: Upcoming''')
elif innings == 3:
    innings_1.configure(text='Innings 1: ' + findBatTeamName(1) +' ' + str(findInningScore(1)) + "/" + str(findInningWickets(1)) + ' ' + '(' +findInningOvers(1) +')')
    innings_2.configure(text='Innings 2: ' + findBatTeamName(2) +' ' + str(findInningScore(2)) + "/" + str(findInningWickets(2)) + ' ' + '(' +findInningOvers(2) +')')
    innings_3.configure(text='Innings 3: On going...')
else:
    innings_1.configure(text='Innings 1: ' + findBatTeamName(1) +' ' + str(findInningScore(1)) + "/" + str(findInningWickets(1)) + ' ' + '(' +findInningOvers(1) +')')
    innings_2.configure(text='Innings 2: ' + findBatTeamName(2) +' ' + str(findInningScore(2)) + "/" + str(findInningWickets(2)) + ' ' + '(' +findInningOvers(2) +')')
    innings_3.configure(text='Innings 3: ' + findBatTeamName(3) +' ' + str(findInningScore(3)) + "/" + str(findInningWickets(3)) + ' ' + '(' +findInningOvers(3) +')')

#for innings 1 and 3
if innings == 1 or innings == 3:
    toss_winner = ''
    decision = ''
    if obj['info']['toss_winner'] == 1 and obj['info']['toss_decision'] == 1:
        toss_winner = slot_details['team1']['player1']['player_name'][0:2] + slot_details['team1']['player2']['player_name'][0:2]
        decision = 'BAT'
    elif obj['info']['toss_winner'] == 1 and obj['info']['toss_decision'] == 2:
        toss_winner = slot_details['team1']['player1']['player_name'][0:2] + slot_details['team1']['player2']['player_name'][0:2]
        decision = 'BOWL'
    elif obj['info']['toss_winner'] == 2 and obj['info']['toss_decision'] == 1:
        toss_winner = slot_details['team2']['player1']['player_name'][0:2] + slot_details['team2']['player2']['player_name'][0:2]
        decision = 'BAT'
    else:
        toss_winner = slot_details['team2']['player1']['player_name'][0:2] + slot_details['team2']['player2']['player_name'][0:2]
        decision = 'BOWL'
        
    target = tk.Label(top)
    target.place(relx=0.005, rely=0.738, height=165, width=1291)
    target.configure(background="#0080c0")
    target.configure(disabledforeground="#a3a3a3")
    target.configure(font="-family {Segoe UI Black} -size 40 -weight bold")
    target.configure(foreground="#ffffff")
    target.configure(text=toss_winner + ' has won the toss and elected to ' + decision)    
else:
    
    Canvas1 = tk.Canvas(top)
    Canvas1.place(relx=0.003, rely=0.738, relheight=0.257, relwidth=0.992)
    Canvas1.configure(background="#0080c0")
    Canvas1.configure(cursor="fleur")
    Canvas1.configure(insertbackground="black")
    Canvas1.configure(relief="ridge")
    Canvas1.configure(selectbackground="blue")
    Canvas1.configure(selectforeground="white")
    
    batingTeam = tk.Label(Canvas1)
    batingTeam.place(relx=0.080, rely=0.300, height=66, width=133)
    batingTeam.configure(background="#0080c0")
    batingTeam.configure(disabledforeground="#a3a3a3")
    batingTeam.configure(font="-family {Segoe UI Black} -size 45 -weight bold")
    batingTeam.configure(foreground="#ffffff")
    batingTeam.configure(text=bat_team_name)
    
    need = tk.Label(Canvas1)
    need.place(relx=0.202, rely=0.300, height=66, width=145)
    need.configure(activebackground="#f9f9f9")
    need.configure(activeforeground="black")
    need.configure(background="#0080c0")
    need.configure(disabledforeground="#a3a3a3")
    need.configure(font="-family {Segoe UI Black} -size 45 -weight bold")
    need.configure(foreground="#ffffff")
    need.configure(highlightbackground="#d9d9d9")
    need.configure(highlightcolor="black")
    need.configure(text='''need''')
    
    req_runs = tk.Label(Canvas1)
    req_runs.place(relx=0.325, rely=0.120, height=120, width=150)
    req_runs.configure(activebackground="#f9f9f9")
    req_runs.configure(activeforeground="black")
    req_runs.configure(background="#0080c0")
    req_runs.configure(disabledforeground="#a3a3a3")
    req_runs.configure(font="-family {Segoe UI Black} -size 95 -weight bold")
    req_runs.configure(foreground="#ffffff")
    req_runs.configure(highlightbackground="#d9d9d9")
    req_runs.configure(highlightcolor="black")
    req_runs.configure(text=str(int(findInningScore(innings-1)) - score))
    
    runsoff = tk.Label(Canvas1)
    runsoff.place(relx=0.450, rely=0.200, height=100, width=250)
    runsoff.configure(activebackground="#f9f9f9")
    runsoff.configure(activeforeground="black")
    runsoff.configure(background="#0080c0")
    runsoff.configure(disabledforeground="#a3a3a3")
    runsoff.configure(font="-family {Segoe UI Black} -size 45 -weight bold")
    runsoff.configure(foreground="#ffffff")
    runsoff.configure(highlightbackground="#d9d9d9")
    runsoff.configure(highlightcolor="black")
    runsoff.configure(text='''runs off''')
    
    
    ballLeft = tk.Label(Canvas1)
    ballLeft.place(relx=0.670, rely=0.120, height=120, width=150)
    ballLeft.configure(activebackground="#f9f9f9")
    ballLeft.configure(activeforeground="black")
    ballLeft.configure(background="#0080c0")
    ballLeft.configure(cursor="fleur")
    ballLeft.configure(disabledforeground="#a3a3a3")
    ballLeft.configure(font="-family {Segoe UI Black} -size 95 -weight bold")
    ballLeft.configure(foreground="#ffffff")
    ballLeft.configure(highlightbackground="#d9d9d9")
    ballLeft.configure(highlightcolor="black")
    ballLeft.configure(text= str(24-deliveries))
    
    balls = tk.Label(Canvas1)
    balls.place(relx=0.800, rely=0.299, height=66, width=150)
    balls.configure(activebackground="#f9f9f9")
    balls.configure(activeforeground="black")
    balls.configure(background="#0080c0")
    balls.configure(disabledforeground="#a3a3a3")
    balls.configure(font="-family {Segoe UI Black} -size 45 -weight bold")
    balls.configure(foreground="#ffffff")
    balls.configure(highlightbackground="#d9d9d9")
    balls.configure(highlightcolor="black")
    balls.configure(text='''balls''')




top.mainloop()

