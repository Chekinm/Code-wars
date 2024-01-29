class Queen:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def kill(self, other):
        if (self.x == other.x or
                self.y == other.y or
                abs(self.x - other.x) == abs(self.y - other.y)):
            return True
        return False

    def __str__(self):
        return f'Q x={self.x}, y={self.y}'


class Field:

    def __init__(self, f=None):
        if f is None:
            self.f = []

    def add_queen(self, new_queen):
        for q in self.f:
            if q.kill(new_queen):
                return False
        self.f.append(new_queen)
        return True

    def pop_queen(self):
        self.f.pop()

    def __str__(self):
        return ''.join([str(q) for q in self.f])


class Solution:
    def totalNQueens(self, n: int) -> int:

        def try_row(y):
            for x in range(n):
                if field.add_queen(Queen(x, y)):
                    if y < n - 1:
                        try_row(y + 1)
                    elif y == n - 1:
                        sol = field.f.copy()
                        ans.append(sol)
                        field.pop_queen()
                        # print('valid', field)
            if y > 0:
                # print('invalid', field)
                field.pop_queen()

            return

        field = Field()
        ans = []
        try_row(0)

        return len(ans)
