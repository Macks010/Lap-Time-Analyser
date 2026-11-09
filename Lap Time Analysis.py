# Pull pit stop data
import fastf1 as ff1
import matplotlib.pyplot as plt
import numpy as np

# Take User Input
Race = input("Enter Circuit Name (i.e Singapore): ")
Year = int(input("Enter Year of Race (2018 or Later): "))
Session = input("Enter Session Type (i.e R, S, Q): ")
Driver = input("Input Driver Name (i.e ANT): ")
Compare = input("Do You Wish To Compare To Another Driver: ")
if Compare == False or Compare == "No":
    # Get Session
    session = ff1.get_session(Year, Race, Session)
    session.load()
    ant_laps = session.laps.pick_driver(Driver)
    caseInfo = ["LapTime", "Compound", "PitInTime", "PitOutTime"]
    print(Driver)
    # Sort from fastest to slowest and print
    print(ant_laps.sort_values("LapTime")[caseInfo].to_string(index=False))
    # Plot lap time against lap number in race order.
    plot_laps = ant_laps.dropna(subset=["LapNumber", "LapTime"]).sort_values("LapNumber")
    lap_times_seconds = plot_laps["LapTime"].dt.total_seconds()
    plt.figure(figsize=(12, 6))
    plt.plot(
        plot_laps["LapNumber"],
        lap_times_seconds,
        marker="o",
        markersize=4,
        label=Driver,
    )
    plt.xlabel("Lap Number")
    plt.ylabel("Lap Time (seconds)")
    plt.title(f"{Driver} Lap Times by Lap Number - {Year} {Race}")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
elif Compare == True or Compare == "Yes":
    # Get Session
    session = ff1.get_session(Year, Race, Session)
    session.load()
    ant_laps = session.laps.pick_driver(Driver)
    caseInfo = ["LapTime", "Compound", "PitInTime", "PitOutTime"]
    print(Driver)
    # Sort from fastest to slowest and print
    print(ant_laps.sort_values("LapTime")[caseInfo].to_string(index=False))
    # Plot lap time against lap number in race order.
    plot_laps = ant_laps.dropna(subset=["LapNumber", "LapTime"]).sort_values("LapNumber")
    lap_times_seconds = plot_laps["LapTime"].dt.total_seconds()
    plt.figure(figsize=(12, 6))
    plt.plot(
        plot_laps["LapNumber"],
        lap_times_seconds,
        marker="o",
        markersize=4,
        label=Driver,
    )
    plt.xlabel("Lap Number")
    plt.ylabel("Lap Time (seconds)")
    plt.title(f"{Driver} Lap Times by Lap Number - {Year} {Race}")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    # Take 2nd User Input
    Race2 = input("Enter 2nd Circuit Name: ")
    Year2 = int(input("Enter 2nd Year: "))
    Session2 = input("Enter 2nd Session: ")
    Driver2 = input("Enter 2nd Driver: ")
    # Get Session
    session2 = ff1.get_session(Year2, Race2, Session2)
    session2.load()
    driver2_laps = session2.laps.pick_driver(Driver2)
    caseInfo = ["LapTime", "Compound", "PitInTime", "PitOutTime"]
    print(Driver2)
    # Sort from fastest to slowest and print
    print(driver2_laps.sort_values("LapTime")[caseInfo].to_string(index=False))
    # Plot lap time against lap number in race order.
    plot_laps = driver2_laps.dropna(subset=["LapNumber", "LapTime"]).sort_values("LapNumber")
    lap_times_seconds = plot_laps["LapTime"].dt.total_seconds()
    plt.figure(figsize=(12, 6))
    plt.plot(
        plot_laps["LapNumber"],
        lap_times_seconds,
        marker="s",
        markersize=4,
        label=f"{Driver2} ({Year2} {Race2})",
    )
    plt.xlabel("Lap Number")
    plt.ylabel("Lap Time (seconds)")
    plt.title(f"{Driver2} Lap Times by Lap Number - {Year2} {Race2}")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    # Compare Both
    driver1_plot_laps = ant_laps.dropna(
        subset=["LapNumber", "LapTime"]
    ).sort_values("LapNumber")
    driver2_plot_laps = driver2_laps.dropna(
        subset=["LapNumber", "LapTime"]
    ).sort_values("LapNumber")

    plt.figure(figsize=(12, 6))
    plt.plot(
        driver1_plot_laps["LapNumber"],
        driver1_plot_laps["LapTime"].dt.total_seconds(),
        marker="o",
        markersize=4,
        label=f"{Driver} ({Year} {Race})",
    )
    plt.plot(
        driver2_plot_laps["LapNumber"],
        driver2_plot_laps["LapTime"].dt.total_seconds(),
        marker="s",
        markersize=4,
        label=f"{Driver2} ({Year2} {Race2})",
    )
    plt.xlabel("Lap Number")
    plt.ylabel("Lap Time (seconds)")
    plt.title("Lap Time Comparison by Lap Number")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()