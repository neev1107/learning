# 🟠 Orange Belt — Python Coding Challenges (Dojo Format)

Same format and difficulty as the Kalvium Dojo proctored test challenges. Each question gives you starter code, a problem statement, Input/Output format, and worked examples — just like the real test.

---

## Challenge #1

**Given an integer `N`, print a right-angled triangle pattern of `*` with `N` rows, where row `i` (1-indexed) contains `i` stars.**

**Input Format:**
- A single line containing an integer `N`.

**Output Format:**
- Print `N` lines forming the pattern.

**Starter Code:**
```python
n = int(input())

# Write your logic here
```

**Example 1:**
```
Input:
4

Output:
*
**
***
****
```
**Explanation:** Row `1` has `1` star, row `2` has `2` stars, and so on up to row `4` which has `4` stars.

**Example 2:**
```
Input:
1

Output:
*
```
**Explanation:** With `N = 1`, only a single row with `1` star is printed.

---

## Challenge #2

**Numbers are entered one at a time until the sentinel value `-1` is entered. `-1` itself is not counted. Print the sum and the count of all numbers entered before the sentinel.**

**Input Format:**
- Multiple lines, each containing a single integer, ending with `-1`.

**Output Format:**
- Print a single line: `Sum: <sum> Count: <count>`

**Starter Code:**
```python
total = 0
count = 0

# Write your logic here (keep reading input() until you get -1)
```

**Example 1:**
```
Input:
10
20
30
-1

Output:
Sum: 60 Count: 3
```
**Explanation:** `10 + 20 + 30 = 60`, and `3` numbers were entered before the sentinel `-1`.

**Example 2:**
```
Input:
-1

Output:
Sum: 0 Count: 0
```
**Explanation:** The sentinel is entered immediately, so no numbers are added.

---

## Challenge #3

**Given an array of integers, print each element. While printing, skip (do not print) any element that is negative, and stop printing entirely (do not process any further elements) as soon as you encounter a `0`.**

**Input Format:**
- The first line contains an integer `N`, representing the number of elements in the array.
- The second line contains `N` space-separated integers.

**Output Format:**
- Print the qualifying elements separated by a space.

**Starter Code:**
```python
n = int(input())
arr = list(map(int, input().split()))

# Write your logic here (use continue to skip negatives, break on 0)
```

**Example 1:**
```
Input:
7
5 -3 8 -1 0 9 4

Output:
5 8
```
**Explanation:** `5` and `8` are printed, `-3` and `-1` are skipped (negative), and processing stops entirely at `0`, so `9` and `4` are never reached.

**Example 2:**
```
Input:
4
-2 -5 -7 6

Output:
6
```
**Explanation:** The first three elements are negative and skipped, and `6` is printed since it's neither negative nor zero. No `0` appears, so the loop runs to the end.

---

## Challenge #4

**Given a string, count the number of vowels (`a, e, i, o, u`, case-insensitive) and the number of consonants (alphabetic characters that are not vowels). Ignore spaces, digits, and punctuation. Print the counts in the format `Vowels: <count> Consonants: <count>`.**

**Input Format:**
- A single line containing a string `s`.

**Output Format:**
- Print a single line: `Vowels: <count> Consonants: <count>`

**Starter Code:**
```python
s = input()

# Write your logic here
```

**Example 1:**
```
Input:
Hello World

Output:
Vowels: 3 Consonants: 7
```
**Explanation:** Vowels are `e, o, o` (3 total). Consonants are `H, l, l, W, r, l, d` (7 total). The space is ignored.

**Example 2:**
```
Input:
Sky123

Output:
Vowels: 0 Consonants: 2
```
**Explanation:** `S` and `k` are consonants, `y` is not counted as a vowel here, and digits `1, 2, 3` are ignored.

---

## Challenge #5

**Trace the output of nested loops. Given two integers `N` and `M`, for every row `i` from `1` to `N`, print the product `i * j` for every `j` from `1` to `M`, space-separated, each row on a new line.**

**Input Format:**
- The first line contains an integer `N`.
- The second line contains an integer `M`.

**Output Format:**
- Print `N` lines, each containing `M` space-separated products.

**Starter Code:**
```python
n = int(input())
m = int(input())

# Write your logic here (use nested loops)
```

**Example 1:**
```
Input:
3
2

Output:
1 2
2 4
3 6
```
**Explanation:** Row `1`: `1*1=1, 1*2=2`. Row `2`: `2*1=2, 2*2=4`. Row `3`: `3*1=3, 3*2=6`.

**Example 2:**
```
Input:
2
1

Output:
1
2
```
**Explanation:** With `M = 1`, each row has only one product: `1*1=1` and `2*1=2`.

---

## Challenge #6

**Given an integer `N`, print a number pyramid pattern with `N` rows, where row `i` (1-indexed) contains the numbers from `1` to `i`, space-separated.**

**Input Format:**
- A single line containing an integer `N`.

**Output Format:**
- Print `N` lines forming the pattern.

**Starter Code:**
```python
n = int(input())

# Write your logic here
```

**Example 1:**
```
Input:
4

Output:
1
1 2
1 2 3
1 2 3 4
```
**Explanation:** Row `1` contains `1`, row `2` contains `1 2`, and so on up to row `4`.

**Example 2:**
```
Input:
2

Output:
1
1 2
```
**Explanation:** With `N = 2`, only two rows are printed, containing `1` and `1 2` respectively.

---

## Challenge #7

**A user keeps entering positive integers. The loop should stop as soon as the user enters a number that is NOT positive (zero or negative), and that stopping number should not be counted. Print the largest number entered before stopping.**

**Input Format:**
- Multiple lines, each containing a single integer, ending with a non-positive number.

**Output Format:**
- Print the largest positive number entered. If no positive number was entered before stopping, print `No numbers entered`.

**Starter Code:**
```python
largest = None

# Write your logic here (keep reading input() while the number is positive)
```

**Example 1:**
```
Input:
12
45
7
-1

Output:
45
```
**Explanation:** `12, 45, 7` are entered before the non-positive `-1` stops the loop, and `45` is the largest among them.

**Example 2:**
```
Input:
0

Output:
No numbers entered
```
**Explanation:** The very first input is `0`, which is non-positive, so the loop stops immediately with nothing counted.

---

## Challenge #8

**Given an array of integers, print only the elements at even indices (0-indexed: index 0, 2, 4, ...), but stop processing completely as soon as you encounter an element equal to `-1` at any index (even before checking if that index is even).**

**Input Format:**
- The first line contains an integer `N`, representing the number of elements in the array.
- The second line contains `N` space-separated integers.

**Output Format:**
- Print the qualifying elements separated by a space.

**Starter Code:**
```python
n = int(input())
arr = list(map(int, input().split()))

# Write your logic here
```

**Example 1:**
```
Input:
6
10 3 20 5 30 7

Output:
10 20 30
```
**Explanation:** Indices `0, 2, 4` hold `10, 20, 30`, and none of the elements is `-1`, so all even-indexed elements are printed.

**Example 2:**
```
Input:
5
10 3 -1 5 30

Output:
10
```
**Explanation:** `10` at index `0` is printed. At index `1`, the value is `3` (odd index, skipped). At index `2`, the value is `-1`, so processing stops immediately — `5` and `30` are never reached even though index `4` is even.

---

## Challenge #9

**Given a string, reverse the order of the words in it (not the characters within each word). Words are separated by single spaces.**

**Input Format:**
- A single line containing a string `s` of space-separated words.

**Output Format:**
- Print the words in reverse order, separated by a single space.

**Starter Code:**
```python
s = input()

# Write your logic here (using a loop; avoid built-in reverse tricks)
```

**Example 1:**
```
Input:
Dojo belt test is fun

Output:
fun is test belt Dojo
```
**Explanation:** The five words are printed in the opposite order they appeared in.

**Example 2:**
```
Input:
Hello World

Output:
World Hello
```
**Explanation:** With two words, they simply swap positions.

---

## Challenge #10

**Two loops are used to solve the same problem — printing all numbers from `1` to `N`. Loop A uses `for i in range(1, N+1)`, and Loop B uses a `while` loop with a manually incremented counter. Given `N`, simulate Loop B's logic and print how many times the loop body executes (i.e., how many times the counter is checked and found valid), followed by the sum of all numbers printed.**

**Input Format:**
- A single line containing an integer `N`.

**Output Format:**
- Print a single line: `Iterations: <count> Sum: <sum>`

**Starter Code:**
```python
n = int(input())
i = 1
count = 0
total = 0

# Write your logic here (use a while loop)
```

**Example 1:**
```
Input:
5

Output:
Iterations: 5 Sum: 15
```
**Explanation:** The while loop runs for `i = 1, 2, 3, 4, 5`, executing `5` times, and `1+2+3+4+5 = 15`.

**Example 2:**
```
Input:
0

Output:
Iterations: 0 Sum: 0
```
**Explanation:** Since `N = 0`, the condition `i <= N` fails immediately (as `i` starts at `1`), so the loop body never executes.

---

# ✅ Sample Solutions (check only after attempting)

**#1**
```python
n = int(input())
for i in range(1, n + 1):
    print("*" * i)
```

**#2**
```python
total = 0
count = 0
while True:
    num = int(input())
    if num == -1:
        break
    total += num
    count += 1
print(f"Sum: {total} Count: {count}")
```

**#3**
```python
n = int(input())
arr = list(map(int, input().split()))
result = []
for x in arr:
    if x == 0:
        break
    if x < 0:
        continue
    result.append(x)
print(*result)
```

**#4**
```python
s = input()
vowels = "aeiouAEIOU"
v_count = 0
c_count = 0
for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1
print(f"Vowels: {v_count} Consonants: {c_count}")
```

**#5**
```python
n = int(input())
m = int(input())
for i in range(1, n + 1):
    row = [str(i * j) for j in range(1, m + 1)]
    print(" ".join(row))
```

**#6**
```python
n = int(input())
for i in range(1, n + 1):
    row = [str(j) for j in range(1, i + 1)]
    print(" ".join(row))
```

**#7**
```python
largest = None
while True:
    num = int(input())
    if num <= 0:
        break
    if largest is None or num > largest:
        largest = num
print(largest if largest is not None else "No numbers entered")
```

**#8**
```python
n = int(input())
arr = list(map(int, input().split()))
result = []
for idx in range(n):
    if arr[idx] == -1:
        break
    if idx % 2 == 0:
        result.append(arr[idx])
print(*result)
```

**#9**
```python
s = input()
words = s.split()
reversed_words = []
i = len(words) - 1
while i >= 0:
    reversed_words.append(words[i])
    i -= 1
print(" ".join(reversed_words))
```

**#10**
```python
n = int(input())
i = 1
count = 0
total = 0
while i <= n:
    count += 1
    total += i
    i += 1
print(f"Iterations: {count} Sum: {total}")
```
