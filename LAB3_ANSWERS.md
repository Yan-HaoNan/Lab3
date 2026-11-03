# Lab 3 worksheet answers

## Exercise 1

The BMI classifications and returns are: BMI < 18.5 -> -1; 18.5 <= BMI <= 25.0 -> 0; BMI > 25.0 -> 1.

Command to add the Lab 2 repository as a submodule (already configured):

```powershell
git submodule add https://github.com/Yan-HaoNan/Lab2.git Lab2
```

For a fresh clone containing the submodule:

```powershell
git submodule update --init --recursive
```

Command to check files requiring staging or committing:

```powershell
git status
```

`__pycache__` contains automatically generated Python bytecode cache files (`.pyc`). These are recreated by Python, can vary by interpreter version, and do not need to be committed. `.gitignore` excludes these files and the pytest cache.

Tests: `Test_bmi.py` contains the three requested classification tests and tests at both BMI boundaries.

## Exercise 2: Table 3

| Requirement | Existing starter test | Completed coverage |
| --- | --- | --- |
| REQ-01: fewer than 10 integers, ascending | test_bubble_sort_ascending | Also test_bubble_sort_nine_numbers and test_bubble_sort_single_number |
| REQ-02: fewer than 10 integers, descending | test_bubble_sort_descending | Also test_bubble_sort_nine_numbers and test_bubble_sort_single_number |
| REQ-03: 10 or more numbers returns integer 1 | None | test_bubble_sort_too_many_numbers |
| REQ-04: no numbers returns integer 0 | None | test_bubble_sort_empty |
| REQ-05: a non-integer value returns integer 2 | None | test_bubble_sort_non_integer |

The starter invalid-order test is retained. Invalid sort orders return an empty list for nonempty lists of fewer than 10 integers. Size checks take priority when invalid conditions overlap; Table 3 does not define that overlap. Boolean values are rejected as non-integer inputs.

The starter defects were: 10+ elements returned -1, empty input returned [], and non-integer elements were not validated. These now return 1, 0, and 2 respectively.

Original remote shown by `git remote -v`:

```text
origin https://github.com/ET0735-DevOps-AIoT/Lab3.git (fetch)
origin https://github.com/ET0735-DevOps-AIoT/Lab3.git (push)
```

Command to use the personal repository:

```powershell
git remote set-url origin https://github.com/Yan-HaoNan/Lab3.git
```

## Exercise 3

`Lab2/Test_Lab2.py` tests `find_min_max`, `calc_average`, and `calc_median_temperature`. The supplied Lab 2 only had a median stub, so all three functions were implemented. They accept a sequence of temperatures. Minimum/maximum returns a tuple; average and median return numbers. Empty input raises ValueError. Tests include odd/even median lengths, negatives, duplicates, one value, and preservation of the input.

## Exercise 4

`total_cost_shopping` multiplies each known fruit price by its matching quantity and sums the costs. The supplied shopping basket totals 46.75. `test_price_info.py` tests the total, every fruit, zero quantity, missing quantities, and an empty basket. The PDF's `cost_of_fruit` spelling refers to the supplied `cost_of_fruits` function.

## Exercise 5

The average salary is 361000 / 6 = 60166.666666666664. Department lookup returns all matching records. `test_employee_info.py` tests average salary, all departments, unknown departments, age ranges, exact age exclusions, and empty records. The starter age function uses exclusive bounds (lower < age < upper), which are preserved because the PDF does not specify a change.

## Verification

```powershell
.venv/Scripts/python.exe -m pytest -q
```

Result: 59 passed. This includes the Lab 2 submodule tests and uppercase Test_bmi.py.

The PDF requests Lab3_v1.0 and Lab3_v2.0 tags, a Lab2_v3.0 release, and Lab3_v4.0 and Lab3_v5.0 releases. Publication status is recorded in README.md; commands described here are worksheet answers and do not by themselves indicate a successful push or release.
