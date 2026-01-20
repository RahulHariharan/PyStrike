import psutil
import os
import time

def monitor_memory():
    process = psutil.Process(os.getpid())
    print(f"Monitoring memory for PID: {os.getpid()} every 3 seconds...")
    print("-" * 40)
    
    try:
        while True:
            # memory_info().rss gives the memory in bytes
            mem_bytes = process.memory_info().rss
            mem_mb = mem_bytes / (1024 * 1024)
            
            print(f"Current Memory Usage: {mem_mb:.2f} MB")
            
            time.sleep(3)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    monitor_memory()