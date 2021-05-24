class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        ans, digit_logs, letter_logs = [], [], []
        for log in logs:
            tokens = log.split()
            if tokens[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        
        letter_logs = sorted(letter_logs, key=lambda x: x.split()[0])
        letter_logs = sorted(letter_logs, key=lambda x: ' '.join(x.split()[1:]))

        ans.extend(letter_logs)
        ans.extend(digit_logs)
        return ans
        