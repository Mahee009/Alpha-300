# Day 02 — Contains Duplicate

**Topic:** Set membership

## Primary: Contains Duplicate

**Approach:** Go through the array and keep a set of numbers already seen. If the current number is already in the set, return True right away. If the loop finishes, there's no duplicate.

- **Time:** O(n)
- **Space:** O(n)

**Edge case:** _TODO_

## Variants

### Contains Duplicate II (LeetCode 219)

Keep a set holding only the last k numbers. Check before adding, and drop nums[i - k] once the set gets bigger than k.

- **Time:** O(n)
- **Space:** O(k)

### Find All Duplicates in an Array (LeetCode 442)

Values are 1 to n, so each value points to an index. Flip the sign at abs(value) - 1, and if it's already negative, that value has shown up before.

- **Time:** O(n)
- **Space:** O(1) extra, not counting the output

### First Repeating Element (GFG)

Walk from right to left with a set. Whenever the current number is already in the set, update the answer to its 1-based position, so the leftmost one wins.

- **Time:** O(n)
- **Space:** O(n)

### Duplicate Zeros (LeetCode 1089)

Count the zeros to know how far each element shifts, then fill from the back with two pointers, writing a zero twice and skipping anything that lands past the end.

- **Time:** O(n)
- **Space:** O(1)
