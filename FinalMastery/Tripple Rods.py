from typing import List
def processOrders(orders:List[int], sizes:List[int]) -> List[bool]:
    allCombo = []
    ans = []
    for i in sizes:
        for j in sizes:
            for k in sizes:
                allCombo.append(j+i+k)
    for i in sizes:
        for j in sizes:
            allCombo.append(i+j)
    allCombo = set(allCombo+sizes)
    for i in orders:
        if i in allCombo:
            ans.append(True)
        else:
            ans.append(False)
    return ans
assert (processOrders([5, 7, 13],[3, 5, 6, 10])==[True, False, True])
assert (processOrders([5, 12, 13, 18, 20, 31],[1, 2, 5, 10])==[True, True, True, False, True, False])
assert (processOrders([17, 92, 159],[10, 14, 32, 49])==[False, False, False])
assert (processOrders([7, 138, 148, 155, 185],[3, 5, 9, 24, 37, 46, 48, 50])==[False, True, True, False, False])
assert (processOrders([13, 31, 73, 92, 102, 134, 168, 188, 200],[2, 10, 17, 18, 30, 37, 39, 46, 47, 49])==[False, False, True, True, True, True, False, False, False])
assert (processOrders([2, 14, 29, 74, 75, 103, 108, 112, 132, 137, 184],[1, 6, 8, 9, 12, 13, 16, 17, 18, 26, 27, 32, 38, 41, 48])==[True, True, True, True, True, True, True, True, False, True, False])
assert (processOrders([2, 39, 41, 48, 86, 94, 123, 136, 140, 149, 161, 164, 191, 193],[1, 2, 9, 10, 11, 14, 17, 18, 24, 25, 32, 40, 41, 44, 45, 47, 49, 50])==[True, True, True, True, True, True, True, True, True, True, False, False, False, False])