class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit


    def isEmpty(self):
        if not self.items:
            return True
        return False

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        self.items.pop(0)
        pass

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        if (len(self.items) >= self.limit):
            return True
        return False
        # if (len(self.items) >= self.limit):
        #     return True
        # return False

    def search(self, target):
        print(f'this is the list: {self.items} and this is the target: {target}')
        try:
            index = self.items.index(target)
            return index
        except: 
            return -1


