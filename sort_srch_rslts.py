"""CSC111 Final Project, Sorting Search Results

Description
===============================
This module uses output from search and sorts results based on user's specifications.
===============================

This file is provided solely for the personal and private use of TA's and professors
teaching CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2020 Dana Alshekerchi, Nehchal Kalsi, Kathy Lee, Audrey Yoshino.
"""
from typing import Dict, List


def time_sort(data: Dict[str, list], max_mins: int, dec_ord: bool = False) -> List[tuple]:
    """Return a dictionary of recipes from data sorted in increasing or decreasing order
    of the total time of the recipes depending on dec_ord. The total time of the recipes
    returned is less than the maximum minutes max_mins.

    If total time of a recipe is not available, do not include it in the return value.
    """
    times = {}
    sorted_recipes = []
    data_copy = data.copy()     # to not mutate the input

    for item in data:  # item = recipe id
        total_time = data_copy[item][6]
        total_time.replace(" ", "")   # remove the whitespace

        if total_time != "X":
            day, hour, minute = _split_time(total_time)

            minutes = (24 * 60 * int(day)) + (60 * int(hour)) + int(minute)
            times[item] = minutes   # convert time to mins

        else:
            data_copy.pop(item)

    # sort by value
    if dec_ord:
        sorted_times = sorted(times.items(), key=lambda x: x[1], reverse=True)

    else:
        sorted_times = sorted(times.items(), key=lambda x: x[1])

    for item in sorted_times:
        if item[1] <= max_mins:     # why getting error?
            sorted_recipes.append((item[0], data_copy[item[0]]))
        # use list instead of dictionary to maintain sort order

    return sorted_recipes


def _split_time(time: str) -> list[str]:
    """Return the given time in [day, hour, min] format."""
    assert time != 'X'
    time_lst = []

    if 'd' in time:     # manage day
        time_lst = time.split("d")
    else:
        time_lst.extend(['0', time])

    assert len(time_lst) == 2

    if 'h' in time_lst[1]:      # manage hour
        mixed_time = time_lst[1]
        time_lst.extend(time_lst[1].split("h"))
        time_lst.remove(mixed_time)
    else:
        time_lst.append(time_lst[1])
        time_lst[1] = '0'
        # pass

    assert len(time_lst) == 3

    if 'm' in time_lst[2]:  # manage min
        time_lst[2] = time_lst[2].strip("m")
    else:
        time_lst[2] = "0"

    return time_lst
