class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = []
        self.limit = limit

        for item in items:
            if(not self.full()):
                self.items.append(item)


    def isEmpty(self):
        return self.items == []
        # if not self.items:
        #     return True
        # return False

    def push(self, item):
        if (not self.full()):
            self.items.insert(0, item)
        else:
            return None

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop(0)

    def peek(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)

    def full(self):
        if (len(self.items) >= self.limit):
            return True
        return False

    def search(self, target):
    
        try:
            index = self.items.index(target)
            return index
        except: 
            return -1


