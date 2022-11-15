import h5py
import numpy as np
import matplotlib.pyplot as plt

data=h5py.File('kerry_440_400_50_W.mat')
datax=data['kerry_440_400_50_W']
print(datax.shape)
data1=np.zeros([440,400,50,1])    
for i in range(0,400):
    data1[:,i,:,0]=np.transpose(np.squeeze(datax[:,i,:]))
fig = plt.figure(3)
plt.imshow(data1[1].squeeze(), aspect='auto')
plt.show()
np.save('kerry_440_400_50_1_W.npy',data1)   # Input data of the network