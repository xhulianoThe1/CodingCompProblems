class Solution(object):
    def groupAnagrams(self, strs):
        dic = {} 
        for i in strs: 
            s_str = ''.join(sorted(i))
            dic[s_str] = []
        for i in strs: 
            s_str = ''.join(sorted(i))
            dic[s_str].append(i)
        return dic.values()
