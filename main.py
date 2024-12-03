import pygame, random, sys, os, neat, visualize, time, math
from checkpoint import Checkpointer

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 900
GREY = (128,128,128)

debug = False

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FONT = pygame.font.Font(pygame.font.get_default_font(),48)
pygame.display.set_caption("2048")


class TwentyFortyEight:

    GAME_BOARD = []


    STUCK_VERT = False
    STUCK_HORI = False
    STUCK = False

    def __init__(self):
        self.GAME_BOARD = [[0 for _ in range(4)] for _ in range(4)]
        self.gen_blocks()
        self.last_score_update_time = time.time()
        self.last_score = 0
        self.GAME_SCORE = 0

    def get_board(self):
        board = []
        for y, row in enumerate(self.GAME_BOARD):
            for x, block in enumerate(row):
                board.append(self.get_block(x,y))
        return board

    def find_empty_blocks(self):
        empty_blocks = []
        for y, row in enumerate(self.GAME_BOARD):
            for x, block in enumerate(row):
                if block == 0:
                    empty_blocks.append([x,y])
        return empty_blocks

    def move_and_merge(self, arr, left_to_right):
        move_merge_arr = []
        def rem_zeros(zarr):
            zdarr = []
            for block in zarr:
                if block != 0:
                    zdarr.append(block)
            return zdarr
        move_merge_arr = rem_zeros(arr)
        if debug:
            print("0's removed:",move_merge_arr)
        if left_to_right:
            i = 0
            k = len(move_merge_arr)-1
            while i < k:
                if move_merge_arr[i] == move_merge_arr[i+1]:
                    move_merge_arr[i] *= 2
                    self.GAME_SCORE += move_merge_arr[i]
                    move_merge_arr[i+1] = 0
                    move_merge_arr = rem_zeros(move_merge_arr)
                    k = len(move_merge_arr)-1
                i+=1
            for i in range(len(arr)-len(move_merge_arr)):
                move_merge_arr.append(0)
        else:
            i = len(move_merge_arr) - 1
            while i > 0:
                if move_merge_arr[i] == move_merge_arr[i - 1] and move_merge_arr[i] != 0:
                    move_merge_arr[i] *= 2
                    self.GAME_SCORE += move_merge_arr[i]
                    move_merge_arr[i - 1] = 0
                i -= 1
            move_merge_arr = rem_zeros(move_merge_arr)
            while len(move_merge_arr) < len(arr):
                move_merge_arr.insert(0, 0)
        if debug:
            print("final merge and move:",move_merge_arr)
        return move_merge_arr

    def get_score(self):
        return self.GAME_SCORE

    def set_block(self, x, y, value):
        self.GAME_BOARD[y][x] = value

    def get_block(self, x, y):
        return self.GAME_BOARD[y][x]

    def clear_board(self):
        self.GAME_BOARD = [[0 for _ in range(4)] for _ in range(4)]
        self.STUCK_HORI = False
        self.STUCK_VERT = False
        self.STUCK = False
        self.GAME_SCORE = 0

    def gen_blocks(self):
        try:
            blanks = self.find_empty_blocks()
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

    def move_vert(self, up):
        verticals = []
        for x in range(4):
            column = []
            for y in range(4):
                column.append(self.get_block(x,y))
            verticals.append(column)
        if debug:
            print("Board seen vertically:",verticals)
        for x, column in enumerate(verticals):
            final_column = self.move_and_merge(column,up)
            if debug:
                print("Column:",final_column)
            for y,value in enumerate(final_column):
                self.set_block(x,y,value)

    def move_hori(self, left):
        horizontals = []
        for y in range(4):
            row = []
            for x in range(4):
                row.append(self.get_block(x,y))
            horizontals.append(row)
        if debug:
            print("Board seen horizontally:",horizontals)
        for y, row in enumerate(horizontals):
            final_row = self.move_and_merge(row,left)
            for x,value in enumerate(final_row):
                self.set_block(x,y,value)

    def update_time(self):
        current_time = time.time()
        if (current_time - self.last_score_update_time) > 1:
            if self.GAME_SCORE == self.last_score:
                self.STUCK = True
            self.last_score_update_time = current_time
            self.last_score = self.GAME_SCORE

    def move(self, direction):
        match direction:
            case 'up':
                self.move_vert(True)
                self.STUCK_VERT = self.gen_blocks()
            case 'down':
                self.move_vert(False)
                self.STUCK_VERT = self.gen_blocks()
            case 'left':
                self.move_hori(True)
                self.STUCK_HORI = self.gen_blocks()
            case 'right':
                self.move_hori(False)
                self.STUCK_HORI = self.gen_blocks()
            case _:
                self.move_vert(True)
        if debug:
            print("Stuck Vertically?",self.STUCK_VERT)
            print("Stuck Horizontally?",self.STUCK_HORI)

def get_color(value):
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
    scores.pop(i)


def eval_genomes(genomes, config):
    global tfes, ge, nets, scores
    clock = pygame.time.Clock()

    tfes = []
    ge = []
    nets = []
    scores = []
    max_fitness = 0

    for genome_id, genome in genomes:
        tfes.append(TwentyFortyEight())
        ge.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        scores.append(0)
        genome.fitness = 0

    def draw_stats(id):
        view = FONT.render(f'Viewing Bot id: {id}',True,(0,0,0))
        SCREEN.blit(view,(0,50))
        score = FONT.render(f'SCORE: {str(int(ge[id].fitness))}',True,(0,0,0))
        SCREEN.blit(score,(450,0))

    def draw_ai_stats():
        text = FONT.render(f'Bots Alive:{len(tfes)}',True,(0,0,0))
        text_2 = FONT.render(f'Generation:{p.generation+1}', True, (0, 0, 0))
        SCREEN.blit(text,(450,50))
        SCREEN.blit(text_2,(0,0))

    def draw_board(id):
        for y,column in enumerate(tfes[id].GAME_BOARD):
            for x,block in enumerate(column):
                text = FONT.render(str(block),True,(0,0,0))
                rect = pygame.Rect(x*200,y*200+100,200,200)
                coords = text.get_rect()
                coords.center = rect.center
                pygame.draw.rect(SCREEN, get_color(block), rect, 0)
                pygame.draw.rect(SCREEN, (187,173,160), rect, 8)
                SCREEN.blit(text, coords)

    run = True
    while run:
        best_score = 0
        best_player = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if len(tfes) == 0:
            print("Max fitness this generation was:",int(max_fitness))
            break

        for i, tfe in enumerate(tfes):
            if tfe.STUCK:
                ge[i].fitness += max(tfe.get_board()) + (sum(tfe.get_board()) / len(tfe.get_board()))
                if ge[i].fitness > max_fitness:
                    max_fitness = ge[i].fitness
                remove(i)

        for i, tfe in enumerate(tfes):
            sqrt_board = []
            for value in tfe.get_board():
                sqrt_board.append(math.sqrt(value))
            output = nets[i].activate(sqrt_board)
            if output[0] > 0.5:
                tfe.move("up")
            if output[1] > 0.5:
                tfe.move("down")
            if output[2] > 0.5:
                tfe.move("left")
            if output[3] > 0.5:
                tfe.move("right")

            if tfe.get_score() > best_score:
                best_score = tfe.get_score()
                best_player = i

            if tfe.get_score() > scores[i]:
                ge[i].fitness += (tfe.get_score()-scores[i])*.4

            if len(tfe.find_empty_blocks()) < 4:
                ge[i].fitness -= 2
            else:
                ge[i].fitness += 3

            if debug:
                print(f'Bot {i}\'s fitness {ge[i].fitness}')
            tfe.update_time()
            scores[i] = tfe.get_score()

        SCREEN.fill((250,248,239))

        if len(tfes)>0:
            draw_board(best_player)
            draw_stats(best_player)
            draw_ai_stats()
        clock.tick(120)
        pygame.display.update()

def run(config_file, checkpoint):
    global p
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)
    p = neat.Population(config)
    checkpointer = Checkpointer()
    if checkpoint > -1:
        p = checkpointer.restore_checkpoint("neat-checkpoint-"+str(checkpoint), update_config=config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(checkpointer)
    winner = p.run(eval_genomes, 20000)

    print('\nBest genome:\n{!s}'.format(winner))
    node_names = {-1: '[0,0]', -2: '[1,0]', -3: '[2,0]', -4: '[3,0]', -5: '[0,1]', -6: '[2,1]', -7: '[1,2]', -8: '[1,3]', -9: '[2,0]', -10: '[2,1]', -11: '[2,2]', -12: '[2,3]', -13: '[3,0]', -14: '[3,1]', -15: '[3,2]', -16: '[3,3]', 0: 'up', 1: 'down', 2: 'left', 3: 'right'}
    visualize.draw_net(config, winner, True, node_names=node_names)
    visualize.plot_stats(stats, ylog=False, view=True)
    visualize.plot_species(stats, view=True)


if __name__ == "__main__":
    max_gen = -1
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    for file in os.listdir(local_dir):
        if file.startswith("neat-checkpoint-"):
            if int(file.removeprefix("neat-checkpoint-")) > max_gen:
                max_gen = int(file.removeprefix("neat-checkpoint-"))
    run(config_path, max_gen)




