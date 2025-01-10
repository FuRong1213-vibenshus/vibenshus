import random
import math

def secretary_problem(n, trials=10000):
    success = 0
    
    for _ in range(trials):
        candidates = list(range(1, n+1))
        random.shuffle(candidates)
        
        k = math.ceil(n / math.e)
        best_in_first_k = max(candidates[:k])
        
        for candidate in candidates[k:]:
            if candidate > best_in_first_k:
                if candidate == n:
                    success += 1
                break
                
    return success / trials

import matplotlib.pyplot as plt
n = 100
probability = secretary_problem(n)
print(f"Probability of selecting the best candidate: {probability:.4f}")

def secretary_probabilities(n_range, trials=10000):
    probabilities = []
    for n in n_range:
        probabilities.append(secretary_problem(n, trials))
    return probabilities

n_range = range(10, 201)
probabilities = secretary_probabilities(n_range)

plt.figure(figsize=(21, 10))
plt.plot(n_range, probabilities, marker='o', linestyle='-', color='tab:blue')
plt.axhline(y=1/math.e, color='r', linestyle='--', label='1/e')
plt.title('Probability of Selecting the Best Candidate')
plt.xlabel('Number of Candidates (n)')
plt.ylabel('Success Probability')
plt.legend()
plt.grid(lw=2,ls=':')
plt.show()
