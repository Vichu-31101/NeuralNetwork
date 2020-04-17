import random


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = []
        self.Randomize()

    def Randomize(self):
        for i in range(self.rows):
            r = []
            for j in range(self.cols):
                r.append(random.random() * random.choice([-1, 1]))
            self.data.append(r)

    @staticmethod
    def Multiply(a, b):
        nm = Matrix(a.rows, b.cols)
        if a.cols != b.rows:
            print("Invalid matrices")
        else:
            c = a.cols
            for i in range(a.rows):
                for j in range(b.cols):
                    nm.data[i][j] = 0
                    for k in range(c):
                        nm.data[i][j] += a.data[i][k] * b.data[k][j]
        return nm

    def ElementMultiply(self, m):
        if isinstance(m, Matrix):
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] *= m.data[i][j]
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] *= m

    def Add(self, nm):
        if self.rows != nm.rows:
            print("Invalid matrices")
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] += nm.data[i][j]

    @staticmethod
    def Subtract(n, m):
        nm = Matrix(n.rows, n.cols)
        for i in range(nm.rows):
            for j in range(nm.cols):
                nm.data[i][j] = n.data[i][j] - m.data[i][j]
        return nm

    @staticmethod
    def Transpose(m):
        nm = Matrix(m.cols, m.rows)
        for i in range(m.rows):
            for j in range(m.cols):
                nm.data[j][i] = m.data[i][j]
        return nm

    def Map(self, func):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = func(self.data[i][j])

    @staticmethod
    def StaticMap(m, func):
        nm = Matrix(m.rows, m.cols)
        for i in range(m.rows):
            for j in range(m.cols):
                nm.data[i][j] = func(m.data[i][j])
        return nm

    @staticmethod
    def FromArray(arr):
        nm = Matrix(len(arr), 1)
        for i in range(len(arr)):
            nm.data[i][0] = arr[i]
        return nm

    def Display(self):
        print(self.data)
