from simulator import simulate
from helpers import generate_nn
from genetic_operations import crossover

from random import randint
from concurrent.futures import ThreadPoolExecutor
import time
import operator

thread_pool_size = 4
number_of_individuals_in_generation = 36
number_of_selected_individuals = 8
number_of_simulations = 1000
number_of_generations = 12


def main():
    print('generation number\t|\tthe average percentage of the maximum score for selected\t|\t' +
          'the average percentage of the maximum score\t|\tscores')
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

        max_score = number_of_simulations
        scores = [x[1] for x in sorted_nns]
        medium_score_percent = sum(scores) / max_score / number_of_individuals_in_generation * 100
        medium_scores_percent_for_selected = sum(scores[:number_of_selected_individuals]) / max_score / \
            number_of_selected_individuals * 100

        print(str(generation) + ')\t',
              str(round(medium_scores_percent_for_selected, 2)) + '%\t',
              str(round(medium_score_percent, 2)) + '%\t',
              scores)

        if generation == number_of_generations:
            break

        selected = []
        for nn, _ in sorted_nns:
            selected.append(nn)
            if len(selected) == number_of_selected_individuals:
                break

        next_generation = []
        for _ in range(number_of_individuals_in_generation):
            idx1 = randint(0, len(selected) - 1)
            while True:
                idx2 = randint(0, len(selected) - 1)
                if idx1 != idx2:
                    break
            n1 = selected[idx1]
            n2 = selected[idx2]
            child = crossover(n1, n2)
            next_generation.append(child)

        nns.clear()
        for nn in next_generation:
            nns[nn] = 0

    stop = time.time()
    print(stop - start)


if __name__ == '__main__':
    main()
