#Robert Bradshaw is a god.

import sys
def analyze_results():

    file_name = sys.argv[1]
    test_names = ["RHC", "SimulatedAnnealing", "GeneticAlgorithm", "MIMIC"]
    with open(file_name) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    tups = [[] for _ in range(4)]

    current_test = 0
    for i in range(len(content)):
        if ("," in content[i]):
            current = content[i]
            stop = current.index(',')
            tups[current_test].append(((current[:stop]), current[(stop + 2):]))
        else:
            if ('-' in content[i] and current_test < 3 and i > 4):
                current_test += 1

    i = 0
    for test in tups:
        val_sum = 0.0
        time_sum = 0.0
        size = 0

        for result in test:
            val_sum += float(result[0])
            time_sum += float(result[1])
            size += 1
        if (size > 0):
            print test_names[i] + ": (" + str((float(val_sum) / size)) + ", " + str((float(time_sum) / size)) + " seconds)"
        else:
            print "fail"
        i += 1


analyze_results()
