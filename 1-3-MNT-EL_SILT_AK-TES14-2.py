import array as arr
import numpy as np
w1=[1,0.8,0]
w2=[0,0.8,-1.0]
w3=[0.5,0.5]
e = arr.array('i',[0,0,0,0,1,1,1,1])
s = arr.array('i',[0,0,1,1,0,0,1,1])
a=  arr.array('i',[1,0,1,0,1,0,1,0])
op= arr.array('i',[0,0,0,1,1,1,1,1])
i=0
def act(r):
      return (1/(1+ np.exp(-r)))

while i<8:

        inputs=np.array([e[i],s[i],a[i]])
        hid1=w1@inputs
        b=act(hid1)
        hid2=w2@inputs
        c=act(hid2)
        ot=np.array([b,c])@w3
#       out =act(ot)

        if ot>=0.6:
              work=1
        else:
              work=0

        if work==op[i]:      
              print("e={},s={},a={},op={},work={},predict true".format(e[i],s[i],a[i],op[i],work))        
        else:
              print("e={},s={},a={},op={},work={},predict false".format(e[i],s[i],a[i],op[i],work))
        i=i+1 

