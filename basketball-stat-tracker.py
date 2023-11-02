import random
import pygame
import tkinter
import pandas as pd
import xlwt
import xlrd
from xlutils.copy import copy

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255,0,0)
blue = (0,0,255)
yellow = (255, 255, 0)
gray = (128, 128, 128)
huge_font = pygame.font.Font('Crimson-Roman.ttf', 36)
instruct_font = pygame.font.Font('Crimson-Roman.ttf', 24)
title_font = pygame.font.Font('freesansbold.ttf', 56)
team1_player_number = 0
team2_player_number = 0
team1 = "Team 1"
team2 = "Team 2"
green_s = 0
sign = 1

board = [[" ", " ", " ", " ", " "," "],
         [" ", " ", " ", " ", " "," "],
         [" ", " ", " ", " ", " "," "],
         [" ", " ", " ", " ", " "," "],
         [" ", " ", " ", " ", " "," "],
         [" ", " ", " ", " ", " "," "]]

board2 = [[" ", " ", " ", " ", " "," "],
         [" ", " ", " ", " ", " "," "],
         [" ", " ", " ", " ", " "," "],
         [" ", " ", " ", " ", " "," "],
         [" ", " ", " ", " ", " "," "],
         [" ", " ", " ", " ", " "," "]]

print("Enter how many players on each team. No more than 6 per team")

team1_player_number = int(input("How many players are on team 1? "))
team2_player_number = int(input("How many players are on team 2? "))
team1_names = []
team2_names = []

team1_stats = [[0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0]]

team2_stats = [[0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0]]

excel_list = [[" ", 0, 0, 0, 0, 0],
              [" ", 0, 0, 0, 0, 0],
              [" ", 0, 0, 0, 0, 0],
              [" ", 0, 0, 0, 0, 0],
              [" ", 0, 0, 0, 0, 0],
              [" ", 0, 0, 0, 0, 0],
              [" ", 0, 0, 0, 0, 0],
              [" ", 0, 0, 0, 0, 0],
              [" ", 0, 0, 0, 0, 0],
              [" ", 0, 0, 0, 0, 0],
              [" ", 0, 0, 0, 0, 0],
              [" ", 0, 0, 0, 0, 0]]

#Getting player names for team 1
print("For team 1:")
for x in range(team1_player_number):
    name = input("What is Player "+ str(x +1) +"'s name? ")
    team1_names.append(name)
    excel_list[x][0] = name
    name = ""
for y in team1_names:
    print(y)

#Getting player names for team 2
print("For team 2:")
for a in range(team2_player_number):
    name = input("What is Player "+ str(a +1) +"'s name? ")
    team2_names.append(name)
    excel_list[a+6][0] = name
    name = ""
for b in team2_names:
    print(b)

print(excel_list)
#Window set up
root = tkinter.Tk()
root.withdraw()
WIDTH = root.winfo_screenwidth()/1.1
HEIGHT = root.winfo_screenheight()/1.1
screen = pygame.display.set_mode((WIDTH, HEIGHT),
                                     pygame.RESIZABLE)
pygame.display.set_caption('Basketball Stats Calculator')
fps = 60
timer = pygame.time.Clock()


current_player = 1
current_stat = 1
check = 1

team1_total = 0
team2_total = 0

running = True
while running:
    timer.tick(fps)
    screen.fill(gray)
    pygame.draw.line(screen,black,[(WIDTH/2),0],[(WIDTH/2),HEIGHT],3)


    #Establishes team 1 left side of the screen
    pygame.draw.rect(screen, gray,[12, 12, 125*6, 75], 3, 5)
    team1_text = title_font.render(team1, True, red)
    screen.blit(team1_text, (282, 25))
    stat1_text = huge_font.render("Points    Assists   Reb.       Steals     Blocks", True, black)
    screen.blit(stat1_text, (137, 125))

    #Establishes team 2 in right side of the screen
    pygame.draw.rect(screen, gray,[(WIDTH/2) + 12, 12, 125*6, 75], 3, 5)
    team2_text = title_font.render(team2, True, blue)
    screen.blit(team2_text, ((WIDTH/2) + 282, 25))
    stat2_text = huge_font.render("Points    Assists   Reb.       Steals     Blocks", True, black)
    screen.blit(stat2_text, ((WIDTH/2) + 137, 125))

    #Team 1 Table set up
    for col in range(0, 6):
        for row in range(0, team1_player_number):
            pygame.draw.rect(screen, white, [col * 120 + 12, (row+2) * 100 + 12 - 50, 125, 75], 3, 5)
            piece_text = huge_font.render(str(board[row][col]), True, black)
            screen.blit(piece_text, (col * 120 + 30, (row+2) * 100 + 25 - 50))
    for row in range(0, team1_player_number):
        board[row][0] = team1_names[row]
    for col in range(1,6):
        for row in range(0, team1_player_number):
            board[row][col] = team1_stats[row][col-1]

    #Team 2 table set up
    for col in range(0, 6):
        for row in range(0, team2_player_number):
            pygame.draw.rect(screen, white, [col * 120 + 12 + (WIDTH/2), (row + 2) * 100 + 12 - 50, 125, 75], 3, 5)
            piece_text = huge_font.render(str(board2[row][col]), True, black)
            screen.blit(piece_text, (col * 120 + 30 + (WIDTH/2), (row + 2) * 100 + 25 - 50))
    for row in range(0, team2_player_number):
        board2[row][0] = str(team2_names[row])
    for col in range(1,6):
        for row in range(0, team2_player_number):
            board2[row][col] = team2_stats[row][col-1]


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                check = 1
                green_s = 0
                print("Current stats is team 1")
            if event.key == pygame.K_w:
                check = 2
                green_s = (WIDTH/2)
                print("Current stats is team 2")
            if event.key == pygame.K_EQUALS:
                sign = 1
            if event.key == pygame.K_MINUS:
                sign = -1
            if event.key == pygame.K_1:
                current_player = 1
            if event.key == pygame.K_2:
                current_player = 2
            if event.key == pygame.K_3:
                current_player = 3
            if event.key == pygame.K_4:
                current_player = 4
            if event.key == pygame.K_5:
                current_player = 5
            if event.key == pygame.K_6:
                current_player = 6

            if event.key == pygame.K_p:
                current_stat = 1
                if check == 1:
                    team1_stats[current_player-1][current_stat-1]+=(1*sign)
                    excel_list[current_player-1][current_stat] = team1_stats[current_player-1][current_stat-1]
                if check == 2:
                    team2_stats[current_player-1][current_stat-1]+=(1*sign)
                    excel_list[5+current_player][current_stat] = team2_stats[current_player - 1][current_stat - 1]

            if event.key == pygame.K_a:
                current_stat = 2
                if check == 1:
                    team1_stats[current_player - 1][current_stat - 1] += (1*sign)
                    excel_list[current_player-1][current_stat] = team1_stats[current_player - 1][current_stat - 1]
                if check == 2:
                    team2_stats[current_player - 1][current_stat - 1] += (1*sign)
                    excel_list[5+current_player][current_stat] = team2_stats[current_player - 1][current_stat - 1]

            if event.key == pygame.K_r:
                current_stat = 3
                if check == 1:
                    team1_stats[current_player - 1][current_stat - 1] += (1*sign)
                    excel_list[current_player-1][current_stat] = team1_stats[current_player - 1][current_stat - 1]
                if check == 2:
                    team2_stats[current_player - 1][current_stat - 1] += (1*sign)
                    excel_list[5+current_player][current_stat] = team2_stats[current_player - 1][current_stat - 1]

            if event.key == pygame.K_s:
                current_stat = 4
                if check == 1:
                    team1_stats[current_player - 1][current_stat - 1] += (1*sign)
                    excel_list[current_player-1][current_stat] = team1_stats[current_player - 1][current_stat - 1]
                if check == 2:
                    team2_stats[current_player - 1][current_stat - 1] += (1*sign)
                    excel_list[5+current_player][current_stat] = team2_stats[current_player - 1][current_stat - 1]

            if event.key == pygame.K_b:
                current_stat = 5
                if check == 1:
                    team1_stats[current_player - 1][current_stat - 1] += (1*sign)
                    excel_list[current_player-1][current_stat] = team1_stats[current_player - 1][current_stat - 1]
                if check == 2:
                    team2_stats[current_player - 1][current_stat - 1] += (1*sign)
                    excel_list[5+current_player][current_stat] = team2_stats[current_player - 1][current_stat - 1]

    pygame.draw.rect(screen, green, [green_s + 12, ((current_player - 1) + 2) * 100 + 12 - 50, 125, 75], 3, 5)
    team1_total = int(team1_stats[0][0]) + int(team1_stats[1][0]) + int(team1_stats[2][0]) + int(team1_stats[3][0]) + int(team1_stats[4][0]) + int(team1_stats[5][0])
    total1_text = title_font.render(str(team1_total), True, red)
    screen.blit(total1_text, (750, 805))

    team2_total = int(team2_stats[0][0]) + int(team2_stats[1][0]) + int(team2_stats[2][0]) + int(team2_stats[3][0]) + int(team2_stats[4][0]) + int(team2_stats[5][0])
    total2_text = title_font.render(str(team2_total), True, blue)
    screen.blit(total2_text, ((WIDTH/2) + ((WIDTH/2)-800), 805))

    t1control_text1 = instruct_font.render("Press 'q' to enter stats for this team ", True, black)
    t1control_text2 = instruct_font.render("To select player, press the number key associated with player ", True, black)
    t1control_text3 = instruct_font.render( "To add/subtract stats, press key associated with first letter of stat", True, black)
    t1control_text5 = instruct_font.render("Note:", True, black)
    t1control_text4 = instruct_font.render("If you want to subtract from stats press '-' and press '=' to change back to adding stats", True, black)
    screen.blit(t1control_text1, (25, 805))
    screen.blit(t1control_text2, (25, 835))
    screen.blit(t1control_text3, (25, 865))
    screen.blit(t1control_text5, (25, 965))
    screen.blit(t1control_text4, (25, 995))

    t2control_text1 = instruct_font.render("Press 'w' to enter stats for this team ", True, black)
    t2control_text2 = instruct_font.render("To select player, press the number key associated with player ", True,
                                           black)
    t2control_text3 = instruct_font.render("To add to stat, press key associated with first letter of stat", True,
                                           black)
    screen.blit(t2control_text1, ((WIDTH/2) +125, 805))
    screen.blit(t2control_text2, ((WIDTH/2) +125, 835))
    screen.blit(t2control_text3, ((WIDTH/2) +125, 865))
    pygame.display.flip()


df = pd.DataFrame (excel_list, columns = ['Name', 'Points', 'Assists', 'Rebounds', 'Steals', 'Blocks'])
print (df)
df.to_excel(r'C:\Users\jacob\Downloads\stats.xlsx', index=False)
pygame.quit()
