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

def send_memory_stats(controller_ip, port=65432):
    worker_name = socket.gethostname()
    
    while True:
        try:
            # Get local memory usage
            mem_bytes = psutil.Process().memory_info().rss
            data = {
                "worker": worker_name,
                "usage_mb": mem_bytes / (1024 * 1024)
            }
            
            # Send to controller via TCP
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((controller_ip, port))
                s.sendall(json.dumps(data).encode('utf-8'))
                
            time.sleep(3)
        except Exception as e:
            print(f"Connection failed: {e}. Retrying in 3s...")
            time.sleep(3)        

if __name__ == "__main__":
    monitor_memory()