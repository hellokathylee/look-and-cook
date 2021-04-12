"""CSC111 Winter 2021 Project Phase 2: Final Submission

Description
===============================
This module creates a graph that will be used to sort recipes according to a user's
provided ingredients.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of TA's and professors
teaching CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2020 Dana Alshekerchi, Nehchal Kalsi, Kathy Lee, Audrey Yoshino.
"""

import data_reading
import data_type


def load_recipe_graph() -> data_type.Graph:
    """Return a recipe graph that corresponds to the provided recipe data set.

    The recipe graph stores one vertex for each ingredient and recipe in the dataset.
    Each vertex stores as its item either a ingredient NAME or recipe ID. The "kind" _Vertex
    attribute will differentiate between the two vertex types.

    Edges represent the use of an ingredient in a recipe i.e. a recipe will be adjacent to
    all it's required ingredients.

    >>> graph = load_recipe_graph()
    >>> len(graph.get_all_vertices(kind='recipe'))
    12351
    >>> len(graph.get_all_vertices(kind='ingredient'))
    943
    >>> peach_coffee_recipe = graph.get_neighbours('27546')
    >>> len(peach_coffee_recipe)
    12
    >>> 'peach' in peach_coffee_recipe
    True
    """
