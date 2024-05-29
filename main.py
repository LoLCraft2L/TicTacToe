#importing stuff
import pygame
import random

#Initialization
screen_width = 400
screen_height = 400
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption("TicTacToe")
run = True

#Set-ups 
#Board
line_width = 5
color = (255,255,255)
def draw_board():


    for x in range(1,3):
        pygame.draw.line(screen,color,(x*133,0),(x*133,screen_width),line_width)
        pygame.draw.line(screen,color,(0,x*133),(screen_height,x*133),line_width)
#Players
choices = [1,-1]
player = random.choice(choices)

#Placement in board
board = []
for i in range(3):
    board.append([0]*3)
def draw_XO():


    x_pos = 0
    for x in board:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen,color,(x_pos*133+30,y_pos*133+30),(x_pos*133+90,y_pos*133+90),line_width)
                pygame.draw.line(screen,color,(x_pos*133+30,y_pos*133+90),(x_pos*133+90,y_pos*133+30),line_width)
            elif y == -1:
                radius = 40
                pygame.draw.circle(screen,color,(x_pos*133+64,y_pos*133+64),radius,line_width)
            y_pos += 1
        x_pos+=1

#Check winner
def check_winner():

    
    y_pos = 0
    for x in board:
        #Columns
        if sum(x) == 3:
            print("X wins")
            run = False
        elif sum(x) == -3:
            print("O wins")
            run = False
        #Rows
        elif board[0][y_pos] + board[1][y_pos] + board[2][y_pos] == 3:
            print("X wins")
            run = False
        elif board[0][y_pos] + board[1][y_pos] + board[2][y_pos] == -3:
            print("O Wins")
            run = False
        y_pos += 1
    
    #Diagonals
    if (board[0][0] + board[1][1] + board[2][2] == 3) or (board[0][2] + board[1][1] + board[2][0] == 3):
        print("X Wins")
        run = False
    elif(board[0][0] + board[1][1] + board[2][2] == -3) or (board[0][2] + board[1][1] + board[2][0] == -3):
        print("O Wins")
        run = False
    
                

#Graphics
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if board[mouse_pos[0] // 133][mouse_pos[1] // 133] == 0:
                board[mouse_pos[0] // 133][mouse_pos[1]//133] = player
                player *= -1
                check_winner()

    draw_board()
    draw_XO()
    pygame.display.update()
    clock.tick(60)

if not run:
    pygame.quit()