class Solution(object):
    
    def isNStraightHand(self, hand, W):
        #ÿ��ȡ��Сֵ���һ���ƣ�ֱ��������Ϊֹ
        if len(hand) % W != 0: return False
        counter = collections.Counter(hand)
        
        while counter:
            m = min(counter)
            for k in range(m, m+W):
                if k not in counter: 
                    return False
                v = counter[k]
                if v == 1:
                    del counter[k]
                else:
                    counter[k] -= 1
            
        return True
    
    def isNStraightHandBF(self, hand, W):
        #������ջģ��
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        
        if len(hand) % W != 0: return False
        hand.sort()
        d = []
        for n in hand:
            found = False
            for i in range(len(d)):
                if d[i][-1] == n - 1 and len(d[i]) < W:
                    found = True
                    d[i].append(n)
                    break
            if not found:
                d.append([n])
            
            if len(d) > len(hand)/W: 
                return False
            
        return len(d) == len(hand) / W