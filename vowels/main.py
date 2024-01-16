class Queue:
    def __init__(self):
        self.items = []
    def add(self, element):
        self.items.append(element)
    def remove(self):
        try:
            return self.items.pop(0)
        except:
            return None
