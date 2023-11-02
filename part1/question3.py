from enum import Enum

################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ <
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ /
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/
#
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at
# different temperatures to craft special materials.
#
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected
# formulas and their outputs in the test file, `question3_test.py`.


# This function should return an oven instance!
def make_oven():
    return MagicalOven()


def alchemy_combine(oven, ingredients, temperature):
    for item in ingredients:
        oven.add(item)

    if temperature < 0:
        oven.freeze()
    elif temperature >= 100:
        oven.boil()
    else:
        oven.wait()

    return oven.get_output()


# class syntax
class OvenTask(Enum):
    BOIL = "boil"
    FREEZE = "freeze"
    WAIT = "wait"


class MagicalOven:
    def __init__(self):
        self.recipes = [
            {
                "ingredients": ["lead", "mercury"],
                "action": OvenTask.BOIL,
                "output": "gold",
            },
            {
                "ingredients": ["water", "air"],
                "action": OvenTask.FREEZE,
                "output": "snow",
            },
            {
                "ingredients": ["cheese", "dough", "tomato"],
                "action": OvenTask.BOIL,
                "output": "pizza",
            },
        ]
        self.ingredients = []
        self.currentTask = None

    def add(self, item):
        self.ingredients.append(item)

    def freeze(self):
        self.currentTask = OvenTask.FREEZE

    def boil(self):
        self.currentTask = OvenTask.BOIL

    def wait(self):
        self.currentTask = OvenTask.WAIT

    def get_output(self):
        for recipe in self.recipes:
            if (
                recipe["ingredients"] == self.ingredients
                and recipe["action"] == self.currentTask
            ):
                return recipe["output"]
        return None


print(alchemy_combine(make_oven(), ["lead", "mercury"], 5000))
