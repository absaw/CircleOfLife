class Test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.sum=0
    def add(self):
        self.sum=self.a+self.b
    
if __name__=="__main__":

    # t=Test(2,3)
    l=list()
    for i in range(0,10):
        l.append(Test(i,i+1))
        l[i].add()
        print(l[i].a,"+",l[i].b,"=",l[i].sum)
    # t.add()
