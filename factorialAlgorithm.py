import time 
import matplotlib.pyplot as plt 
import pandas as pd 

# function to compare factorial
def factorial(n):
    if n == 0 or n ==1:
        return 1
    return n * factorial(n-1)



# Range of input values
max_n = 20
results = []

# Compute factorial and runtime
for n in range(1, max_n + 1):
    start = time.perf_counter()
    fact = factorial(n)
    end = time.perf_counter()
    duration = (end - start) * 1e6
    results.append((n, fact, duration))

# Convert to DataFrame for nice table
df = pd.DataFrame(results, columns=["n", "fact", "runtime"])
print(df.to_string(index=False))

# plotting
plt.figure(figsize=(10,6))
plt.plot(df["n"], df["runtime"], marker='o', linestyle = "-")
plt.title("Runtime of Recursive Factorial")
plt.xlabel("n")
plt.ylabel("Runtime")
plt.grid(True)
plt.xticks(range(1, max_n + 1))
plt.tight_layout()
plt.show()


[1,2,3,4,5,6,7,8,9]

