class GridWorld:
    def __init__(self, size=4):
        self.size = size
        self.n_states = size * size
        self.n_actions = 4
        self.reset()

        def reset(self):
            self.s = 0
            return self.s

    def step(self, a):
        row, col = divmod(self.s, self.size)
        
        if a == 0: row = max(row - 1, 0)
        if a == 1: row = min(row + 1, self.size - 1)
        if a == 2: col = max(col - 1, 0)
        if a == 3: col = min(col + 1, self.size - 1)
        
        self.s = row * self.size + col
        reward = -1
        
        done = self.s == self.n_states - 1
        return self.s, reward, done
