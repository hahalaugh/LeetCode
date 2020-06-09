import collections


class Solution:

    def reorganizeString(self, s: str) -> str:
        counter = collections.Counter(s).most_common()
        n = counter[0][1]
        if n > (len(s) + 1) / 2:
            return ""
        
        r = [''] * len(s)
        step = len(s) // n if len(s) % n == 0 else len(s) // n + 1
        r[::step] = [counter[0][0]] * n
        
        for ch, count in counter[1:]:
            print(r)
            i = 0
            for _ in range(count):
                while i < len(r) and r[i] != '':
                    i += 1
                
                if r[i - 1] == ch:
                    i += 1
                r[i] = ch
            
        return ''.join(r)
        
        
s = Solution()
# print(s.reorganizeString("aab"))
# print(s.reorganizeString("aaabc"))
# print(s.reorganizeString("baaba"))
# print(s.reorganizeString("eqmeyggvp"))
# print(s.reorganizeString("abbabbaaab"))
print(s.reorganizeString("gpneqthatplqrofqgwwfmhzxjddhyupnluzkkysofgqawjyrwhfgdpkhiqgkpupgdeonipvptkfqluytogoljiaexrnxckeofqojltdjuujcnjdjohqbrzzzznymyrbbcjjmacdqyhpwtcmmlpjbqictcvjgswqyqcjcribfmyajsodsqicwallszoqkxjsoskxxstdeavavnqnrjelsxxlermaxmlgqaaeuvneovumneazaegtlztlxhihpqbajjwjujyorhldxxbdocklrklgvnoubegjrfrscigsemporrjkiyncugkksedfpuiqzbmwdaagqlxivxawccavcrtelscbewrqaxvhknxpyzdzjuhvoizxkcxuxllbkyyygtqdngpffvdvtivnbnlsurzroxyxcevsojbhjhujqxenhlvlgzcsibcxwomfpyevumljanfpjpyhsqxxnaewknpnuhpeffdvtyjqvvyzjeoctivqwann"))
