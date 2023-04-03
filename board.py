import random
import numpy as np
import os
import time
import curses


class Board:
    def __init__(self, height=10, width=10, file_name=None):
        self.file_name = file_name
        if file_name is None:
            self.height = height
            self.width = width
            self.board = np.zeros((height, width))
            self.soup()
        else:
            self.board = self.load_board_state(file_name)
            (self.height, self.width) = np.shape(self.board)

    def soup(self):
        for i in range(self.height):
            for j in range(self.width):
                self.board[i][j] = random.randint(0, 1)

    def get_board(self):
        return self.board

    def render(self, stdscr):
        stdscr.clear()
        stdscr.addstr("-" * (self.width + 2) + "\n")
        for i in range(self.height):
            print("|")
            for j in range(self.width):
                if self.board[i][j] == 1:
                    stdscr.addstr("\u2588")
                else:
                    stdscr.addstr(" ")
            stdscr.addstr("|\n")
        stdscr.addstr("-" * (self.width + 2))
        stdscr.refresh()


    def check_pos(self, y, x):
        if 0 <= x < self.width and 0 <= y < self.height:
            if self.board[y][x] == 1:
                return 1
            return 0
        return 0

    def check_all_neighbors(self, y, x):
        num_of_neighbors = 0
        for j in range(-1, 2):
            for i in range(-1, 2):
                if i != 0 or j != 0:
                    num_of_neighbors += self.check_pos(y + i, x + j)
        return num_of_neighbors

    def next_value(self, y, x):
        neighbors = self.check_all_neighbors(y, x)
        if neighbors <= 1 and self.board[y][x] == 1:
            return 0
        elif neighbors > 3 and self.board[y][x] == 1:
            return 0
        elif neighbors == 3 and self.board[y][x] == 0:
            return 1
        return self.board[y][x]

    def next_step(self):
        temp_board = np.zeros((self.height, self.width))
        for i in range(self.height):
            for j in range(self.width):
                temp_board[i][j] = self.next_value(i, j)
        self.board = temp_board

    def load_board_state(self, file_name):
        with open(file_name, 'r') as file:
            lines = [list(map(int, line.strip())) for line in file]
        return np.array(lines)

    def run(self, stdscr):
        stdscr.timeout(100)
        while True:
            self.render(stdscr)
            self.next_step()

            key = stdscr.getch()
            if key == ord('q'):
                break

