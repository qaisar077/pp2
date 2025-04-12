import pygame
pygame.init() 

clock = pygame.time.Clock()
WIDTH = 640
HEIGHT = 480

LMBpressed = False
THICKNESS = 5
colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

currX = 0
currY = 0
palette=0
prevX = 0
prevY = 0
FPS = 60 
current_shape = "rect" 
colors=[colorRED, colorBLUE, colorWHITE] 
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
base_layer = pygame.Surface((WIDTH, HEIGHT)) 

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2)) 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed!")
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1] 
        
        if event.type == pygame.MOUSEMOTION:
            print("Position of the mouse:", event.pos)
            if LMBpressed:
                currX = event.pos[0]
                currY = event.pos[1] 
                screen.blit(base_layer, (0, 0))  
                if current_shape=="rect":
                    pygame.draw.rect(screen, colors[palette], calculate_rect(prevX, prevY, currX, currY), THICKNESS) 
                elif current_shape=='circle':
                    pygame.draw.circle(screen, colors[palette],  (prevX, prevY), int(((currX - prevX)**2 + (currY - prevY)**2)**0.5), THICKNESS)
                elif current_shape == "eraser":
                    pygame.draw.rect(screen, colorBLACK, calculate_rect(prevX, prevY, currX, currY))  
                pygame.display.flip()  
            
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released!")
            LMBpressed = False 
            currX = event.pos[0]
            currY = event.pos[1]
            if current_shape=="rect":
                    pygame.draw.rect(screen, colors[palette], calculate_rect(prevX, prevY, currX, currY), THICKNESS)  
            elif current_shape=='circle':
                    pygame.draw.circle(screen, colors[palette],  (prevX, prevY), int(((currX - prevX)**2 + (currY - prevY)**2)**0.5), THICKNESS) 
            elif current_shape == "eraser":
                pygame.draw.rect(screen, colorBLACK, calculate_rect(prevX, prevY, currX, currY))  
            base_layer.blit(screen, (0, 0))  
        
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_EQUALS:  
                print("increased thickness")
                THICKNESS += 1  
            if event.key == pygame.K_MINUS:
                print("reduced thickness")
                THICKNESS-=1  
            if event.key == pygame.K_r:  
                print("Switched to rectangle mode")
                current_shape = "rect"
            if event.key == pygame.K_c:  
                print("Switched to circle mode")
                current_shape = "circle"
            if event.key == pygame.K_e:  
                print("Switched to eraser mode")
                current_shape = "eraser"
            if event.key == pygame.K_p: 
                print("Switched color")
                palette+=1
                palette%=3 

clock.tick(FPS)  

pygame.quit()
