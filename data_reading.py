"""CSC111 Final Project, Data Reading

Description
===============================
This module reads the raw data from the csv file and converts it into a usable format.
===============================

This file is provided solely for the personal and private use of TA's and professors
teaching CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

Nehchal can you see this?

This file is Copyright (c) 2020 Dana Alshekerchi, Nehchal Kalsi, Kathy Lee, Audrey Yoshino.
"""

from __future__ import annotations
from typing import Dict
import csv


def read(file: str) -> Dict[str, list]:
    """Read the given file and return a dictionary with recipe id mapping to
    other attributes of the recipe stored in a list.
    """
    recipe_dict = {}

    with open(file) as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        next(reader)

        for row in reader:
            dict_val = []   # list containing recipe attributes
            index = 0

            for inner_row in row[:9]:
                if index == 7:  # ingredients
                    dict_val.append(set(inner_row.split(',')))

                elif index == 8:    # directions
                    sntnc = row[8].strip("'")
                    if not sntnc[-2:] == "**":
                        sntnc = sntnc + "**"    # to split every bullet point
                    dict_val.append(list(sntnc.split('**'))[:-1])

                else:
                    dict_val.append(inner_row.strip())

                index += 1

                recipe_dict[row[9].strip()] = dict_val  # remove extra space before assigning

    return recipe_dict


def get_ingredients(data: Dict[str, list]) -> set:
    """Return a set of ingredients given data complying to the
    format the function 'read' returns data in."""
    ing = set()

    for i in data:
        ing.update(data[i][7])

    return ing
