from collections import deque

class Solution:
    def invalidTransactions(self, transactions):
        n = len(transactions)
        parsed = []
        for i, t in enumerate(transactions):
            name, time, amount, city = t.split(',')
            parsed.append({
                'name': name, 'time': int(time), 
                'amount': int(amount), 'city': city, 
                'idx': i, 'raw': t
            })

        # Step 1: Sort by time to enable a sliding window
        parsed.sort(key=lambda x: x['time'])
        
        invalid_indices = set()
        # window stores the parsed objects currently within 60 mins of 'curr'
        window = deque()

        for curr in parsed:
            # Condition 1: Simple amount check
            if curr['amount'] > 1000:
                invalid_indices.add(curr['idx'])
            
            # Step 2: Maintain the window (remove transactions > 60 mins old)
            while window and curr['time'] - window[0]['time'] > 60:
                window.popleft()

            # Step 3: Manual scan of the window (No active_names map!)
            for other in window:
                if curr['name'] == other['name'] and curr['city'] != other['city']:
                    invalid_indices.add(curr['idx'])
                    invalid_indices.add(other['idx'])

            # Step 4: Add current transaction to the window
            window.append(curr)

        return [transactions[i] for i in invalid_indices]