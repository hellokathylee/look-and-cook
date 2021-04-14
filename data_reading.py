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

This file is Copyright (c) 2020 Dana Alshekerchi, Nehchal Kalsi, Kathy Lee, Audrey Yoshino.
"""

from __future__ import annotations
from typing import Dict
import csv

RECIPES_FILE = "data/clean_recipes.csv"
REVIEWS_FILE = "data/reviews.csv"   # todo: upload file to repo


def read_recipes(file: str) -> Dict[str, list]:
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
    format the function 'read_recipes' returns data in."""
    ing = set()

    for i in data:
        ing.update(data[i][7])

    return ing


def get_review_scores(file: csv) -> Dict[str, float]:
    """Return a dictionary of recipe ids mapping to respective user ratings obtained
    from the given file."""
    unclean_reviews_dict = {}   # recipe_id: (score, length)

    with open(file) as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        next(reader)

        for row in reader:

            if row[0] in unclean_reviews_dict:
                unclean_reviews_dict[row[0]][0] += int(row[2])
                unclean_reviews_dict[row[0]][1] += 1
            else:
                unclean_reviews_dict[row[0]] = (int(row[2]), 1)

    reviews_dict = {x: unclean_reviews_dict[x][0] / unclean_reviews_dict[x][1]
                    for x in unclean_reviews_dict}

    return reviews_dict


def get_reviews(file: csv) -> Dict[str, list]:
    """Return a dictionary of recipe ids mapping to respective user reviews obtained
       from the given file."""
    reviews_dict = {}  # recipe_id: [reviews]

    with open(file) as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        next(reader)

        for row in reader:

            if row[0] in reviews_dict:
                reviews_dict[row[0]].append(row[3])
            else:
                reviews_dict[row[0]] = [row[3]]

    return reviews_dict


def clean_ingredients(data: Dict[str, list]) -> None:
    """Mutate the provided dictionary by cleaning the ingredients (removing measurements and
    strings that aren't ingredients).
    """
    words_to_remove = {'packages', 'cups', 'cup', 'tablespoons', 'tablespoon', 'teaspoon',
                       'teaspoons', 'packets', 'pounds', 'pound', 'inch', 'ounces', 'drops',
                       'dashes', 'jar', 'dash', 'envelope', 'container', 'package', 'crushed',
                       'ounce', 'cans', 'can', 'loaves', 'bottle', 'packet', 'tube', 'bottle',
                       'sheets', 'recipe'}

    remove_ingredients1 = {'marinate', 'low fat', 'breakfast', 'england', ' 2', 'fry', 'side',
                           'low sodium', 'Dry Mix Ingredients', 'kosher for passover', '2',
                           'mexico', 'raw', 'drained and mashed', 'without shells', 'bake',
                           'peeled and segmented', 'peeled and shredded', 'pan drippings',
                           'dessert', 'cubed', '(optional)', 'drained and chopped',
                           'Glaze', 'rinsed and dried', 'divided', 'thick circles',
                           'washed and cubed', 'mashed', 'fat free', 'Southern Comfort',
                           'peeled and julienned', 'lunch', 'chopped', 'stemmed and rinsed',
                           's thick', 'y', 'chopped', 'drained and finely chopped', 'top round',
                           'julienned', 'cleaned', 'boil', 'calories', 'party', 'gluten', 'Filling',
                           't'}

    remove_ingredients2 = {'rinsed and torn', 'and dried', 'rating',
                           'peeled and cubed', 'split', 'for topping', 'warmed'}

    for recipe in data:
        ingredients = data[recipe][7]
        ingredients_to_remove = set()
        ingredients_to_add = set()

        for ingredient in ingredients:
            add_ingredient = True
            new_ingredient = ingredient

            if ingredient == '':
                # If the ingredient is an empty string, remove it.
                ingredients_to_remove.add(ingredient)
                add_ingredient = False

            elif ingredient[-1] == ':' or ingredient.isupper() or ingredient in remove_ingredients1:
                # If a label has incorrectly been classified as an ingredient or the entire
                # string is not an ingredient, remove it.
                ingredients_to_remove.add(ingredient)
                add_ingredient = False

            elif ingredient[0] == ' ':
                # If the ingredient has a space at the beginning of it's string, remove the space
                new_ingredient = ingredient[1:]
                ingredients_to_remove.add(ingredient)

            elif any(character.isdigit() for character in new_ingredient):
                # If there is a number indicating the quantity of an ingredient, remove it (and the
                # space following it).
                numbers = [character for character in new_ingredient if character.isdigit()]
                number_index = new_ingredient.index(numbers[-1])

                new_ingredient = new_ingredient[number_index + 2:]

                ingredients_to_remove.add(ingredient)

            if ')' in new_ingredient:
                beginning = new_ingredient.index(')')

                new_ingredient = new_ingredient[beginning + 2:]

            for word in words_to_remove:
                # Remove measurements using key words
                if word in new_ingredient:
                    beginning = new_ingredient.index(word)
                    word_end_index = beginning + len(word)

                    new_ingredient = new_ingredient[word_end_index + 1:]

                    ingredients_to_remove.add(ingredient)

            for word in remove_ingredients2:
                # Remove entire ingredients if they aren't food items
                if word in ingredient:
                    ingredients_to_remove.add(ingredient)
                    add_ingredient = False

            if 'to taste' in new_ingredient:
                # If the substring 'to taste' is in the ingredient, remove the 'to taste'
                index = new_ingredient.index('to taste')
                new_ingredient = new_ingredient[:index]

            if add_ingredient:
                ingredients_to_add.add(new_ingredient)

        for ingredient in ingredients_to_remove:
            # Remove all the unnecessary ingredients: did not mutate in the for loop because of
            # possible errors
            ingredients.remove(ingredient)

        for ingredient in ingredients_to_add:
            final_ingredient = ingredient

            if ingredient != '':
                # As long as the new ingredient is not an empty string, add it to the recipe's
                # ingredients.
                if ingredient[0] == ' ':
                    # Ensure the ingredient we are adding does not have an unnecessary space at the
                    # beginning
                    final_ingredient = ingredient[1:]

                ingredients.add(final_ingredient)
