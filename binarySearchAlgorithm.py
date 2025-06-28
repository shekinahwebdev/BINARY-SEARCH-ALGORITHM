import time
import matplotlib.pyplot as mplt
import seaborn as sns  
import pandas as pd


def binary_search_recursive(array, target, start, end):
    """
    Recursive binary search.
    Args:
        arr (list): The sorted list to search in.
        target: The item to search for.
        left (int): Left index.
        right (int): Right index.
    Returns:
        int: Index of target in arr if found, else -1.
    """

    # If the target is not found then return -1
    if start > end:
        return -1
    
    # If the target == middle
    middle = (start + end) // 2
    if array[middle] == target:
        return middle
    
    # If the target > middle move to the right
    elif array[middle] < target:
        start = middle + 1
        return binary_search_recursive(array, target, start, end)
    
    # If the target < middle move to the left
    elif array[middle] > target:
        end = middle - 1
        return binary_search_recursive(array, target, start, end)


# Data storage
data = []

input_sizes = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
for n in input_sizes:
    arr = list(range(1, n + 1))  # Sorted array from 1 to n
    target = n 

    # Measures start time
    start_time = time.perf_counter()

    # Perfom binary search
    result = binary_search_recursive(arr, target, 0, len(arr) - 1)

    # Measure end time
    end_time = time.perf_counter()

    # duration
    runtime = (end_time - start_time) * 1e6
    data.append([n, target, runtime, result])


# Convert to DataFrame for proper table representation
df = pd.DataFrame(data, columns=["Input Size", "Target", "Runtime (μs)", "Result Index"])
print(df.to_string(index=False))

# plotting
mplt.style.use('fivethirtyeight')
mplt.figure(figsize=(10,6))
mplt.plot(df["Input Size"], df["Runtime (μs)"],
          marker='o',
          linestyle='-',
          color='mediumvioletred',
          markerfacecolor='yellow',
          markeredgecolor='black',
          markersize=8,
          linewidth=2.5)
mplt.title("Binary Search Runtime Analysis", fontsize=14)
mplt.xlabel("Input Size (n)", fontsize=12)
mplt.ylabel("Runtime (μs)", fontsize=12)
mplt.grid(True)
mplt.xticks(df["Input Size"])
mplt.tight_layout()
mplt.legend(["Recursive Binary Search"])
mplt.show()