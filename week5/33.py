InputList = list(map(int, input().split()))
Max = max(InputList)
IndexMax = InputList.index(Max)
Min = min(InputList)
IndexMin = InputList.index(Min)
Answer = InputList.copy()
Answer.insert(IndexMax, Min)
Answer.pop(IndexMax + 1)
Answer.insert(IndexMin, Max)
Answer.pop(IndexMin + 1)
print(*Answer)