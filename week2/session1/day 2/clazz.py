from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Run:
    milage: float
    duration: float
    location: Tuple[float, float]
    location_desc: str
    run_name: str

    def speed(self) -> float:
        """Return run speed in km/h"""
        return self.milage / (self.duration / 60)

    def pace(self) -> float:
        """Return run pace in min/km"""
        return self.duration / self.milage

    def get_location_desc_by_location(self):
        # TODO: Hopefully I will come back soon !!!
        return self.location_desc


def pace_fn(r: Run) -> float:
    return r.pace()


def distance_fn(r: Run) -> float:
    return r.milage


class RunApp:
    runs: List[Run]

    def __init__(self) -> None:
        self.runs = []

    def add_run(self, run: Run):
        self.runs.append(run)

    def best_pace(self) -> Run:
        return min(self.runs, key=pace_fn)

    def longest_run(self) -> Run:
        return max(self.runs, key=distance_fn)


# print(sorted(runs, key=pace_fn)[0])


milages = [4.38, 3.11, 4.82]
durations = [37.37, 33.47, 41.48]
locations = [(40.2, 36.3)] * 3
locations_desc = ["Belgrad", "MacFit", "Belgrad"]
runs_desc = ["Tuesday Run", "Belt Walk", "Before YKB Run"]

app = RunApp()


for m, d, l, ld, r in zip(milages, durations, locations, locations_desc, runs_desc):
    r = Run(
        milage=m,
        duration=d,
        location=l,
        location_desc=ld,
        run_name=r,
    )

    r.pace()

    print(
        f"Adding a new run {r.location_desc}@{r.location} with an average speed of {r.speed():.2f} km/h ({r.pace():.2f} min/km)"
    )

    app.add_run(r)

print(f"Your best run (per pace) is {app.best_pace().run_name} for this week")
print(f"Your longest milage is {app.longest_run().run_name} for this week")
