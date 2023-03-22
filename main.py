from numerical_methods.bisection_method import bisection
from utility.util import parse_expression

results = bisection((3, 3.7), parse_expression('x^3-3x^2-5'), decimals=3, show_decimals=4)

print("k \t a \t b \t Xi \t f(Xi) \t e \t")
for row in results:
    print(f"{row.k} \t {row.a} \t {row.b} \t {row.ik} \t {row.f_eval} \t {row.ep}")
