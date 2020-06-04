class Solution:
    def reverseWords(self, s: str) -> str:
        result = ''
        for item in s.split(' '):
            result += ''.join(reversed(item)) + ' '
        return result[:len(result)-1]

    def reverseWords2(self, s: str) -> str:
        return ' '.join(item[::-1] for item in s.split(' '))


# 讲解，reversed()实际上返回的是一个反向的迭代器，
# 是不能用来直接和str相加，想要得到str，直接''.join()即可，反正插入的是空字符串

s = Solution()
print(s.reverseWords2("Let's take LeetCode contest"))
