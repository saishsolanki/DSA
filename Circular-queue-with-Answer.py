class circularQueue(object):
    ''' Simple circular queue '''

    def __init__(self,max):
        ''' Initialise the queue '''
        # Define instance variables
        self.__frontPointer = 0
        self.__rearPointer  = max-1
        self.__size = 0
        self.__max = max

        # Initialise empty queue
        self.queue = []
        for i in range(self.__max):
            self.queue.append('')

    def __str__(self): # Print magic method
        ''' Print raw queue '''
        string = '\n'
        for i in range(self.__max):
            string += '{!s:3}'.format(i) + ' : ' + str(self.queue[i]) + '\n'
        string += '\n'
        string += 'Front Pointer : ' + str(self.__frontPointer) +'\n'
        string += 'Rear Pointer  : ' + str(self.__rearPointer)  +'\n'
        string += 'Size          : ' + str(self.__size)         +'\n'
        return string

    def __isEmpty(self):
        ''' Check whether queue is empty '''
        return self.__size == 0

    def __isFull(self):
        ''' Check whether queue is full '''
        return self.__size == self.__max

    def enqueue(self,item):
        ''' Enqueue item, if space '''
        if self.__isFull():
            return False
        else:
            self.__rearPointer = (self.__rearPointer + 1) % self.__max
            self.queue[self.__rearPointer] = item
            self.__size += 1

    def dequeue(self):
        ''' Dequeue item, if one exists '''
        if self.__isEmpty():
            return False
        else:
            dequeued = self.queue[self.__frontPointer]
            self.queue[self.__frontPointer] = ''
            self.__frontPointer = (self.__frontPointer + 1) % self.__max
            self.__size -= 1
            return dequeued

    def display(self):
        ''' Display the entire queue as a string '''
        string = 'Circular Queue:\n'
        for i in range(self.__frontPointer, self.__frontPointer + self.__size):
            string += '{!s:3}'.format(i % self.__max) + ' : ' + str(self.queue[i % self.__max]) + '\n'
        print(string)
        
if __name__ == "__main__":
    max_size = 10
    cq = circularQueue(max_size)

    cq.enqueue(50)
    cq.enqueue(100)
    cq.enqueue(25)
    cq.enqueue(150)
    cq.enqueue(250)
    cq.display()

    cq.dequeue()
    cq.display()
    cq.enqueue(50)
    cq.display()
    
    cq.dequeue()
    cq.display()
    
    cq.dequeue()
    cq.display()
    
    cq.enqueue(90)
    cq.display()
    cq.enqueue(80)
    cq.display()
