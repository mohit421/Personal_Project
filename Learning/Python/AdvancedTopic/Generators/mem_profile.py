import psutil
import os

# Function to check memory usage using psutil (Windows compatible)
def memory_usage_psutil():
    """Return the memory usage in MB using psutil."""
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / (1024 ** 2)  # Convert bytes to MB
    return mem

# Alternative memory check if needed (no resource module on Windows)
def memory_usage():
    """Alias for memory usage using psutil."""
    return memory_usage_psutil()

# Example usage
if __name__ == "__main__":
    print(f"Memory usage: {memory_usage()} MB")
