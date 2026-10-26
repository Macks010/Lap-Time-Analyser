# Pull pit stop data
import fastf1 as ff1

session = ff1.get_session(2026, "Singapore", "R")
session.load()
ant_laps = session.laps.pick_driver("ANT")

caseInfo = ["LapTime", "Compound", "PitInTime", "PitOutTime"]
print("ANT")
# sort from fastest to slowest
ant_laps = ant_laps.sort_values("LapTime")
print(ant_laps[caseInfo].to_string(index=False))
# print