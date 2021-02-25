from classes import *


def write(path, output):
    with open(path, "w") as file:
        # n. of intesections with schedules
        file.write(f"{len(output)}\n")

        for schedule in output:
            # Id of intersection
            file.write(f"{schedule.intersection.int_id}\n")
            # n. of schedule pairs
            file.write(f"{len(schedule.pairs)}\n")

            for sp in schedule.pairs:
                # name of street and duration
                file.write(f"{sp.street_in.name} {sp.duration}\n")