def step(self, action):
    # Actions: 0=up, 1=right, 2=down, 3=left
    r, c = self.state
    if action == 0:   # up
        #Fill in the blank: 1
        r = max(r - 1, 0)
    # (Other actions omitted for brevity)
    self.state = (r, c)
    # Terminal state check
    if self.state in self.terminal:
        return self.state, 1, True
    else:
        return self.state, 0, False
