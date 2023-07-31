import numpy as np
a=np.array([3,4,5,6,7])
a

def show_array(arr):
 print('shape:',arr.shape)
 print('size:',arr.size)
 print('type:',arr.dtype)
 print('length:',len(arr))
 print('array:',arr)
 print('type:',type(a))
 print('dimensions:',arr.ndim)
 
b=np.array([[10,34,56],[4,78,5],[6,9,4]])
b
show_array(b)
b[0][0]
b[1][1:]
b[:,-1]
b[:,-1].shape
c=np.array([[10,11,13,14],[45,22,9,2],[6,5,1,8]])
c
d=np.array([[[10,100],[11,110],[13,130],[14,140]],[[45,145],[22,122],[9,19],[2,12]],[[6,16],[5,15],[1,11],[8,18]]])
d
print(c[-1:,:])
print(d[:1,:2,:])
print(d[:,1:2,:1])
print(d[-2:,-1:,:1])
print(d[:2,-2:,:])
b[1,2]=90
b
np.append(a,80)
a=np.append(a,80)
a
np.append(c,[[9,90,900,9000]],axis=0)
np.append(c,[[9],[90],[900]],axis=1)
np.delete(b,0,axis=0)

a*2
a-2
a/2
a+2
c.reshape(2,6,1)
c.astype(float)
c.astype('uint16')
## more functions to create array
np.arange()
np.ones()
np.zeros()
np.linspace()
np.random.random()
np.random.randint()