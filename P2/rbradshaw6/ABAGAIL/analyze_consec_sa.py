def analyze_sa(file_name):
    with open(file_name) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    sets = [[] for i in range(7)]

    curr_set = 0
    i = 0
    while (i < len(content)):
        curr = i + 2
        line = content[i]
        if ("ITER" in line):
            stop = line.index("R")
            num_lines = int(line[stop + 1: len(line) - 1])
            print num_lines
            for j in range(curr, curr + num_lines):
                data = content[j]
                comma = data.index(",")

                data = data[comma + 1:].replace("%", "")

                sets[curr_set].append(float(data))
            curr_set += 1
        i += 1

    iters = [10, 100, 1000, 2000, 10000, 20000, 100000]
    percents = [0.0 for i in range(7)]
    x = 0
    for result in sets:
        val_sum = 0.0
        for data in result:
            val_sum += data
        percents[x] = val_sum / float(iters[x])
        x += 1
    print percents




analyze_sa("sa_iter_curve_data.txt")
