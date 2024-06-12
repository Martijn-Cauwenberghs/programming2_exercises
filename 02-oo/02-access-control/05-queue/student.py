class Queue:
    def __init__(self):
        self.__queue = []

    def add(self, person):
        self.__queue.append(person)

    def next(self):
        person = self.__queue[0]
        del self.__queue[0]
        return person

    def is_empty(self):
        return self.__queue == []

    