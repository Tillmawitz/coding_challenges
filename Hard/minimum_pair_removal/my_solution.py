import heapq

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        min_sums = 0
        n = len(nums)

        if n <= 1:
            return min_sums

        # Create doubly linked list with active boolean
        nodes = {}
        violations = set()

        for i in range(n):
            nodes[i] = {
                'value': nums[i],
                'left': i-1 if i > 0 else None,
                'right': i+1 if i < n-1 else None,
                'active': True
            }

        for i in range(n-1):
            if nums[i] > nums[i+1]:
                violations.add(i)

        # min heap (sum, left_id, right_id, left_val, right_val)
        heap = []
        for i in range(n-1):
            left_val = nums[i]
            right_val = nums[i+1]
            heapq.heappush(heap, (left_val + right_val, i, i+1, left_val, right_val))

        while violations:
            while heap:
                pair_sum, left_id, right_id, left_val, right_val = heapq.heappop(heap)

                # Check both nodes are active and neighbors, if not discard value and get next
                if (nodes[left_id]['active']
                and nodes[left_id]['value'] == left_val
                and nodes[right_id]['active']
                and nodes[right_id]['value'] == right_val
                and nodes[left_id]['right'] == right_id):
                    break

            left_neighbor = nodes[left_id]['left']
            right_neighbor = nodes[right_id]['right']

            valid_left = left_neighbor is not None and nodes[left_neighbor]['active']
            valid_right = right_neighbor is not None and nodes[right_neighbor]['active']

            # Discard related violations
            if valid_left:
                violations.discard(left_neighbor)
            violations.discard(left_id)
            violations.discard(right_id)

            # Deactivate right node, update left node value
            nodes[right_id]['active'] = False
            nodes[left_id]['value'] = pair_sum

            # Point left node to new right neighbor and vice versa
            nodes[left_id]['right'] = right_neighbor
            if valid_right:
                nodes[right_neighbor]['left'] = left_id
            
            # Add any new violations and update heap with new values
            if valid_left:
                if nodes[left_neighbor]['value'] > pair_sum:
                    violations.add(left_neighbor)
                
                left_sum = pair_sum + nodes[left_neighbor]['value']
                heapq.heappush(heap, (left_sum, left_neighbor, left_id, nodes[left_neighbor]['value'], pair_sum))
            
            if valid_right:
                if pair_sum > nodes[right_neighbor]['value']:
                    violations.add(left_id)

                right_sum = pair_sum + nodes[right_neighbor]['value']
                heapq.heappush(heap, (right_sum, left_id, right_neighbor, pair_sum, nodes[right_neighbor]['value']))

            min_sums += 1

        return min_sums