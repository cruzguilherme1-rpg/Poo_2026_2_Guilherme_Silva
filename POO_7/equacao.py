class equacao:
    def init(self, a, b, c):
        self.set_a(a)
        self.set_b(b)
        self.set_c(c)

    def set_a(self, a): self.__a = a
    def set_b(self, b): self.__b = b
    def set_c(self, c): self.__c = c

    def get_a(self): return self.__a
    def get_b(self): return self.__b
    def get_c(self): return self.__c

    def delta(self): return -self.__b *4*self.__a*self.__c
    def x1(self): return self 