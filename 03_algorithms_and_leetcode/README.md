# 🧠 Algorithms & LeetCode Solutions

A curated collection of algorithmic challenges and LeetCode problem solutions implemented in Python 3, adhering to clean code standards, type annotations, Big-O complexity analysis, and automated test assertions.

---

## 📊 Summary Table

| # | Problem | Difficulty | Category | Time Complexity | Space Complexity | Solution File |
|:---:|:---|:---:|:---:|:---:|:---:|:---|
| 0001 | [Two Sum](https://leetcode.com/problems/two-sum/) | `Easy` | Array / Hash Table | $O(N)$ | $O(N)$ | [`0001_two_sum.py`](0001_two_sum.py) |
| 0003 | [Longest Substring Without Repeating](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | `Medium` | Sliding Window / Hash Table | $O(N)$ | $O(\min(N, M))$ | [`0003_longest_substring_without_repeating.py`](0003_longest_substring_without_repeating.py) |
| 0005 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | `Medium` | Two Pointers / String | $O(N^2)$ | $O(1)$ | [`0005_longest_palindromic_substring.py`](0005_longest_palindromic_substring.py) |
| 0007 | [Reverse Integer](https://leetcode.com/problems/reverse-integer/) | `Medium` | Math / Bit Guard | $O(\log_{10} N)$ | $O(1)$ | [`0007_reverse_integer.py`](0007_reverse_integer.py) |
| 0014 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | `Easy` | String / Vertical Scan | $O(S)$ | $O(1)$ | [`0014_longest_common_prefix.py`](0014_longest_common_prefix.py) |
| 0020 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | `Easy` | Stack / String | $O(N)$ | $O(N)$ | [`0020_valid_parentheses.py`](0020_valid_parentheses.py) |
| 0056 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | `Medium` | Array / Sorting | $O(N \log N)$ | $O(N)$ | [`0056_merge_intervals.py`](0056_merge_intervals.py) |
| 0202 | [Happy Number](https://leetcode.com/problems/happy-number/) | `Easy` | Hash Set / Math | $O(\log N)$ | $O(\log N)$ | [`0202_happy_number.py`](0202_happy_number.py) |
| - | Element Frequency Counter | `Fundamental` | Hash Map / Counting | $O(N)$ | $O(K)$ | [`element_frequency_counter.py`](element_frequency_counter.py) |

---

## 🧪 Running Tests

Each solution is self-contained with unit tests and assertions. To test all solutions:

```bash
python -c "
import subprocess, glob
for f in sorted(glob.glob('03_algorithms_and_leetcode/*.py')):
    res = subprocess.run(['python', f], capture_output=True, text=True)
    status = 'PASS' if res.returncode == 0 else 'FAIL'
    print(f'[{status}] {f}')
"
```
