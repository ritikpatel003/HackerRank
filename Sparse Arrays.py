strings=["aba","baba","aba","xzxb"]
queries=["aba","xzxb","ab"]
from collections import Counter
s = Counter(strings)
res = []
for i in queries:
	res.append(s[i])
print(res)