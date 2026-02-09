class OrderedStream:
    def __init__(self, n: int):
        # n + 2 to handle 1-indexing and last while loop iteration
        self.stream = [None] * (n + 2)
        self.nextToReturn = 1 # 1-indexed

    def insert(self, idKey: int, value: str) -> list[str]:
        self.stream[idKey] = value
        
        results = []
        
        if idKey == self.nextToReturn:
            while self.stream[self.nextToReturn]:
                results.append(self.stream[self.nextToReturn])
                self.nextToReturn += 1
                
        return results