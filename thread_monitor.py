import psutil
import time
import os

def monitor_threads():
    try:
        while True:
            # Clear the terminal screen based on OS
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print(f"{'PROCESS NAME':<25} | {'PID':<8} | {'THREAD ID':<10}")
            print("-" * 50)
            
            total_threads = 0
            
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    # Fetch detailed thread objects for the process
                    threads = proc.threads()
                    total_threads += len(threads)
                    
                    for t in threads:
                        # t.id is the OS-level Thread ID
                        print(f"{proc.info['name'][:25]:<25} | {proc.info['pid']:<8} | {t.id:<10}")
                        
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    continue

            print("-" * 50)
            print(f"Total Active System Threads: {total_threads}")
            print("Refreshing in 5 seconds... (Ctrl+C to stop)")
            
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    monitor_threads()