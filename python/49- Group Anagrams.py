class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = [] 
        for i in range(len(strs)):
            arr.append(("".join(sorted(strs[i])), strs[i]))
        dic = collections. defaultdict(list)
        for i in range(len(arr)): 
            if arr[i][0] not in dic:
                dic[arr[i][0]].append(arr[i][1]) 
            else: 
                dic[arr[i][0]].append(arr[i][1]) 
        return dic.values()
