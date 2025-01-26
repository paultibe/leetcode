class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [] # strings
        
        wordMappings = {3: "Fizz", 5: "Buzz"}

        for i in range(1, n + 1):
            answerStr = ""
            for divisor in wordMappings:
                if i % divisor == 0:
                    answerStr += wordMappings[divisor]
            # not divisible, just append the index
            if not answerStr:
                answerStr += str(i)
            answer.append(answerStr)
        return answer