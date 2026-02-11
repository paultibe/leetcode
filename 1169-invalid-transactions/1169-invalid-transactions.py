class Solution:
    def invalidTransactions(self, transactions):
        n = len(transactions)
        parsed = []
        for t in transactions:
            name, time, amount, city = t.split(',')
            parsed.append({'name': name, 'time': int(time), 'amount': int(amount), 'city': city})
        
        invalid_indices = set()
        
        for i in range(n):
            # Condition 1: Simple amount check
            if parsed[i]['amount'] > 1000:
                invalid_indices.add(i)
            
            # Condition 2: Compare against every other transaction
            for j in range(i + 1, n): # Start from i+1 to avoid checking the same pair twice
                if parsed[i]['name'] == parsed[j]['name'] and parsed[i]['city'] != parsed[j]['city']:
                    if abs(parsed[i]['time'] - parsed[j]['time']) <= 60:
                        invalid_indices.add(i)
                        invalid_indices.add(j)
                        
        return [transactions[idx] for idx in invalid_indices]