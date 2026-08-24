class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        stack = students

        while stack :
            if stack[0] == sandwiches[0] :
                stack.pop(0)
                sandwiches.pop(0)
            else :
                i = 0
                while i < len(stack) and stack[0] != sandwiches[0]:
                    i += 1
                    stack.append(stack.pop(0))

                if len(stack) == i :
                    break

        return len(sandwiches)