# Homework 9
# White Python
# 10/25/2023

def quadraticDirection(a):
    if a > 0:
        return "The parabola opens up."
    elif a < 0:
        return "The parabola opens down."
    else:
        return "The function yields a linear line."

def quadraticInterceptFinder(a, b, c):
    d = ((b ** 2) - (4 * a * c))
    x1 = ((-b + d ** 0.5) / (2 * a))
    x2 = ((-b - d ** 0.5) / (2 * a))
    if d > 0:
        return (x1, x2)
    elif d == 0:
        return (x1,)
    else:
        return ()

def quadraticInterceptInterpreter(intercepts):
    if len(intercepts) == 2:
        x1, x2 = intercepts
        print(f"There are exactly 2 x-intercepts: {x1} and {x2}")
    elif len(intercepts) == 1:
        x1 = intercepts[0]
        print(f"There is 1 x-intercept: {x1}")
    else:
        print("There are no x-intercepts.")

def quadraticEvaluator(a, b, c, x):
    F = a * x ** 2 + b * x + c
    return F

def quadraticVertexFinder(a, b, c):
    V = - (b / (2 * a))
    return f"The coordinates for the vertex of the parabola can be found at {V}, {quadraticEvaluator(a, b, c, V)}"

def quadraticFacts(a, b, c):
    print(quadraticDirection(a))
    intercepts = quadraticInterceptFinder(a, b, c)
    quadraticInterceptInterpreter(intercepts)
    print(quadraticVertexFinder(a, b, c))


quadraticFacts(5, 3, 2)
print()
quadraticFacts(-5,0,0)
print()
quadraticFacts(-5,3,2)
