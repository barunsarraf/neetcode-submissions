class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        result = []
        for ele in strs:
            current = "".join(sorted(ele))
            if current in d:
                current_list = d[current]
                current_list.extend([ele])
                d[current] = current_list
            else:
                d[current] = [ele]

        for key, value in d.items():
            result.append(value)
        return result