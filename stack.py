
class Stack:

    def __init__(self,Capacity=1):
        self.top = -1
        self.Capacity = Capacity
        self.A = [None]*Capacity

    def push(self, data):
        if self.Capacity == self.top+1:
            print('Stack overflow')
            return 
        self.top += 1 
        self.A[self.top] = data

    def pop(self):
        if self.top == -1:
            print("Stack underflow")
            return 
        temp = self.A[self.top]
        self.top -= 1
        return temp
    
    def peek(self):
        if self.top == -1:
            print("Stack Overflow")
            return 
        return self.A[self.top]
    
    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.Capacity == self.top + 1


# class Stack:

#     def __init__(self, Capacity=1):
#         self.top = -1
#         self.Capacity = Capacity
#         self.A = [None] * Capacity

#     def push(self, data):
#         if self.Capacity == self.top + 1:
#             return 'Stack overflow'
#         self.top += 1
#         self.A[self.top] = data

#     def pop(self):
#         if self.top < 0:
#             return 'Stack underflow'
#         temp = self.A[self.top]
#         self.top -= 1
#         return temp

#     def peek(self):
#         if self.top < 0:
#             return 'Stack Underflow'
#         return self.A[self.top]

#     def isEmpty(self):
#         return self.top == -1

#     def isFull(self):
#         return self.Capacity == self.top + 1


# def p():
#     s = Stack(30)

#     s.push(5) 
#     s.push(3)
#     print(s.pop()) 
#     print(s.pop()) 
#     print(s.isEmpty())

# p()