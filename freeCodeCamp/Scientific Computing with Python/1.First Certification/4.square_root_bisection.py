# square_root_bisection
# In this project, you will find the approximate square root of a given
# number using the bisection method.

# The bisection method is a technique for finding the roots of a real-
# valued function. It works by narrowing down an interval where the 
# square root lies until it converges to a value within a specified tolerance.

# square_target: The number for which you want to find the square root.
# tolerance (optional): The acceptable difference between the square of the approximate root value and the actual target value (default is 1e-7)
# max_iterations (optional): The maximum number of iterations to perform (default is 100).

def square_root_bisection(square_target, tolerance = 1e-7, max_iterations = 100):
    if square_target < 0:
        # The raise statement allows you to force a specific exception to occur. 
        # It consists of the raise keyword followed by the exception type, and enables you to provide a custom error message
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')
    else:
        low = 0
        high = max(1, square_target)
        root = None
        # The _ acts as a placeholder and is useful when you need to use a variable but don't actually need its value.
        # For loop doesn't assing any value to root after passing the max_iterations
        for _ in range(max_iterations):                                        
            mid = (low + high) / 2
            square_mid = mid**2
            if abs(square_mid - square_target) < tolerance:
                root = mid
                break
            elif square_mid < square_target:
                low = mid
            else:
                high = mid
    # In Python, the is keyword checks for object identity. It's used to determine if two variables point to the same object in memory.
    # In contrast to is, the equality operator (==) determines if the values of two objects are the same, regardless of whether they are the same object in memory.
        if root is None:
            print(f'Failed to converge within {max_iterations} iterations.')
        else:   
            print(f'The square root of {square_target} is approximately {root}')
    return root

N = -2

square_root_bisection(N)
