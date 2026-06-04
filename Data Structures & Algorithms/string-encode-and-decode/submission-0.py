# Encode and Decode Strings
# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

class Solution:

    def encode(self, strs: List[str]) -> str:
        metadata = [f"{len(s):03d}" for s in strs] # max string len - 200, hence 3 digit
        meta_length = len(metadata)
        return f"{meta_length:03d}{"".join(metadata)}{"".join(strs)}"

    def decode(self, s: str) -> List[str]:
        offset = 3 # to read the length
        length = int(s[0:offset])

        chunks = []
        for i in range(0, length):
            chunks.append(int(s[offset:offset+3]))
            offset += 3

        res = []
        for c in chunks:
            res.append(s[offset:offset+c])
            offset += c
        
        return res
