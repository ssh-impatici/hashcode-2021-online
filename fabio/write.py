from classes import *

# schedules = [
#     Schedule(
#         intersection=Intersection(1, [], []),
#         pairs=[
#             SchedulePair(street_in=Street("rue-d-athenes", "", "", 0), duration=2),
#             SchedulePair(street_in=Street("rue-d-amsterdam", "", "", 0), duration=1),
#         ],
#     ),
#     Schedule(
#         intersection=Intersection(0, [], []),
#         pairs=[
#             SchedulePair(street_in=Street("rue-de-londres", "", "", 0), duration=2),
#         ],
#     ),
#     Schedule(
#         intersection=Intersection(2, [], []),
#         pairs=[
#             SchedulePair(street_in=Street("rue-de-moscou", "", "", 0), duration=1),
#         ],
#     ),
# ]


def write(path, output):
    with open(path, "w") as file:
        # n. of intesections with schedules
        file.write(f"{len(schedules)}\n")

        for schedule in schedules:
            # Id of intersection
            file.write(f"{schedule.intersection.int_id}\n")
            # n. of schedule pairs
            file.write(f"{len(schedule.pairs)}\n")

            for sp in schedule.pairs:
                # name of street and duration
                file.write(f"{sp.street_in.name} {sp.duration}\n")


# # test
# write("./output.txt", schedules)
