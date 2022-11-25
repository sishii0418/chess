from typing import List, Optional
import sys

piece = Optional[str]

class GameState:
    def __init__(self) -> None:
        self.board: List[List[piece]] = [["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
                                         ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
                                         [None, None, None, None, None, None, None, None],
                                         [None, None, None, None, None, None, None, None],
                                         [None, None, None, None, None, None, None, None],
                                         [None, None, None, None, None, None, None, None],
                                         ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
                                         ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
    def coor(self, piece_loc) -> piece:
        x, y = piece_loc
        return self.board[x][y]

    # Check if the specified two pieces are of the same player's
    # Return False for a location for None
    def isMyPiece(self, piece_loc: tuple[int, int], piece_loc2: tuple[int, int]) -> bool:
        if self.coor(piece_loc) == None or self.coor(piece_loc2) == None:
            return False
        elif self.coor(piece_loc)[0] == self.coor(piece_loc2)[0]:
            return True
        else:
            return False

    # Returns possible location for a specified piece to move
    def move(self, piece_loc: tuple[int, int]) -> Optional[set[tuple[int, int]]]:
        x, y = piece_loc
        def zero2seven(xy: tuple[int, int]) -> bool:
            return 0 <= xy[0] and xy[0] <= 7 and 0 <= xy[1] and xy[1] <= 7
        if self.board[x][y] in ["bK", "wK"]:
            # FIXME: 移動先でチェックメイトされるようなマスには移動できない
            rt = set(filter(zero2seven, [(x+1, y+1), (x+1, y), (x+1, y-1), (x, y+1), (x, y), (x, y-1),(x-1, y+1), (x-1, y), (x-1, y-1),]))
            return set(filter(lambda x: not self.isMyPiece(piece_loc, x), rt))
        elif self.board[x][y] in ["bQ", "wQ"]:
            rt = set([])
            # 左
            while 0 < x:
                if self.board[x-1][y] != None:
                    if self.isMyPiece(piece_loc, (x-1, y)):
                        break
                    else:
                        rt.add((x-1, y))
                        break
                rt.add((x-1, y))
                x -= 1
            # 右
            x, y = piece_loc
            while x < 7:
                if self.board[x+1][y] != None:
                    if self.isMyPiece(piece_loc, (x+1, y)):
                        break
                    else:
                        rt.add((x+1, y))
                        break
                rt.add((x+1, y))
                x += 1
            # 下
            x, y = piece_loc
            while y < 7:
                if self.board[x][y+1] != None:
                    if self.isMyPiece(piece_loc, (x, y+1)):
                        break
                    else:
                        rt.add((x, y+1))
                        break
                rt.add((x, y+1))
                y += 1
            # 上
            x, y = piece_loc
            while 0 < y:
                if self.board[x][y-1] != None:
                    if self.isMyPiece(piece_loc, (x, y-1)):
                        break
                    else:
                        rt.add((x, y-1))
                        break
                rt.add((x, y-1))
                y -= 1
            # 斜め
            # 左上
            while 0 < x and 0 < y:
                if self.board[x-1][y-1] != None:
                    if self.isMyPiece(piece_loc, (x-1, y-1)):
                        break
                    else:
                        rt.add((x-1, y-1))
                        break
                rt.add((x-1, y-1))
                x -= 1
                y -= 1
            # 右下
            x, y = piece_loc
            while x < 7 and y < 7:
                if self.board[x+1][y+1] != None:
                    if self.isMyPiece(piece_loc, (x+1, y+1)):
                        break
                    else:
                        rt.add((x+1, y+1))
                        break
                rt.add((x+1, y+1))
                x += 1
                y += 1
            # 右上
            x, y = piece_loc
            while 0 < x and y < 7:
                if self.board[x-1][y+1] != None:
                    if self.isMyPiece(piece_loc, (x-1, y+1)):
                        break
                    else:
                        rt.add((x-1, y+1))
                        break
                rt.add((x-1, y+1))
                x -= 1
                y += 1
            # 左下
            x, y = piece_loc
            while x < 7 and 0 < y:
                if self.board[x+1][y-1] != None:
                    if self.isMyPiece(piece_loc, (x+1, y-1)):
                        break
                    else:
                        rt.add((x+1, y-1))
                        break
                rt.add((x+1, y-1))
                x += 1
                y -= 1
            return rt
        elif self.board[x][y] in ["bR", "wR"]:
            rt = set([])
            # 左
            while 0 < x:
                if self.board[x-1][y] != None:
                    if self.isMyPiece(piece_loc, (x-1, y)):
                        break
                    else:
                        rt.add((x-1, y))
                        break
                rt.add((x-1, y))
                x -= 1
            # 右
            x, y = piece_loc
            while x < 7:
                if self.board[x+1][y] != None:
                    if self.isMyPiece(piece_loc, (x+1, y)):
                        break
                    else:
                        rt.add((x+1, y))
                        break
                rt.add((x+1, y))
                x += 1
            # 下
            x, y = piece_loc
            while y < 7:
                if self.board[x][y+1] != None:
                    if self.isMyPiece(piece_loc, (x, y+1)):
                        break
                    else:
                        rt.add((x, y+1))
                        break
                rt.add((x, y+1))
                y += 1
            # 上
            x, y = piece_loc
            while 0 < y:
                if self.board[x][y-1] != None:
                    if self.isMyPiece(piece_loc, (x, y-1)):
                        break
                    else:
                        rt.add((x, y-1))
                        break
                rt.add((x, y-1))
                y -= 1
            return rt
        elif self.board[x][y] in ["bB", "wB"]:
            rt = set([])
            # 斜め
            # 左上
            while 0 < x and 0 < y:
                if self.board[x-1][y-1] != None:
                    if self.isMyPiece(piece_loc, (x-1, y-1)):
                        break
                    else:
                        rt.add((x-1, y-1))
                        break
                rt.add((x-1, y-1))
                x -= 1
                y -= 1
            # 右下
            x, y = piece_loc
            while x < 7 and y < 7:
                if self.board[x+1][y+1] != None:
                    if self.isMyPiece(piece_loc, (x+1, y+1)):
                        break
                    else:
                        rt.add((x+1, y+1))
                        break
                rt.add((x+1, y+1))
                x += 1
                y += 1
            # 右上
            x, y = piece_loc
            while 0 < x and y < 7:
                if self.board[x-1][y+1] != None:
                    if self.isMyPiece(piece_loc, (x-1, y+1)):
                        break
                    else:
                        rt.add((x-1, y+1))
                        break
                rt.add((x-1, y+1))
                x -= 1
                y += 1
            # 左下
            x, y = piece_loc
            while x < 7 and 0 < y:
                if self.board[x+1][y-1] != None:
                    if self.isMyPiece(piece_loc, (x+1, y-1)):
                        break
                    else:
                        rt.add((x+1, y-1))
                        break
                rt.add((x+1, y-1))
                x += 1
                y -= 1
            return rt
        elif self.board[x][y] in ["bN", "wN"]:
            rt = set(filter(zero2seven, {(x+2, y+1), (x+2, y-1), (x+1, y+2), (x+1, y-2), (x-1, y+2), (x-1, y-2), (x-2, y+1), (x-2, y-1)}))
            return set(filter(lambda x: not self.isMyPiece(piece_loc, x), rt))
        elif self.board[x][y] in ["bP", "wP"]:
            rt = set([])
            if self.board[x][y] == "bP":
                if x == 1:
                    rt = set(filter(lambda x: self.coor(x) is None, {(x+1, y), (x+2, y)}))
                else:
                    if x+1 <= 7:
                        rt = set(filter(lambda x: self.coor(x) is None, {(x+1, y)}))
                if zero2seven((x+1, y+1)) and self.coor((x+1, y+1)) != None:
                    if not self.isMyPiece(piece_loc, (x+1, y+1)):
                        rt.add((x+1, y+1))
                if zero2seven((x+1, y-1)) and self.coor((x+1, y-1)) != None:
                    if not self.isMyPiece(piece_loc, (x+1, y-1)):
                        rt.add((x+1, y-1))
            else: # self.board[x][y] == "wP"
                if x == 6:
                    rt = set(filter(lambda x: self.coor(x) is None, {(x-1, y), (x-2, y)}))
                else:
                    if 0 <= x-1:
                        rt = set(filter(lambda x: self.coor(x) is None, {(x-1, y)}))
                if zero2seven((x-1, y+1)) and self.coor((x-1, y+1)) != None:
                    if not self.isMyPiece(piece_loc, (x-1, y+1)):
                        rt.add((x-1, y+1))
                if zero2seven((x-1, y-1)) and self.coor((x-1, y-1)) != None:
                    if not self.isMyPiece(piece_loc, (x-1, y-1)):
                        rt.add((x-1, y-1))
            return rt