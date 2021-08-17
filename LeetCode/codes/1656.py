# Author: Abshar Mohammed Aslam, github.com/abxhr

class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None]*(n+1)
        self.lId = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        if idKey > self.lId:
            return []
        else:
            ostream = []
            for i in range(self.lId, len(self.stream)):
                if self.stream[i] is None:
                    self.lId = i
                    break
                else:
                    ostream.append(self.stream[i])
            return ostream


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
