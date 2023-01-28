from decimal import *


def problem1(number):
    # split the number into 3 parts
    #print(number)
    sign: str = number[0]
    exponent: str = number[1:12]
    mantissa: str = number[12:]
    #print(sign + ' ' + exponent + ' ' + mantissa)

    # reverse the exponent string
    exponent = exponent[::-1]
    #print(exponent)

    # convert the binary number in exponent to a decimal number
    exponent_int: int = 0
    for i in range(0, len(exponent)):
        if exponent[i] == '1':
            exponent_int += 2**i
    #print(exponent_int)

    # subtract 1023 from exponent
    exponent_int -= 1023
    #print(exponent_int)

    # convert mantissa
    #print(mantissa)
    mantissa_int: int = 0
    for j in range(0, len(mantissa)):
        if mantissa[j] == '1':
            mantissa_int += 2**(-(j+1))
    #print(mantissa_int)

    # result
    result: float = (-1)**(int(sign))
    result *= (1 + mantissa_int)
    result *= 2**exponent_int
    #print(result)

    return result


def format_to_5_decimal_places(number):
    # check if number is formatted to 5 decimal places
    # store number as a string
    result_string: str = str(number)

    count: int = 0
    i: int = 0
    # find the length of the string after '.'
    current_char: str = result_string[i]
    while ((current_char != '.') and (i <= len(result_string))):
        i += 1
        current_char = result_string[i]
    count = len(result_string) - (i + 1)

    # if there are more than 5 decimal places, keep only the first 5
    if count > 5:
        result_string = result_string[:-(count-5)]

    return result_string


def three_digit_chopping_arithmetic(number):
    # express number in normalized form
    result_string: str = str(number)

    # find the amount of numbers before '.'
    i: int = 0
    current_char: str = result_string[i]
    while (current_char != '.') and (i <= len(result_string)):
        i += 1
        current_char = result_string[i]
    # divide number by 10, i times (number is in form 0._____ * 10^i)
    number_temp: float = number
    for j in range(0, i):
        number_temp /= 10
    result_string = str(number_temp)
    #print(result_string, "x 10^{}".format(i))

    # keep 3 digits
    # keep first 2 chars (0.) and 3 decimals
    result_string2: str = result_string[:5]
    #print(result_string2, "x 10^{}".format(i))
    # multiply by 10, i times
    number_temp = float(result_string2)
    for k in range(0, i):
        number_temp *= 10
    #print(number_temp)
    result_string2 = str(number_temp)

    return result_string2


def three_digit_rounding_arithmetic(number):
    # express number in normalized form
    result_string: str = str(number)

    # find the amount of numbers before '.'
    i: int = 0
    current_char: str = result_string[i]
    while (current_char != '.') and (i <= len(result_string)):
        i += 1
        current_char = result_string[i]
    # divide number by 10, i times (number is in form 0._____ * 10^i)
    number_temp: float = number
    for j in range(0, i):
        number_temp /= 10
    result_string = str(number_temp)
    #print(result_string, "x 10^{}".format(i))

    # add 5 to 4th digit
    # keep 1st 2 characters (0.) and next 4
    result_string = result_string[:6]
    #print(result_string, "x 10^{}".format(i))
    number_temp = float(result_string)
    #print(number_temp)
    number_temp += 0.0005
    #print(number_temp)
    # multiply by 10, i times
    for k in range(0, i):
        number_temp *= 10
    # print(number_temp)
    result_string = str(number_temp)

    return result_string


def absolute_error(exact, rounded):
    return abs(exact - rounded)


def relative_error(exact, absolute_error_result):
    return (absolute_error_result / abs(exact))


def check_alternating_series(series):
    # if (-1)**k is a term in the function, the series is alternating
    if "(-1)**k" in series:
        return True
    else:
        return False


def check_decreasing(series, x):
    k: int = 1
    term = abs(eval(series))
    for k in range(2, 100):
        # find the value of the function at x with current k
        current_term = abs(eval(series))

        # check if current term is smaller than previous
        if current_term < term:
            term = current_term
        else:
            return False
    return True


def minimum_terms(series, x, error):
    # find the first term less than the error
    k: int = 1
    term = abs(eval(series))
    #print(term)
    while term >= error:
        # the first term with a value less than the error has not been found yet
        # k is 1 for the first term, and increases by 1 for every new term, so it counts the terms
        k += 1
        term = abs(eval(series))
        #print(term)
    return (k - 1)


def bisection_method(function, a, b, accuracy):
    error_tolerance = accuracy
    max_iterations = 100
    i: int = 0
    # start with a and b such that f(a) and f(b) have different signs
    # need x for eval and left/right for while loop
    x = a
    left = a
    f_a = eval(function)
    x = b
    right = b
    f_b = eval(function)
    if ((f_a > 0 and f_b > 0) or (f_a < 0 and f_b < 0)):
        # f(a) and f(b) have the same sign
        print("f(a) and f(b) must have different signs")
        return

    while (abs(right - left) > error_tolerance) and i < max_iterations:
        # find the point midway between a and b, then find the function value at that point
        x = (a + b) / 2
        f_midpoint = eval(function)
        # this new value has the same sign as either f(a) or f(b)
        # next interval uses the new point and previous point with different sign
        if (f_a < 0 and f_midpoint > 0) or (f_a > 0 and f_midpoint < 0):
            # left and midpoint have opposite signs
            # f_a still uses a/left, f_b changes to f_midpoint
            right = x
            b = x
            f_b = f_midpoint
        else:
            # right and midpoint have opposite signs
            left = x
            a = x
            f_a = f_midpoint
        i += 1

    return i


def newton_raphson_method(function, a, tangent, accuracy):
    error_tolerance = accuracy
    max_iterations = 100
    # start with x close to actual root
    # find f(x)
    x = a
    f_x = eval(function)
    # use tangent at f(x) to find next value to try
    f_tangent = eval(tangent)
    i: int = 1
    # iterate until convergence
    while (i <= max_iterations):
        if f_tangent != 0:
            # update x
            old_x = x
            x = old_x - (f_x / f_tangent)
            # update f(x) and f'(x)
            f_x = eval(function)
            f_tangent = eval(tangent)
            if abs(x - old_x) < error_tolerance:
                # return iterations
                return i
            i += 1
        else:
            return i
    return i


if __name__ == "__main__":
    # Use double precision, calculate the resulting values (format to 5 decimal places)
    # a) 010000000111111010111001 000000000000000000000000000000
    number1: str = "010000000111111010111001000000000000000000000000000000"
    # store the number before formatting
    result: float = problem1(number1)

    # format the result to 5 decimal places
    #print(result)
    problem1_result = format_to_5_decimal_places(result)
    print(problem1_result)
    print("")


    # Repeat exercise 1 using three-digit chopping arithmetic
    problem2_result = three_digit_chopping_arithmetic(result)
    print(problem2_result)
    print("")


    # Repeat exercise 1 using three-digit rounding arithmetic
    problem3_result = three_digit_rounding_arithmetic(result)
    print(problem3_result)
    print("")


    # Compute the absolute and relative error with the exact value
    # from question 1 and its 3 digit rounding
    #print(float(problem1_result), "", float(problem3_result))
    problem4_result = absolute_error(float(problem1_result), float(problem3_result))
    print(problem4_result)
    problem4_result2 = relative_error(Decimal(problem1_result), Decimal(problem4_result))
    print(f'{problem4_result2:.31f}')
    print("")


    # Consider the infinite series: f(x) = sum_from_k=1_to_infinity( ( (-1)^k )( (x^k) / (k^3) ) )
    # What is the minimum number of terms needed to compute f(1) with error < 10^-4?
    # check that the function is an alternating series and that the terms are decreasing
    function: str = "((-1)**k) * ((x**k) / (k**3))"
    x: int = 1
    # check alternating
    alternating_check: bool = check_alternating_series(function)
    if alternating_check:
        # check decreasing
        decreasing_check: bool = check_decreasing(function, x)
        if decreasing_check:
            # find minimum number of terms needed to compute f(1) with error < 10^-4
            # 10^-4 = 0.0001
            number_of_terms: int = minimum_terms(function, x, 0.0001)
            print(number_of_terms)
        else:
            print("The series is not decreasing")
    else:
        print("The series is not an alternating series")
    print("")


    # Determine the number of iterations necessary to solve f(x) = x^3 + 4x^2 – 10 = 0
    # with accuracy 10^-4 using a=-4 and b=7.
    # a) Using the bisection method
    # b) Using the newton Raphson method
    function: str = "(x**3) + (4*(x**2)) - 10"
    accuracy = 0.0001
    a: int = -4
    b: int = 7
    iterations = bisection_method(function, a, b, accuracy)
    print(iterations)
    print("")
    tangent: str = "(3*(x**2)) + (8*x)"
    iterations = newton_raphson_method(function, b, tangent, accuracy)
    print(iterations)
    print("")