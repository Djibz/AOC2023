import re

with open('./5/input.txt', 'r') as input:
    seedline = input.readline()
    seeds = [int(i) for i in seedline.split(':')[1].split()]

    input.readline()

    sources = seeds
    news = []
    title = ()
    print(seeds)
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
            #print(sources)
        
            if (title[0][1] == 'location'):
                min = sources[0]
                for j in range(0, len(sources)-1, 2):
                    if sources[j] < min:
                        min = sources[j]
                print(min)
            continue

        (dest, source, r) = [int(i) for i in re.findall(r'^(\d+) (\d+) (\d+)$', line)[0]]

        ss = sources.copy()
        to_add = []
        for j in range(0, len(sources)-1, 2):
            (start, rm) = ss[j], ss[j+1]
            slide = dest - source

            if start >= source and start < source + r:
                if start + rm >= source and start + rm <= source + r:
                    news.append(start + slide)
                    news.append(rm)
                    
                else:
                    news.append(start + slide)
                    news.append(source + r - start)
                    to_add.append(source + r)
                    to_add.append(rm - (source + r - start))
                sources.remove(start)
                sources.remove(rm)

            elif start + rm >= source and start + rm <= source + r:
                
                to_add.append(start)
                to_add.append(source - start)

                news.append(source + slide)
                news.append(rm - (source - start))

                sources.remove(start)
                sources.remove(rm)

            elif start < source and start + rm > source + r:
                to_add.append(start)
                to_add.append(source - start)

                news.append(source + slide)
                news.append(r)

                to_add.append(source + r)
                to_add.append(start + rm - (source+r))

                sources.remove(start)
                sources.remove(rm)

        sources += to_add