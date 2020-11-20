import pygame
from time import sleep

pygame.init()
WHITE = (255, 255, 255)
BLUE = (0, 0, 128)
LIGHT_BLUE = (0,102,255)
GREY = (224,224,224)

class TicTacToe:
    def __init__(self):
        self.width=192
        self.height=192
        self.textures={
            'x': pygame.image.load("x.png"),
            'o': pygame.image.load("o.png"),
        }
        pygame.display.set_caption("tic-tac-toe")
        self.turn = 'x'
        self.board = [['-','-','-'],
                      ['-','-','-'],
                      ['-','-','-']]
        self.clock = pygame.time.Clock()


    def draw_board(self):
        self.screen.fill(WHITE)
        #drawing vertical lines
        pygame.draw.line(self.screen, BLUE, (0, int(self.height*1/3)), (int(self.width), int(self.height*1/3)))
        pygame.draw.line(self.screen, BLUE, (0, int(self.height*2/3)), (int(self.width), int(self.height*2/3)))
        # drawing horizontal lines
        pygame.draw.line(self.screen, BLUE, (int(self.width*1/3), 0), (int(self.width*1/3), int(self.height)))
        pygame.draw.line(self.screen, BLUE, (int(self.width*2/3), 0), (int(self.width*2/3), int(self.height)))
        
        pygame.display.update()


    def draw_win_line_horizontal(self, y):
        newX, newY = self.convert_coord(0, y)
        width = self.width+2
        height = int(self.height/3-1)
        pygame.draw.rect(self.screen, GREY, (newX, newY, width, height))
        pygame.display.update()


    def draw_win_line_vertical(self, x):
        newX, newY = self.convert_coord(x, 0)
        width = int(self.width/3-1)
        height = self.height+2
        pygame.draw.rect(self.screen, GREY, (newX, newY, width, height))
        pygame.display.update()


    def draw_win_line_ldiagonal(self):
        width = int(self.width/3-1)
        height = int(self.height/3-1)
        for i in range(3):
            newX, newY = self.convert_coord(i, i)
            pygame.draw.rect(self.screen, GREY, (newX, newY, width, height))
        pygame.display.update()


    def draw_win_line_rdiagonal(self):
        width = int(self.width/3-1)
        height = int(self.height/3-1)
        for i in range(3):
            newX, newY = self.convert_coord(i, 2-i)
            pygame.draw.rect(self.screen, GREY, (newX, newY, width, height))
        pygame.display.update()


    def display_winner_message(self):
        font = pygame.font.Font('freesansbold.ttf', 60)
        text = font.render(f'{self.turn} wins', True, LIGHT_BLUE, WHITE) 
        textRect = text.get_rect() 
        textRect.center = (self.width//2, self.height//2)
        self.screen.blit(text, textRect)
        pygame.display.update()


    def start_new_game(self):
        self.draw_board()
        self.turn = 'x'
        self.board = [['-','-','-'],
                      ['-','-','-'],
                      ['-','-','-']]


    def horizontal_win(self):
        for y in range(3):
            for x in range(3):
                if self.board[y][x]!=self.turn:
                    break
                elif x==2:
                    self.draw_win_line_horizontal(y)
                    sleep(1)
                    self.display_winner_message()
                    sleep(1)
                    return True
        return False


    def vertical_win(self):
        for x in range(3):
            for y in range(3):
                if self.board[y][x]!=self.turn:
                    break
                elif y==2:
                    self.draw_win_line_vertical(x)
                    sleep(1)
                    self.display_winner_message()
                    sleep(1)
                    return True
        return False
    

    def ldiagonal_win(self):
        for i in range(3):
            if self.board[i][i]!=self.turn:
                break
            elif i==2:
                self.draw_win_line_ldiagonal()
                sleep(1)
                self.display_winner_message()
                sleep(1)
                return True
        return False
    

    def rdiagonal_win(self):
        for i in range(3):
            if self.board[i][2-i]!=self.turn:
                break
            elif i==2:
                self.draw_win_line_rdiagonal()
                sleep(1)
                self.display_winner_message()
                sleep(1)
                return True
        return False


    def all_spaces_occupied(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j]=='-':
                    return False
        return True


    def game_ended(self):
        if self.horizontal_win() or self.vertical_win() or self.rdiagonal_win() or self.ldiagonal_win():
            return True
        return self.all_spaces_occupied()
       
    
    def convert_coord(self, x, y):
        return (int(x*(self.width/3+1)), int(y*(self.height/3+1)))


    def drawXO(self, x, y):
        pos = self.convert_coord(x, y)
        self.screen.blit(self.textures[self.turn], pos)
        pygame.display.update()


    def swap_turn(self):
        if self.turn=='x':
            self.turn = 'o'
        else:
            self.turn = 'x'   


    def get_mouse_on_board_coords(self):
        pos = pygame.mouse.get_pos()
        x=int(pos[0]//((self.width+2)/3))
        y=int(pos[1]//((self.height+2)/3))
        return (x, y)


    def run(self):
        self.screen = pygame.display.set_mode((self.width+2, self.height+2))
        self.draw_board()
        
        runing = True
        while runing:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = self.get_mouse_on_board_coords()

                    if self.board[y][x]=='-':
                        self.board[y][x]=self.turn
                        self.drawXO(x, y)
                        if not self.game_ended(): 
                            self.swap_turn()     
                        else:
                            self.start_new_game()

                if event.type == pygame.QUIT:
                    runing = False
                self.clock.tick(50)


def main():
    gameInstance = TicTacToe()
    gameInstance.run()


if __name__=='__main__':
    main()
