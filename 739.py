class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        result = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while st:
                if temperatures[st[-1]] < temperatures[i]:
                    idx = st.pop()
                    result[idx] = i - idx
                else:
                    break
            st.append(i)
        return result