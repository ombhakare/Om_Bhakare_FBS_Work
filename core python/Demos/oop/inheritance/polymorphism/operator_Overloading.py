class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def __add__(self, other):
        print("this is add function.")

t1 = Time(35, 43, 29)
t2 = Time(20, 34, 55)

print(t1 + t2)