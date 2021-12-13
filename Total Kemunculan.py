import collections

List = list(map(str,input().split()))

def TotalKemunculan(List):
    counting = collections.Counter(List)
    sorted_dict = {}
    sorted_keys = sorted(counting, key=counting.get)  
    for a in sorted_keys:
        sorted_dict[a] = counting[a]
    return sorted_dict

dipisah = TotalKemunculan(List)
for b in dipisah:
    print(b, ":", dipisah[b])
