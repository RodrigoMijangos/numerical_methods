from numerical_methods.bisection_method import bisection
from numerical_methods.secant_method import secant
from numerical_methods.false_position_method import false_position
from utility.util import parse_expression, to_print

results = bisection((3, 3.7), parse_expression('x^3-3x^2-5'), decimals=4, show_decimals=4, error=0)

print("k \t a \t b \t Xi \t f(Xi) \t e \t")
for row in results:
    print(to_print(row))


print("\n\nk \t a \t b \t fa \t fb \t Xi \t f(Xi) \t e \t")
results = secant((0, 1), parse_expression('x^3+2x^2+10x-20'), decimals=5, show_decimals=5, error=0.0000000001)
for row in results:
    print(to_print(row))

print("\n\nk \t a \t b \t fa \t fb \t Xi \t f(Xi) \t e \t")
results = false_position((3, 4), parse_expression('x^3-3x^2-5'), decimals=2, show_decimals=4, error=0.0000000001)
for row in results:
    print(to_print(row))
