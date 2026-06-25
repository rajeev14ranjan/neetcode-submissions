# Alien Dictionary
# There is a new alien language that uses the English alphabet, but the order of the letters is unknown.
# You are given a list of strings words from the alien language's dictionary. It is claimed that the strings in words are sorted lexicographically by the rules of this new language.
# If this claim is incorrect, and the given arrangement of strings in words cannot correspond to any order of letters, return "".
# Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.
# A string a is lexicographically smaller than a string b if either of the following is true:
# The first letter where they differ is smaller in a than in b.
# a is a prefix of b and a.length < b.length.


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words) == 1: return words[0]

        graph = defaultdict(set)
        indegree = defaultdict(int)
        nodes = set()

        # build the graph and indegree count
        for i in range(len(words) - 1):
            for j in range(i+1, len(words)):
                a, b = words[i], words[j]
                nodes |= set(a)
                nodes |= set(b)

                same_count = 0
                min_length = min(len(a), len(b))
                for li in range(min_length):
                    cha, chb = a[li], b[li]

                    if cha != chb:
                        if chb not in graph[cha]:
                            graph[cha].add(chb)
                            indegree[chb] += 1
                        break
                    else:
                        same_count += 1
                
                # valide if these two words a, b were in correct order
                if same_count == min_length and len(a) > len(b): # the common part of words were same and larger word comes before smaller word
                    return ""

        # now do topological sort
        q = deque()
        result = []
        
        for n in nodes:
            if n not in indegree:
                q.append(n)
        
        while q:
            n = q.popleft()
            result.append(n)

            for ch in graph[n]:
                indegree[ch] -= 1
                if indegree[ch] == 0:
                    q.append(ch)

        isValid = len(result) == len(nodes) # cycle detection
        return "".join(result) if isValid else ""







