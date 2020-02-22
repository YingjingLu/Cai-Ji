def maxLevelSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        max_level = 0
        cur_level = 1
        max_sum =  (-2)**31
        queue = []
        new_queue = []
        queue.append( root )
        while len( queue ) != 0:
            cum_sum = 0
            while len( queue ) != 0:
                node = queue.pop()
                cum_sum += node.val
                if node.left is not None:
                    new_queue.append( node.left )
                if node.right is not None:
                    new_queue.append( node.right )
            if max_sum < cum_sum:
                max_level = cur_level
                max_sum = cum_sum
            queue = new_queue
            new_queue = []
            cur_level += 1
        return max_level