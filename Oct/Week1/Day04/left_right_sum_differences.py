def left_right_difference(nums):
    total = 0
    for num in nums:
        total += num
    answer = []
    left = 0
    for num in nums:
        right = total - left - num
        answer.append(abs(left - right))
        left += num
    return answer


print(left_right_difference([10, 4, 8, 3]))
print(left_right_difference([1]))
