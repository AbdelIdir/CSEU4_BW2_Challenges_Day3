# Time:  O(n)
# Space: O(h), h is the depth of the recursion

# Given an encoded string, return it's decoded string.
#
# The encoding rule is: k[encoded_string],
# where the encoded_string inside the square brackets is
# being repeated exactly k times. Note that k is guaranteed
# to be a positive integer.
#
# You may assume that the input string is always valid;
# No extra white spaces, square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not
# contain any digits and that digits are only for those repeat numbers, k.
# For example, there won't be input like 3a or 2[4].
#
# Examples:
#
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".


2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num = ""

        stack = []
        stack.append(["", 0])
        for ch in s:
            # 123456789
            if ch.isdigit():
                num += ch
            elif ch == '[':
                # num
                stack.append(["", int(num)])
                num = ""
            elif ch == ']':
                sub = stack[-1][0] * stack[-1][1]
                stack.pop()
                stack[-1][0] += sub
            else:
                # characters
                stack[-1][0] += ch
        return stack[0][0]


yyoo = Solution()

print(yyoo.decodeString("3[a]2[bc]"))
