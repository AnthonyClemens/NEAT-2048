import pygame, random, sys, os

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 900
GREY = (128,128,128)

debug = True

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FONT = pygame.font.Font(pygame.font.get_default_font(),48)
pygame.display.set_caption("2048")

def find_empty_blocks(board):
    empty_blocks = []
    for y, row in enumerate(board):
        for x, block in enumerate(row):
            if block == 0:
                empty_blocks.append([x,y])
    return empty_blocks


class Block:
    # Constructor
    def __init__(self, value, x, y, w, h, color = (255,255,255)):
        self.rect = pygame.Rect(x, y, w, h)
        self.txt = FONT.render(value, True, (0,0,0))
    # Draw Method
    def Draw(self):
        coords = self.txt.get_rect()
        coords.center = self.rect.center
        SCREEN.blit(self.txt, coords)

class TwentyFortyEight:

    GAME_BOARD = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]

    GAME_SCORE = 0

    def __init__(self):
        self.board = self.GAME_BOARD
        self.score = self.GAME_SCORE
        self.gen_blocks()

    def gen_blocks(self):
        blanks = find_empty_blocks(self.board)
        ids = random.sample(range(0,len(blanks)-1),2)
        if debug:
            print("Generating blocks at:",blanks[ids[0]],blanks[ids[1]])
        for id in ids:
            if random.random() < 0.9:
                block_value = 2
            else:
                block_value = 4
            self.board[blanks[id][0]][blanks[id][1]] = block_value

    def MoveVert(self, up):
        if up:
            pass



    def move(self, direction):
        match direction:
            case 'up':
                self.MoveVert(True)
            case 'down':
                self.MoveVert(False)
            case _:
                self.MoveVert(True)

def GetColor(value):
    match value:
        case 2:
            return (238,228,218)
        case 4:
            return (237,224,200)
        case 8:
            return (242,177,121)
        case 16:
            return (245,149,99)
        case 32:
            return (246,124,95)
        case _:
            return (205,193,180)



def run():
    clock = pygame.time.Clock()

    tfes = [TwentyFortyEight()]
    scores = [0]

    for tfe in tfes:
        if debug:
            print(tfe.GAME_BOARD)

    def draw_board(id):
        for x,row in enumerate(tfes[id].GAME_BOARD):
            for y,block in enumerate(row):
                text = FONT.render(str(block),True,(0,0,0))
                rect = pygame.Rect(x*200,y*200+100,200,200)
                coords = text.get_rect()
                coords.center = rect.center
                pygame.draw.rect(SCREEN, GetColor(block), rect, 0)
                pygame.draw.rect(SCREEN, (187,173,160), rect, 8)
                SCREEN.blit(text, coords)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.fill((250,248,239))
        draw_board(scores.index(max(scores)))


        clock.tick(30)
        pygame.display.update()
run()




