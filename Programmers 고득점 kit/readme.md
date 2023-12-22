# Sorting a Hashmap in Reverse Order

## Sorting the Entire Hashmap

To sort a hashmap by its values in reverse order, you can use the `sorted` function along with the `items()` method. Here's an example:

```python
hashmap = {'A': 100, 'B': 200, 'C': 150}
sorted_hashmap = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
```

# Heap
import heapq as hp

hp.heapify(x)			# 리스트 x를 힙으로 반환한다.
hp.heappush(heap, item)		# item 값을 heap으로 push한다.
hp.heappop(heap)		# heap에서 가장 작은 값을 pop한다(=빼낸다).
hp.heappushpop(heap, item)	# heap에 item을 push한 후, heap에서 가장 작은 값을 pop한다. (개별 호출하는 것보다 더 효율적)
hp.heapreplace(heap, item)	# heap에서 가장 작은 값을 pop한 후, 새로운 item을 push한다. (개별 호출하는 것보다 더 효율적)

출처: https://mini-min-dev.tistory.com/202

heapq를 Max heap으로 사용하고 싶은 경우
```Python
import heapq

def solution(scoville, K):
    # Negate the values to create a max heap
    neg_scoville = [-x for x in scoville]
    heapq.heapify(neg_scoville)
    
    count = 0
    
    while len(neg_scoville) >= 2:
        first = -heapq.heappop(neg_scoville)  # Negate again to get the original value
        second = -heapq.heappop(neg_scoville)
        res = first + (second * 2)
        heapq.heappush(neg_scoville, -res)  # Negate before pushing onto the max heap
        count += 1
        if res > K:
            break
    
    return count if res > K else -1
```


# 문자열 비교를 통한 큰 수 만들기 예시

만약 3과 30이라는 두 숫자가 있을 때, 문자열로 변환하고 `x * 3`을 적용한 결과를 비교하면 다음과 같습니다:

1. 3을 문자열로 변환하면 '3'이 되고, `x * 3`은 '333'이 됩니다.
2. 30을 문자열로 변환하면 '30'이 되고, `x * 3`은 '303030'이 됩니다.

이제 '333'과 '303030'을 비교하는 것은 문자열 비교입니다. 파이썬에서는 문자열을 비교할 때, 첫 번째 문자부터 비교하며 크기를 판단합니다. 따라서 '333'에서 첫 번째 자리 숫자인 3과 '303030'에서 첫 번째 자리 숫자인 3을 비교하게 됩니다. 이 부분에서는 크기가 같으므로 두 번째 자리를 비교합니다. 이때 '333'은 자리수가 부족하므로 자신을 반복해서 채우는데, 결국 첫 번째 자리 숫자인 3과 두 번째 자리 숫자인 0을 비교하게 됩니다.

그 결과로 '333'에서 '303030'보다 큰 영향을 주게 됩니다. 이것이 큰 수를 만들기 위해 `x * 3`을 사용하는 이유입니다. 따라서 '333'이 '303030'보다 앞에 오게 되고, 이를 전체 리스트에 적용하면 두 숫자를 이어붙였을 때 '330'과 '3030'이 되며, '330'이 더 큰 수가 됩니다.

```Python
sorted_numbers = sorted(map(str, numbers), key=lambda x: x * 3, reverse=True)
```

# Map function

The `map` function applies a given function to each element of an iterable (such as a list or tuple) and returns the results.

```python
# Example
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]
```


# Permutation

```Python
from itertools import permutations

letters = ['A', 'B', 'C']
perms = permutations(letters, 2)
print(list(perms))  # Output: [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
```

# Combination
```python
from itertools import combinations

letters = ['A', 'B', 'C']
combs = combinations(letters, 2)
print(list(combs))  # Output: [('A', 'B'), ('A', 'C'), ('B', 'C')]
```

# Set update

```python
set1 = {1, 2, 3}
iterable = {3, 4, 5}

set1.update(iterable)
print(set1)  # Output: {1, 2, 3, 4, 5}
```
