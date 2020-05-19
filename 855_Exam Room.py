class ExamRoom(object):

    def __init__(self, N):
        self.students = []
        self.capacity = N
        
    def seat(self):
        if not self.students:
            self.students.append(0)
            return 0
        else:
            mx = float('-inf')
            idx = 0
            for i in range(len(self.students) - 1):
                d = self.students[i + 1] - self.students[i]
                if d > mx + 1:
                    mx = d
                    idx = i
            
            d = self.capacity - 1 - self.students[-1]
            if d > mx + 1:
                mx = d
                idx = self.students[-1] 
            m = (self.students[idx] + self.students[idx + 1]) / 2
            self.students.insert(index + 1, m)
            return m

    def leave(self, p):
        self.students.remove(p)


s = ExamRoom(10)
print(s.seat())
print(s.seat())
print(s.seat())
print(s.seat())
print(s.leave(4))
print(s.seat())
