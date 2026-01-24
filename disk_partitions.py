import psutil

def count_partitions():
    try:
        # Fetch all disk partitions
        # all=False ignores virtual/internal file systems
        partitions = psutil.disk_partitions(all=False)
        
        if not partitions:
            print("No physical partitions detected.")
            return

        print("--- Detected Partitions ---")
        for p in partitions:
            try:
                # Some devices might trigger a PermissionError when accessing their details
                print(f"Device: {p.device} | Mountpoint: {p.mountpoint} | Type: {p.fstype}")
            except Exception as e:
                print(f"Could not read details for device {p.device}: {e}")
        
        print("---------------------------")
        print(f"Total physical partitions detected: {len(partitions)}")

    except PermissionError:
        print("Error: Permission denied. Try running the script with elevated privileges (sudo/admin).")
    except OSError as e:
        print(f"System error encountered: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    count_partitions()