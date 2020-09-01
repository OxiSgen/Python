from collections import Counter
from operator import itemgetter

with open('file.txt', 'r', encoding="utf-8") as file:
    words = [i.lower() for i in file.read().replace(';', '').replace(',', '').replace(':', '').split()]
common = sorted(sorted(Counter(words).most_common()), key=itemgetter(1), reverse=True)
print(*common[0])
