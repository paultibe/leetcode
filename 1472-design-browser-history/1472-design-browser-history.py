class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cur = 0
        self.n = 1 # actual size of valid array

    def visit(self, url: str) -> None:
        self.cur += 1
        if self.cur == len(self.history): # no invalid forward history
            self.history.append(url)
            self.n += 1
        else:
            self.history[self.cur] = url # overwrite forward history
            self.n = self.cur + 1 # adjust length

    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        return self.history[self.cur]

    def forward(self, steps: int) -> str:
        self.cur = min(self.n - 1, self.cur + steps)
        return self.history[self.cur]