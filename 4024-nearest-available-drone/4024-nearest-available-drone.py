class Solution(object):
    def nearestDrone(self, drones, target):
        """
        :type drones: List[List[int]]
        :type target: List[int]
        :rtype: int
        """
        minn = float('inf')
        answer = -1

        tx, ty = target

        for i, (x, y, range_) in enumerate(drones):
            distance = abs(x - tx) + abs(y - ty)

            if distance <= range_ and distance < minn:
                minn = distance
                answer = i

        return answer