import re

with open('./5/input.txt', 'r') as input:
    seedline = input.readline()
    seeds = [int(i) for i in seedline.split(':')[1].split()]

    new_seeds = []
    for j in range(0, len(seeds), 2):
        new_seeds += [seeds[j] + i for i in range(seeds[j+1])]
    input.readline()

    print(new_seeds)
    sources = new_seeds
    news = []
    title = ()
    for line in input:
        l = line[:-1]

        t = re.findall(r'^(\w+)-to-(\w+) map:$', line)
        if len(t) == 1:
            title = t
            continue

        if l == '':
            news += sources
            sources = news
            news = []
            print(sources)
            if (title[0][1] == 'location'):
                print(min(sources))
            continue

        (dest, source, r) = [int(i) for i in re.findall(r'^(\d+) (\d+) (\d+)$', line)[0]]
        
        for s in sources.copy():
            if s >= source and s < (source + r):
                sources.remove(s)
                news.append(s + (dest - source))
        