import random
from pprint import pprint

convi = ['껌','삼각김밥','콜라','사이다','구운계란']*100
random.shuffle(convi)
convi = convi[:50]

print(convi)

# dictionary 저장
# 아이템 : 개수
result = {}
for item in convi:
    result.setdefault(item,[]).append(item)

pprint(result)