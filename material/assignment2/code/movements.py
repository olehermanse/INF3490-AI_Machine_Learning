# Feel free to use numpy in your MLP if you like to.
import numpy as np
import mlp

filename = 'data/movements_day1-3.dat'

movements = np.loadtxt(filename,delimiter='\t')
movements[:,:40] = movements[:,:40]-movements[:,:40].mean(axis=0)
imax = np.concatenate(  ( movements.max(axis=0) * np.ones((1,41)) ,
                          np.abs( movements.min(axis=0) * np.ones((1,41)) ) ),
                        axis=0 ).max(axis=0)
movements[:,:40] = movements[:,:40]/imax[:40]

# Split into training, validation, and test sets
target = np.zeros((np.shape(movements)[0],8));
for x in range(1,9):
    indices = np.where(movements[:,40]==x)
    target[indices,x-1] = 1

# Randomly order the data
order = list(range(np.shape(movements)[0]))
np.random.shuffle(order)
movements = movements[order,:]
target = target[order,:]

train = movements[::2,0:40]
traint = target[::2]

valid = movements[1::4,0:40]
validt = target[1::4]

test = movements[3::4,0:40]
testt = target[3::4]

# Train the network
hidden = 12
net = mlp.mlp(train,traint,hidden)
net.earlystopping(train, traint, valid, validt)
net.confusion(test,testt)
