# 🎓 Academic Coursework & Labs

A comprehensive suite of programming assignments, laboratories, and examination problems completed during **Year 1 Computer Science / Engineering**.

---

## 📚 Curriculum Breakdown

### 1. `special_assignments/`
- **`01_connect_game.py`**: Connect-3 6x6 board game against a computer opponent with gravity mechanics.
- **`02_bomb_proximity_grid.py`**: Chebyshev distance proximity field simulation on 2D matrices.

### 2. `lab_06_string_and_lists/`
Focus on string algorithms, list comprehensions, and recursion.
- `01_pangram_checker.py`: English pangram verification.
- `02_remove_duplicates.py`: In-place duplicate removal with custom bubble sort.
- `03_filter_short_words.py`: Word length threshold filtering.
- `04_sum_nested_list.py`: Recursive list summation.
- `05_count_elements.py`: Character occurrence counting across list elements.
- `06_filter_negative_numbers.py`: Matrix negative integer filtering.
- `07_count_negatives.py`: Negative number frequency counter.

### 3. `lab_06_1_data_structures/`
Focus on list slicing, recursive string manipulation, and leaderboard algorithms.
- `01_string_validation.py`: Alphabet and whitespace character filter.
- `02_add_two_lists.py`: Element-wise list addition.
- `03_flatten_list.py`: 2D to 1D nested list flattening.
- `04_common_members.py`: Set intersection across list sequences.
- `05_remove_vowels.py`: English vowel stripping.
- `06_add_last_element.py`: Cumulative boundary summation.
- `07_student_ranking.py`: Rank sorting and student ID lookup.
- `08_majority_element.py`: Majority candidate finder ($> n/2$).
- `09_recursive_reverse.py`: Recursive string reversal.

### 4. `lab_07_dictionaries/`
Focus on key-value data structures, nested objects, and record management.
- `01_student_scores.py`: Subject score map and GPA calculation.
- `02_nested_scores.py`: Multi-student gradebook and global average computation.
- `03_char_frequency.py`: Character frequency histogram.
- `04_record_collection.py`: Music database record mutations.

### 5. `lab_08_matrix_and_grids/`
Focus on 2D coordinates, board representations, and grid searching.
- `01_grid_board.py`: 6x6 grid board marker (1-36 index mapping).
- `02_word_search_grid.py`: 2D character matrix scanning and coordinate matching.

### 6. `final_exam/`
- `prime_factor_search.py`: Prime number sieve generator and target product factor search.

---

## 🧪 Testing All Lab Exercises

Run this command to execute and test all coursework scripts:

```bash
python -c "
import subprocess, glob
for pattern in ['04_academic_coursework/*/*.py']:
    for f in sorted(glob.glob(pattern)):
        res = subprocess.run(['python', f], capture_output=True, text=True)
        status = 'PASS' if res.returncode == 0 else 'FAIL'
        print(f'[{status}] {f}')
"
```
