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
    plt.plot(plot_laps["LapNumber"], lap_times_seconds, marker="o")
    plt.xlabel("Lap Number")
    plt.ylabel("Lap Time (seconds)")
    plt.title(f"{Driver} Lap Times - {Year} {Race}")
    plt.grid(True)
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
    plt.plot(plot_laps["LapNumber"], lap_times_seconds, marker="o")
    plt.xlabel("Lap Number")
    plt.ylabel("Lap Time (seconds)")
    plt.title(f"{Driver} Lap Times - {Year} {Race}")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    # Take 2nd User Input
    Race2 = input("Enter 2nd Circuit Name: ")
    Year2 = input("Enter 2nd Year: ")
    Session2 = input("Enter 2nd Session: ")
    Driver2 = input("Enter 2nd Driver: ")
    # Get Session
    session = ff1.get_session(Year, Race, Session)
    session.load()
    cant_laps = session.laps.pick_driver(Driver2)
    caseInfo = ["LapTime", "Compund", "PitInTime", "PitOutTime"]
    print(Driver2)
    # Sort from fastest to slowest and print
    print(cant_laps.sort_values("LapTime")[caseInfo].to_string(index=False))
    # Plot lap time against lap number in race order.
    plot_laps = cant_laps.dropna(subset=["LapNumber", "LapTime"]).sort_values("LapNumber")
    lap_times_seconds = plot_laps["LapTime"].dt.total_seconds()
    plt.plot(plot_laps["LapNumber"], lap_times_seconds, marker="o")
    plt.xlabel("Lap Number")
    plt.ylabel("Lap Time (seconds)")
    plt.title(f"{Driver} Lap Times - {Year} {Race}")
    plt.grid(True)
    plt.tight_layout()
    plt.show()