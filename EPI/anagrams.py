def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    dic = defaultdict(list)
    for i in dictionary: 
        dic[''.join(sorted(i))] = []

    for i, val in enumerate(dictionary): 
        s_val = ''.join(sorted(val))
        if s_val in dic: 
            dic[s_val].append(val) 
    return [i for i in list(dic.values())  if len(i) > 1] 
