import sys
import os
import time

# import psutil
try:
    import psutil
except ImportError:
    print("Error: The 'psutil' library is not installed.")
    print("Please install it by running: pip install psutil")
    sys.exit(1)

def bytes_to_gb(bytes_value):
    """Converts bytes to Gigabytes (GB) for readability."""
    return bytes_value / (1024 ** 3)

def print_progress_bar(percent, label, length=30):
    """Prints a visual progress bar to the console."""
    filled_length = int(length * percent // 100)
    bar = '█' * filled_length + '-' * (length - filled_length)
    print(f"{label:<10} |{bar}| {percent:>5.1f}%")

def get_memory_usage():
    # 1. Get Virtual Memory (Physical RAM)
    # 'available' is memory that can be given instantly to processes without swapping.
    # 'used' is memory currently in use.
    svmem = psutil.virtual_memory()

    # 2. Get Swap Memory (Disk space used as RAM)
    swap = psutil.swap_memory()

    # Clear terminal (optional, works on Mac/Linux/Windows)
    os.system('cls' if os.name == 'nt' else 'clear')

    print("=" * 45)
    print(f" SYSTEM MEMORY USAGE")
    print("=" * 45)

    # --- Physical RAM Statistics ---
    print(f"Total RAM       : {bytes_to_gb(svmem.total):.2f} GB")
    print(f"Available RAM   : {bytes_to_gb(svmem.available):.2f} GB")
    print(f"Used RAM        : {bytes_to_gb(svmem.used):.2f} GB")
    print("-" * 45)
    
    # --- Swap Memory Statistics ---
    print(f"Total Swap      : {bytes_to_gb(swap.total):.2f} GB")
    print(f"Used Swap       : {bytes_to_gb(swap.used):.2f} GB")
    print(f"Free Swap       : {bytes_to_gb(swap.free):.2f} GB")
    print("-" * 45)

    # --- Visual Bars ---
    print("\nUtilization:")
    print_progress_bar(svmem.percent, "RAM")
    print_progress_bar(swap.percent, "SWAP")
    print("=" * 45)

if __name__ == "__main__":
    get_memory_usage()