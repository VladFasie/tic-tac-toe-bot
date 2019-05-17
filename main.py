from game import TicTacToe
from nn import NeuralNetwork
from threadtest import EvaluatorThread

import operator
import time

def generate_nn():
    return NeuralNetwork(18, [
        #[18, 'sigmoid'],
        [16, 'sigmoid'],
        #[14, 'sigmoid'],
        #[12, 'sigmoid'],
        #[10, 'sigmoid'],
        [9, 'sigmoid']
    ])

n = 4
k = 10000
nns = {}
for i in range(n):
    nns[generate_nn()] = 0

#nn.unbind_neurons(0, 0, 1)
#nn.unbind_neurons(0, 2, 0)
#nn.unbind_neurons(1, 1, 0)

#for i in nn.layers:
#    print(i)

def test():
    threads = []
    for nn in nns:
        th = EvaluatorThread(nn, k)
        threads.append(th)
        th.start()

    for th in threads:
        th.join()
        nns[th.nn] = th.score
        print('stopped simulation')

    sorted_nns = sorted(nns.items(), key=operator.itemgetter(1))
    print(sorted_nns)

start = time.time()
test()
stop = time.time()

print(stop - start)