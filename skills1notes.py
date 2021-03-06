"""Skills Assessment: Lists

Edit the function bodies until all of the doctests pass when you run this file.
"""


def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []

    """
    all_odd_list = []

    for num in number_list:
        if num % 2 != 0:
            all_odd_list.append(num)

    return all_odd_list

    # ************************************************* #
    # NOTES FROM HB


def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """

    all_even_list = []

    for num in number_list:
        if num % 2 == 0:
            all_even_list.append(num)

    return all_even_list


def print_indexes(my_list):
    """Print the index of each item in the input_list, followed by the item itself.

    Do this without using a counting variable---that is, don't do something
    like this:

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this:

        >>> print_indexes(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

    """
    # FIRST VERSION
    # for item in my_list:
    #     item_index = my_list.index(item)
    #     print "%d %s" % (item_index, item)

    # ************************************************* #
    # NOTES FROM HB
    # How might you solve this problem using range and len?
    # ************************************************* #

    index_list = range(len(my_list))

    for item in index_list:
        print "%d %s" % (item, my_list[item])


def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """
    long_words_list = []

    for word in word_list:
        if len(word) > 4:
            long_words_list.append(word)         
    
    return long_words_list


def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

    DO NOT USE the built-in function `min`!

        >>> smallest_int([-5, 2, -5, 7])
        -5


        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return None:


        >>> smallest_int([]) is None
        True

    """

    # FIRST VERSION
    #
    # if len(number_list) == 0:
    #     return None
    # else:
    #     smallest_int = number_list[0]

    #     for num in number_list:
    #         if num <= smallest_int:
    #             smallest_int = num

    #     return smallest_int

    # ************************************************* #
    # NOTES FROM HB
    # How might you solve this problem without needed the outer if/else?
    # ************************************************* #

    smallest = None

    for num in number_list:
        if num < smallest or smallest == None:
            smallest = num

    return smallest


def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.

    DO NOT USE the built-in function `max`!

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None:

        >>> largest_int([]) is None
        True

    """

    # if len(number_list) == 0:
    #     return None
    # else:
    #     largest_int = number_list[0]
    #     for num in number_list:
    #         if num >= largest_int:
    #             largest_int = num
    #     return largest_int

    # ************************************************* #
    # NOTES FROM HB
    # Same as previous problem
    # ************************************************* #

    largest = None

    for num in number_list:
        if num > largest or largest == None:
            largest = num

    return largest


def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """
    # halvesies_list = []

    # for num in number_list:
    #     if num % 2 == 0:
    #         half_num = float(num / 2)
    #     else:
    #         half_num = float(num / 2) + 0.5

    #     halvesies_list.append(half_num)

    # return halvesies_list

    # ************************************************* #
    # NOTES FROM HB
    # This problem is possible without the if/else or the floats
    # Try to implement a solution like that.
    # ************************************************* #

    # Some tests in Python
    # float(2/2)>>>1.0
    # float(1/2)>>>0.0
    # float(1/2.0)>>>0.5

    halvesies_list = []

    for num in number_list:
        halvesies_list.append(num / 2.0)

    return halvesies_list


def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """

    word_lengths_list = []

    for word in word_list:
        word_length = len(word)
        word_lengths_list.append(word_length)

    return word_lengths_list


def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does this -- but for
    this exercise, you should not use it.

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero:

        >>> sum_numbers([])
        0

    """

    # FIRST VERSION
    #
    # sum_numbers = 0

    # if len(number_list) == 0:
    #     return sum_numbers
    # else:
    #     for num in number_list:
    #         sum_numbers += num

    # return sum_numbers

    # ************************************************* #
    # NOTES FROM HB
    # Can you implement a solution without the if/else?
    # ************************************************* #

    sum_numbers = 0

    for num in number_list:
        sum_numbers += num

    return sum_numbers


def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in the input, the product will be zero:

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product, if the list is
    empty, the product should be 1:

        >>> mult_numbers([])
        1

    """
    # FIRST VERSION

    # mult_numbers = 1

    # if len(number_list) == 0:
    #     return mult_numbers
    # else:
    #     for num in number_list:
    #         mult_numbers *= num

    # return mult_numbers

    # ************************************************* #
    # NOTES FROM HB
    # Can you implement a solution without the if/else?
    # ************************************************* #

    mult_numbers = 1

    for num in number_list:
        mult_numbers *= num

    return mult_numbers


def join_strings(word_list):
    """Return a string of all input strings joined together.

    Python has a built-in method on lists, `join`---but for this exercise, you
    should not use it.

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string:

        >>> join_strings([])
        ''

    """

    # FIRST VERSION
    #
    # join_strings = ""

    # if len(word_list) == 0:
    #     return join_strings
    # else:
    #     for word in word_list:
    #         join_strings += word

    # return join_strings

    # ************************************************* #
    # NOTES FROM HB
    # Is there an available python method that can
    # simplify this solution?
    # Do you need an if/else?
    # ************************************************* #

    join_strings = ""

    for word in word_list:
        join_strings += word

    return join_strings


def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """

    # FIRST VERSION

    # sum_all = 0
    # num_count = 0

    # for num in number_list:
    #     num = float(num)
    #     sum_all += num
    #     num_count += 1

    # average = sum_all / num_count

    # return average

    # ************************************************* #
    # NOTES FROM HB
    # Can you implement a solution without a counter?
    # There's a built in python function that can help
    # ************************************************* #

    average = float(sum_numbers(number_list)) / len(number_list)

    return average


def join_strings_with_comma(list_of_words):
    """Return ['list', 'of', 'words'] like "list, of, words".

        >>> join_strings_with_comma(["Labrador", "Poodle", "French Bulldog"])
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course:

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'

    """

    if len(list_of_words) == 1:
        joint_string = list_of_words[0]
        return joint_string
    else:
        joint_string = ""
        for word in list_of_words:
            if list_of_words.index(word) == 0:
                joint_string = list_of_words[0]
            else:
                joint_string = joint_string + ", " + word

    return joint_string

    # ************************************************* #
    # NOTES FROM HB
    # Do you really need an if/else?
    # Is there a python function that can simplify this code?
    # ************************************************* #


##############################################################################
# END OF ASSIGNMENT: You can ignore everything below.


if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s TESTS PASSED. GOOD WORK!" % result.attempted
    print