import urllib.request


# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())

counts = dict()
with urllib.request.urlopen('http://data.pr4e.org/romeo.txt') as f:
    for line in f:
        words = line.decode().split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1

print(counts)