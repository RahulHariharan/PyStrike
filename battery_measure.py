import psutil

def check_battery_status():
    # psutil.sensors_battery() returns None if no battery is installed
    battery = psutil.sensors_battery()

    if battery is None:
        print("No Charge Required, This is a Desktop")
    else:
        # Get the battery percentage
        percent = battery.percent
        
        # Check if the device is plugged in
        plugged_in = battery.power_plugged
        status = "Plugged In" if plugged_in else "Not Plugged In"
        
        print(f"Device is a Laptop.")
        print(f"Battery Charge: {percent}%")
        print(f"Power Status: {status}")

if __name__ == "__main__":
    check_battery_status()