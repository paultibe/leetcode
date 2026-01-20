import heapq
from collections import defaultdict

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

        # 1. Sort by time O(N log N)
        parsed.sort(key=lambda x: x['time'])
        
        invalid_indices = set()
        # Heap stores (expiry_time, name, city, original_index)
        heap = []
        # Map stores name -> {city: set of indices}
        active_names = defaultdict(lambda: defaultdict(set))

        for curr in parsed:
            # Check amount rule immediately
            if curr['amount'] > 1000:
                invalid_indices.add(curr['idx'])
            
            # 2. Remove expired transactions (older than curr['time'] - 60)
            while heap and heap[0][0] < curr['time'] - 60:
                _, name, city, idx = heapq.heappop(heap)
                active_names[name][city].remove(idx)
                if not active_names[name][city]:
                    del active_names[name][city]

            # 3. Check for same name but different city in the current window
            if curr['name'] in active_names:
                for city, indices in active_names[curr['name']].items():
                    if city != curr['city']:
                        # Current is invalid
                        invalid_indices.add(curr['idx'])
                        # All previous transactions in different cities are also invalid
                        invalid_indices.update(indices)

            # 4. Add current to heap and map
            heapq.heappush(heap, (curr['time'], curr['name'], curr['city'], curr['idx']))
            active_names[curr['name']][curr['city']].add(curr['idx'])

        return [transactions[i] for i in invalid_indices]