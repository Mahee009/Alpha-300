class NumArray:
    def __init__(self, nums):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]


num_array = NumArray([-2, 0, 3, -5, 2, -1])
print(num_array.sumRange(0, 2), num_array.sumRange(2, 5), num_array.sumRange(0, 5))
print(NumArray([5]).sumRange(0, 0))
