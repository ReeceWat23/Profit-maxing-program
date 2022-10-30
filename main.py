import pulp as p
# from matplotlib import pyplot as plt


# problem variable(s):
def get_lpvar(prod):
    x = p.LpVariable(prod, lowBound=0)
    return x


def prompt_prod():
    # prompt user for product
    user_product = input("What product are you selling?:")
    return user_product


def get_constraint():
    num = int(input("What is your constraint/ next constraint:"))
    return num


def get_limit():
    lim = int(input("what is the limit on this resource/ variable:"))
    return lim


def get_objective():
    # Objective can mean profit in some examples
    obj = int(input("What is the objective/profit for this item:"))
    return obj


def get_point(cons, limit):
    h = cons / limit
    return h


def solve_problem():
    Lp_prob = p.LpProblem("Maximize_profits", p.LpMaximize)

    # Get the lp variables for the problem
    a = get_lpvar(prompt_prod())
    b = get_lpvar(prompt_prod())

    # Get the limitations and constraints for each item with that resource
    print("first limit")
    lim1 = get_limit()
    print("constriants for this limit")
    con1a = get_constraint()
    con1b = get_constraint()

    # Get the limitations and constraints for each item with that resource
    print("2nd limit")
    lim2 = get_limit()
    print("constriants for this limit")
    con2a = get_constraint()
    con2b = get_constraint()

    print("Please input a number for each objective prompt")
    # create object function (what we want to maximize)
    Lp_prob += get_objective() * a + get_objective() * b

    # Constraints
    # Man hours
    print("Constraint 1")
    Lp_prob += con1a * a + con1b * b <= lim1
    # Number of people(employees) it takes to close this deal
    print("Constraint 2:")
    Lp_prob += con2a * a + con2b * b <= lim2

    # Solve the problem
    status = Lp_prob.solve()
    print(p.LpStatus[status])
    value = p.value(Lp_prob.objective)
    print(p.value(Lp_prob.objective))
    print("Product1:",a," ",  round(p.value(a)))
    print("Product2:",b," ", round(p.value(b)))


# Run program
solve_problem()

# think about how we can optimize a trade