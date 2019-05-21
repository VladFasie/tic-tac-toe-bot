from simulator import simulate
from helpers import generate_nn
from genetic_operations import crossover

from random import randint
from concurrent.futures import ThreadPoolExecutor
import time
import operator

thread_pool_size = 2
number_of_individuals_in_generation = 12
number_of_selected_individuals = 3
number_of_simulations = 1000
number_of_generations = 4


def main():
    print('generation number\t|\tmedium win rate of selected\t|\tmedium win rate\t|\twin rates')
    start = time.time()
    executor = ThreadPoolExecutor(thread_pool_size)
    nns = {}
    for i in range(number_of_individuals_in_generation):
        nns[generate_nn()] = 0

    for generation in range(1, number_of_generations + 1):
        futures = []
        for nn in nns:
            futures.append(executor.submit(simulate, nn, number_of_simulations))

        for nn, future in zip(nns, futures):
            score = future.result()
            nns[nn] = score

        sorted_nns = sorted(nns.items(), key=operator.itemgetter(1), reverse=True)
        # save the best from current generation
        sorted_nns[0][0].save('bot' + str(generation) + '.nn')

        win_rates = [x[1] / number_of_simulations for x in sorted_nns]
        medium_win_rate = sum(win_rates) / number_of_individuals_in_generation * 100
        medium_win_rate_for_selected = sum(win_rates[:number_of_selected_individuals]) / number_of_selected_individuals * 100
        print(str(generation) + ')\t',
              str(round(medium_win_rate_for_selected, 2)) + '%\t',
              str(round(medium_win_rate, 2)) + '%\t',
              win_rates)

        if generation == number_of_generations:
            break

        selected = []
        for nn, _ in sorted_nns:
            selected.append(nn)
            if len(selected) == number_of_selected_individuals:
                break

        next_generation = []
        for _ in range(number_of_individuals_in_generation):
            n1 = selected[randint(0, len(selected) - 1)]
            n2 = selected[randint(0, len(selected) - 1)]
            child = crossover(n1, n2)
            next_generation.append(child)

        nns.clear()
        for nn in next_generation:
            nns[nn] = 0

    stop = time.time()
    print(stop - start)


if __name__ == '__main__':
    main()
