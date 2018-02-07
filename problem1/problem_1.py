import pytest


def highest_value(nr):
    """
    Return the highest value containing all digits from nr.
    If a chr from nr is not a digit ignore it.
    """
    counter = count_digit_occurence(nr)
    result = compose_highest_value(counter)
    return result


def count_digit_occurence(nr):
    zero_ord = ord('0')
    nine_ord = ord('9')
    counters = [0] * 10
    for letter in nr:
        if zero_ord <= ord(letter) <= nine_ord:
            counters[int(letter)] += 1
    return counters


def compose_highest_value(counters):
    result_list = []
    for i in range(9, -1, -1):
        result_list.append(str(i) * counters[i])
    result = ''.join(result_list)
    if result.startswith('0'):
        result = '0'
    return result


@pytest.mark.parametrize('nr, result', [
    ('', ''),
    ('0000', '0'),
    ('19a', '91'),
    ('5372989', '9987532'),
    ('589043594385845353294832498435', '999988888555555444444333333220'),
    ('893284948325908439284324902385', '999998888885544444333332222200'),
    ('9084325743590328548359048590843232493283249324932840984332483258'
     '9043753687543689547689754675468975654689754543534754375374574932'
     '78473289749783248372487389757435437535943578435984358435890438',
     '9999999999999999999988888888888888888888888888777777777777777777'
     '7777666666655555555555555555555555555544444444444444444444444444'
     '44444444333333333333333333333333333333333222222222222220000000')
])
def test_highest_value(nr, result):
    assert highest_value(nr) == result
