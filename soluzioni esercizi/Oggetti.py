class A:
    a = 10
    b = "Ciao"
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __str__(self):
        return str(self.a) + self.b

class C:
    
    def __init__(self):
        self.v = []
        
    def __str__(self):
        s = ""
        for i in self.v:
            s += str(i)
        return s
    def append(self, a):
        self.v.append(a)

    def dell(self, id):
        for e in self.v:
            if e.a == id:
                self.v.remove(e)
                break
            
f = C()
f.append(A(10,"Ciao"))
f.append(A(20, "Mondo"))
f.dell(10)
print(f)
