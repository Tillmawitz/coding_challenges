# Performance

My solution beat 36.8% of others in runtime and 5.63% in memory. In terms of runtime I fell into a valley between two clusters, indicating I had an uncommon approach. Most solutions used half the memory I did, indicating a lot of room for improvement. Overall, while I did produce a successful solution on my own, there is significant room for improvement in my approach to this kind of problem. Both solutions have time complexity $O(n\log{n})$ and space complexity $O(n)$

# Similarities in Solutions

- Used min heap to track smallest sums
- Used doubly linked list to keep track of neighbors
- Used lazy deletion for both min heap and nums
    - min heap tracked sum as well as components, if components were not valid sum was discarded
- Kept track of violations to remove need to iterate through nums repeatedly

# Key Differences

- Optimal solution implimented a doubly linked list data structure directly, I used a dictionary which added significant overhead
- I used a set to track pairs in violations, optimal simply kept track of the number of violations which decremented if the smallest sum was between a violation. After updating the nodes the count was updated again as the sum could still be a violation

# Reflection

While I used the optimal approach from a logical/algorithmic perspective, my solution left a lot of room for improvement. When iterating and improving a solution, I need to reflect more on what parts updates make obsolete. An example is when I added the components to the sum in the min heap, keeping track of which pairs resulted in violations (the set I used) became unnecessary and I could have moved to a count of violations like in the optimal solution. Not implimenting a doubly linked list directly was a result of a similar mistake. Going forward, focus more on keeping track of WHY we are using certain data structures or approaches so that I better recognize opportunities for improvement.

Originally completed 1/24/26