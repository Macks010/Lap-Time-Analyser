# Pull pit stop data
import fastf1 as ff1

# Take User Input
Race = input("Enter Circuit Name (i.e Singapore): ")
Year = int(input("Enter Year of Race: "))
Session = input("Enter Session Type (i.e R, S, Q): ")
Driver = input("Input Driver Name (i.e ANT): ")

# Get Session
session = ff1.get_session(Year, Race, Session)
session.load()
ant_laps = session.laps.pick_driver(Driver)
caseInfo = ["LapTime", "Compound", "PitInTime", "PitOutTime"]
print(Driver)
ant_laps = ant_laps.sort_values("LapTime")

# sort from fastest to slowest and print
print(ant_laps[caseInfo].to_string(index=False))