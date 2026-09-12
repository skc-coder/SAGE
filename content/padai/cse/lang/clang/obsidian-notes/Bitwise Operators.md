https://cp-algorithms.com/algebra/bit-manipulation.html#setflipclear-a-bit
Left shift:
~~if 1 is not cut off at left then shift by k~~
increases the number by 2^k.

Right shift:
if 1 is not cut off at right then divide by 2^k.
If number is Unsigned – fill zeros
If number is signed – depends on system (either zeros or sign bit


Complement finds 1s complement.

class Solution:

def missingNumber(self, nums: List[int]) -> int:

xor = len(nums)

for i, n in enumerate(nums):

xor ^= i^n

return xor

  

https://leetcode.com/problems/missing-number/