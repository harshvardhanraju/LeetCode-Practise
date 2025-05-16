class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_count = {5:0, 10:0, 20:0}
        
        for bill in bills:
            bill_count[bill] += 1

            if bill == 10:
                if bill_count[5] < 1:
                    return False
                else:
                    bill_count[5] -= 1
            elif bill == 20:
                #2 possible ways to give change
                if  bill_count[5] >= 1 and bill_count[10] >= 1:
                    bill_count[5] -= 1
                    bill_count[10] -= 1
                elif bill_count[5] >= 3:
                    bill_count[5] -= 3
                else:
                    return False
        return True

        