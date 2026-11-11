import pygame
import networkx as nx


def Visualize(G,coloring=None):
    pygame.init()
    WIDTH, HEIGHT = 800, 600   # window size in pixels
    FPS = 60 
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)
    DARK_GRAY = (100, 100, 100)
    RED = (220, 50, 50)
    GREEN = (50, 180, 80)
    BLUE = (50, 100, 220)
    YELLOW = (240, 200, 40)
    PURPLE = (150, 80, 200)

    palette = {
        1: RED,
        2: GREEN,
        3: BLUE
    }

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Graph Visualization")

    layout_graph = nx.Graph(G)

    layout = nx.spring_layout(layout_graph, seed = 67)

    positions = {}

    for node, (x,y) in layout.items():
        screen_x = 60 + (x+1)/2 * (WIDTH - 120)
        screen_y = 60 + (y+1)/2 * (HEIGHT - 120)

        positions[node] = (round(screen_x), round(screen_y))

    clock = pygame.time.Clock()



    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)


        for u in G:
            for v in G[u]:
                if u < v:
                    pygame.draw.line(
                        screen, GRAY, positions[u], positions[v], 2
                    )

        for node in G:
            fill_color = WHITE

            if coloring is not None:
                fill_color = palette[coloring[node]]

            pygame.draw.circle(
                screen, fill_color, positions[node], 20
            )
            pygame.draw.circle(
                screen, BLACK, positions[node], 20, 2
            )

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


def Animation(G):
    coloring = {node: None for node in G}
    steps = [coloring.copy()]
    colors = [1,2,3]

    def can_color(node,c):
        for i in G[node]:
            if coloring[i] == c:
                return False
        return True

    def backtrack():
        node = None
        for i in G:
            if coloring[i] is None:
                node = i
                break

        if node is None:
            return True

        for c in colors:
            if can_color(node,c):
                coloring[node] = c
                steps.append(coloring.copy())

                if backtrack():
                    return True

                coloring[node] = None
                steps.append(coloring.copy())

        return False

    solved = backtrack()

    pygame.init()
    WIDTH, HEIGHT = 800, 600
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    GRAY = (200,200,200)
    palette = {
        None: WHITE,
        1: (220,50,50),
        2: (50,180,80),
        3: (50,100,220)
    }

    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Graph Coloring")
    clock = pygame.time.Clock()

    layout = nx.spring_layout(nx.Graph(G), seed=67)
    positions = {}

    for node, (x,y) in layout.items():
        screen_x = 60 + (x+1)/2 * (WIDTH-120)
        screen_y = 60 + (y+1)/2 * (HEIGHT-120)
        positions[node] = (round(screen_x),round(screen_y))

    step = 0
    elapsed = 0
    running = True

    while running:
        elapsed += clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not running:
            break

        if elapsed >= 500 and step < len(steps)-1:
            step += 1
            elapsed = 0

        if step == len(steps)-1:
            if solved:
                pygame.display.set_caption("3-coloring found")
            else:
                pygame.display.set_caption("No solution")

        screen.fill(WHITE)

        for u in G:
            for v in G[u]:
                if u < v:
                    pygame.draw.line(
                        screen, GRAY, positions[u], positions[v], 2
                    )

        for node in G:
            fill_color = palette[steps[step][node]]
            pygame.draw.circle(screen, fill_color, positions[node], 20)
            pygame.draw.circle(screen, BLACK, positions[node], 20, 2)

        pygame.display.flip()

    pygame.quit()
