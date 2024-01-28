#!/usr/bin/python3
"""custom_functions.py"""


def factorize(product):
    """Print the factors of the given product.

        Parameters:
            - product (int): The number for which factors need to be printed.

        Returns:
            - bool: Always returns True.
    """
    for right_factor in range(2, product + 1):
        if product % right_factor == 0:
            left_factor = product // right_factor
            print(f"{product}={left_factor}*{right_factor}")
            break
    return True
