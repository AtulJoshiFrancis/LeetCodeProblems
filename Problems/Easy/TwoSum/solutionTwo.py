from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # Create an empty dictionary to store the complement of each number and its index
    num_map = {}
    
    # Iterate through the list of numbers using enumerate to get both index and value
    for i, v in enumerate(nums):
        # If the current number is already in the dictionary, we have found the pair
        if v in num_map:
            # Return the indices of the two numbers that add up to the target
            return([num_map[v], i])
        
        # Calculate the complement (the number we need to find to sum up to the target)
        complement = target - v
        
        # Store the complement and its index in the dictionary
        # We store the complement as the key and the current index as the value
        num_map[complement] = i

    # If there is no valid solution (though the problem guarantees one solution), this will be reached.
    # You can add a return statement like `return []` to handle such cases, but it's not necessary as per the problem constraints.
