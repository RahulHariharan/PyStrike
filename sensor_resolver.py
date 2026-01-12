import psutil

def list_sensors():
    print("--- Hardware Sensors ---")

    # 1. Temperatures
    print("\n[Temperatures]")
    if hasattr(psutil, "sensors_temperatures"):
        temps = psutil.sensors_temperatures()
        if not temps:
            print("No temperature sensors detected.")
        for name, entries in temps.items():
            for entry in entries:
                print(f"{name}: {entry.current}°C (High: {entry.high}°C)")
    else:
        print("Temperature sensing not supported on this OS.")

    # 2. Fans
    print("\n[Fans]")
    if hasattr(psutil, "sensors_fans"):
        fans = psutil.sensors_fans()
        if not fans:
            print("No fan sensors detected.")
        for name, entries in fans.items():
            for entry in entries:
                print(f"{name}: {entry.current} RPM")
    else:
        print("Fan sensing not supported on this OS.")

    # 3. Battery
    print("\n[Battery]")
    if hasattr(psutil, "sensors_battery"):
        battery = psutil.sensors_battery()
        if battery:
            print(f"Percent: {battery.percent}%")
            print(f"Power Plugged: {battery.power_plugged}")
            print(f"Time Left: {battery.secsleft // 60} minutes")
        else:
            print("No battery detected.")

if __name__ == "__main__":
    list_sensors()