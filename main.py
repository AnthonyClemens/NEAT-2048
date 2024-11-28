import pygame, random, sys, os, neat, visualize

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 900
GREY = (128,128,128)

debug = False

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FONT = pygame.font.Font(pygame.font.get_default_font(),48)
pygame.display.set_caption("2048")


class TwentyFortyEight:

    GAME_BOARD = [[0 for x in range(4)] for y in range(4)]


    STUCK_VERT = False
    STUCK_HORI = False
    GAME_SCORE = 0

    def __init__(self):
        self.gen_blocks()

    def find_empty_blocks(self):
        empty_blocks = []
        for y, row in enumerate(self.GAME_BOARD):
            for x, block in enumerate(row):
                if block == 0:
                    empty_blocks.append([x,y])
        return empty_blocks

    def MoveMerge(self, arr, left_to_right):
        newArr = []
        def RemoveZeros(zarr):
            zdarr = []
            for block in zarr:
                if block != 0:
                    zdarr.append(block)
            return zdarr
        newArr = RemoveZeros(arr)
        if debug:
            print("0's removed:",newArr)
        if left_to_right:
            i = 0
            k = len(newArr)-1
            while i < k:
                if newArr[i] == newArr[i+1]:
                    newArr[i] *= 2
                    self.GAME_SCORE += newArr[i]
                    newArr[i+1] = 0
                    newArr = RemoveZeros(newArr)
                    k = len(newArr)-1
                i+=1
            for i in range(len(arr)-len(newArr)):
                newArr.append(0)
        else:
            i = len(newArr) - 1
            while i > 0:
                if newArr[i] == newArr[i - 1] and newArr[i] != 0:
                    newArr[i] *= 2
                    self.GAME_SCORE += newArr[i]
                    newArr[i - 1] = 0
                i -= 1
            newArr = RemoveZeros(newArr)
            while len(newArr) < len(arr):
                newArr.insert(0, 0)
        if debug:
            print("final merge and move:",newArr)
    
        return newArr


    def set_block(self, x, y, value):
        self.GAME_BOARD[y][x] = value

    def get_block(self, x, y):
        return self.GAME_BOARD[y][x]

    def clear_board(self):
        self.GAME_BOARD = [[0 for x in range(4)] for y in range(4)]
        self.STUCK_HORI = False
        self.STUCK_VERT = False
        self.GAME_SCORE = 0

    def gen_blocks(self):
        try:
            blanks = find_empty_blocks(self.GAME_BOARD)
            if debug:
                    print("Blanks:",blanks)
            if len(blanks) > 2:
                ids = random.sample(range(0,len(blanks)-1),2)
                if debug:
                    print("Generating blocks at:",blanks[ids[0]],blanks[ids[1]])
            else:
                ids = [0]
            for id in ids:
                if random.random() < 0.9:
                    block_value = 2
                else:
                    block_value = 4
                self.set_block(blanks[id][0],blanks[id][1], block_value)
                return False
        except:
            return True

    def MoveVert(self, up):
        verticals = []
        for x in range(4):
            column = []
            for y in range(4):
                column.append(self.get_block(x,y))
            verticals.append(column)
        if debug:
            print("Board seen vertically:",verticals)
        for x, column in enumerate(verticals):
            final_column = self.MoveMerge(column,up)
            if debug:
                print("Column:",final_column)
            for y,value in enumerate(final_column):
                self.set_block(x,y,value)
                    
    def MoveHori(self, left):
        horizontals = []
        for y in range(4):
            row = []
            for x in range(4):
                row.append(self.get_block(x,y))
            horizontals.append(row)
        if debug:
            print("Board seen horizontally:",horizontals)
        for y, row in enumerate(horizontals):
            final_row = self.MoveMerge(row,left)
            for x,value in enumerate(final_row):
                self.set_block(x,y,value)



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
        if debug:
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
        case 64:
            return (246,94,59)
        case 128:
            return (237,207,114)
        case 256:
            return (237,204,97)
        case 512:
            return (237,200,80)
        case 1024:
            return (237,197,63)
        case 2048:
            return (237,194,46)
        case 0:
            return (205,193,180)
        case _:
            return (0,255,0)

def remove(i):
    tfes.pop(i)
    ge.pop(i)
    nets.pop(i)


def eval_genomes(genomes, config):
    global tfes, ge, nets
    clock = pygame.time.Clock()

    tfes = []
    ge = []
    nets = []

    for genome_id, genome in genomes:
        tfes.append(TwentyFortyEight())
        ge.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0

    def draw_stats(id):
        text = FONT.render("Game Over!",True,(0,0,0))
        restart = FONT.render("Press \'r\' to restart",True,(0,0,0))
        if tfes[id].STUCK_HORI and tfes[id].STUCK_VERT:
            SCREEN.blit(text,(0,0))
            SCREEN.blit(restart,(0,50))
        score = FONT.render(f'SCORE: {str(tfes[0].GAME_SCORE)}',True,(0,0,0))
        SCREEN.blit(score,(400,0))

    def draw_board(id):
        for y,column in enumerate(tfes[id].GAME_BOARD):
            for x,block in enumerate(column):
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
                if event.key == pygame.K_r:
                    tfes[0].clear_board()
                
        SCREEN.fill((250,248,239))
        if len(tfes) == 0:
            break

        for i, dinosaur in enumerate(tfes):
            output = nets[i].activate()

        draw_board(0)
        draw_stats(0)
        clock.tick(30)
        pygame.display.update()

def run(config_file):
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(5))

    winner = p.run(eval_genomes, 300)

    print('\nBest genome:\n{!s}'.format(winner))
    node_names = {-1: 'Game board', -2: 'Empty slots', 0: 'up', 1: 'down', 2: 'left', 3: 'right'}
    visualize.draw_net(config, winner, True, node_names=node_names)
    visualize.draw_net(config, winner, True, node_names=node_names, prune_unused=True)
    visualize.plot_stats(stats, ylog=False, view=True)
    visualize.plot_species(stats, view=True)
    p.run(eval_genomes, 10)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    run(config_path)




