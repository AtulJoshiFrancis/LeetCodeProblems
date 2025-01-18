from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    """
    Given a list of integers `nums` and an integer `target`, 
    this function finds two distinct indices in the list such that 
    the sum of the elements at these indices equals `target`.

    Args:
    nums (List[int]): A list of integers where each element is in the range [-10^9, 10^9].
    target (int): The target sum for which we need to find two distinct numbers.

    Returns:
    List[int]: A list of two indices `[i, j]` such that `nums[i] + nums[j] == target`.
               The order of the indices in the result can vary.

    Time Complexity:
    O(n^2) where n is the number of elements in `nums`. This is because we are iterating through 
    every pair of elements in the list.

    Space Complexity:
    O(n) where n is the number of elements in `nums`. This is the space used by the `output` set 
    to store unique indices.
    """
    
    output = set()  # Initialize an empty set to store the unique indices of the numbers that sum to target

    # Iterate over the list of numbers with indices
    for i, v in enumerate(nums):
        # Iterate over the list of numbers with indices again
        for j, w in enumerate(nums):
            # Check if the two numbers are at different indices (i < j) and their sum equals the target
            if i < j and v + w == target:
                # Add both indices to the output set to ensure they are unique
                output.add(i)
                output.add(j)
    
    # Convert the set of indices into a list and return
    return list(output)
