class Solution:
    def exclusiveTime(self, n, logs):
        # result[i] will store the total exclusive time for function ID i
        result = [0] * n
        stack = []
        # prev_time marks the start of the current "block" of execution
        prev_time = 0
        
        for log in logs:
            # Parse the log string: "0:start:0" -> [0, "start", 0]
            fn_id, type, timestamp = log.split(':')
            fn_id, timestamp = int(fn_id), int(timestamp)
            
            if type == 'start':
                # If there's a function already on the stack, it was running 
                # until this very moment. Let's give it the time it earned.
                if stack:
                    result[stack[-1]] += timestamp - prev_time
                
                # Now push the new function onto the stack and update prev_time
                stack.append(fn_id)
                prev_time = timestamp
                
            else:  # type == 'end'
                # Pop the function that just finished
                top_fn = stack.pop()
                
                # The + 1 is crucial because an 'end' at timestamp 5 
                # means it ran THROUGH the end of the 5th second.
                result[top_fn] += timestamp - prev_time + 1
                
                # The next function starts at the beginning of the NEXT second
                prev_time = timestamp + 1
                
        return result