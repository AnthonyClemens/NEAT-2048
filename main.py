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
                empty_blocks.append([y,x])
    return empty_blocks

def MoveMerge(arr, left_to_right):
    def merge_elements(elements):
        merged = []
        i = 0
        while i < len(elements):
            if i < len(elements) - 1 and elements[i] == elements[i + 1]:
                merged.append(elements[i] * 2)
                i += 2
            else:
                merged.append(elements[i])
                i += 1
        return merged
    final_arr = arr
    #TODO make code to sort arrays and merge based on direction
    
    return final_arr


class TwentyFortyEight:

    GAME_BOARD = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]

    STUCK_VERT = False
    STUCK_HORI = False
    GAME_SCORE = 0

    def __init__(self):
        self.gen_blocks()

    def gen_blocks(self):
        try:
            blanks = find_empty_blocks(self.GAME_BOARD)
            if debug:
                    print("Blanks:",blanks)
            if len(blanks) > 2:
                ids = random.sample(range(0,len(blanks)-1),2)
                if debug:
                    print("Generating blocks at:",blanks[ids[1]],blanks[ids[0]])
            else:
                ids = [0]
            for id in ids:
                if random.random() < 0.9:
                    block_value = 2
                else:
                    block_value = 4
                self.GAME_BOARD[blanks[id][0]][blanks[id][1]] = block_value
                return False
        except:
            return True

    def MoveVert(self, up):
        verticals = []
        for x in range(4):
            column = []
            for y in range(4):
                column.append(self.GAME_BOARD[x][y])
            verticals.append(column)
        if debug:
            print("Board seen vertically:",verticals)
        for x, column in enumerate(verticals):
            final_column = MoveMerge(column,up)
            if debug:
                print("Column:",final_column)
            for y,value in enumerate(final_column):
                self.GAME_BOARD[x][y] = value
                    
    def MoveHori(self, left):
        horizontals = []
        for y in range(4):
            row = []
            for x in range(4):
                row.append(self.GAME_BOARD[x][y])
            horizontals.append(row)
        if debug:
            print("Board seen horizontally:",horizontals)
        for x, row in enumerate(horizontals):
            final_row = MoveMerge(row,left)
            print("Row",final_row)
            for y,value in enumerate(row):
                self.GAME_BOARD[y][x] = value



    def move(self, direction):
        match direction:
            case 'up':
                self.MoveVert(True)
                self.STUCK_VERT = self.gen_blocks()
            case 'down':
                self.MoveVert(False)
                self.STUCK_VERT = self.gen_blocks()
            case 'left':
                self.MoveHori(True)
                self.STUCK_HORI = self.gen_blocks()
            case 'right':
                self.MoveHori(False)
                self.STUCK_HORI = self.gen_blocks()
            case _:
                self.MoveVert(True)
        print("Stuck Vertically?",self.STUCK_VERT)
        print("Stuck Horizontally?",self.STUCK_HORI)

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
            print("Current game board:",tfe.GAME_BOARD)

    def draw_stats(id):
        text = FONT.render("Game Over!",True,(0,0,0))
        if tfes[id].STUCK_HORI and tfes[id].STUCK_VERT:
            SCREEN.blit(text,(0,0))

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    tfes[0].move("up")
                if event.key == pygame.K_s:
                    tfes[0].move("down")
                if event.key == pygame.K_a:
                    tfes[0].move("left")
                if event.key == pygame.K_d:
                    tfes[0].move("right")
                if event.key == pygame.K_g:
                    tfes[0].gen_blocks()
        SCREEN.fill((250,248,239))
        draw_board(scores.index(max(scores)))

        draw_stats(scores.index(max(scores)))
        clock.tick(30)
        pygame.display.update()
run()




