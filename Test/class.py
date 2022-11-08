import copy
class Test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.sum=0
    def add(self):
        self.sum=self.a+self.b

class Test2:
    def __init__(self,T:Test):
        self.T=T
    def change(self):
        self.T.a=500
        self.T.b=300
    

if __name__=="__main__":

    t=Test(2,3)
    t.add()

    # l=list()
    # for i in range(0,10):
    #     l.append(Test(i,i+1))
    #     l[i].add()
    #     print(l[i].a,"+",l[i].b,"=",l[i].sum)
    # t.add()
    t2=Test2(t)
    t2.change()
    t3=copy.copy(t)
    t3.a=333
    t3.b=323
    print("T's value -> ",t.a,",",t.b)#so class variable is referenced all the way through. Any change reflects the original values
    
    print("T3's value ->",t3.a,",",t3.b)