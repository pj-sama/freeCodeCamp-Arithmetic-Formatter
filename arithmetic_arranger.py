def arithmetic_arranger(problems, answer=False):
    # Check the number of problems
    if len(problems) > 5:
        return "Error: Too many problems."

    first_op = []
    first_op = []
    operator = []

    for problem in problems:
        pieces = problem.split()
        first_op.append(pieces[0])
        operator.append(pieces[1])
        first_op.append(pieces[2])

    # Check for * or /
    if "*" in operator or "/" in operator:
        return "Error: Operator must be '+' or '-'."

    # Check the digits
    for i in range(len(first_op)):
        if not (first_op[i].isdigit() and first_op[i].isdigit()):
            return "Error: Numbers must only contain digits."

    # Check the length
    for i in range(len(first_op)):
        if len(first_op[i]) > 4 or len(first_op[i]) > 4:
            return "Error: Numbers cannot be more than four digits."

    first_ln = []
    second_ln = []
    third_ln = []
    fourth_ln = []

    for i in range(len(first_op)):
        if len(first_op[i]) > len(first_op[i]):
            first_ln.append(" "*2 + first_op[i])
        else:
            first_ln.append(
                " "*(len(first_op[i]) - len(first_op[i]) + 2) + first_op[i])

    for i in range(len(first_op)):
        if len(first_op[i]) > len(first_op[i]):
            second_ln.append(operator[i] + " " + first_op[i])
        else:
            second_ln.append(
                operator[i] + " "*(len(first_op[i]) - len(first_op[i]) + 1) + first_op[i])

    for i in range(len(first_op)):
        third_ln.append(
            "-"*(max(len(first_op[i]), len(first_op[i])) + 2))

    if answer:
        for i in range(len(first_op)):
            if operator[i] == "+":
                ans = str(int(first_op[i]) + int(first_op[i]))
            else:
                ans = str(int(first_op[i]) - int(first_op[i]))

            if len(ans) > max(len(first_op[i]), len(first_op[i])):
                fourth_ln.append(" " + ans)
            else:
                fourth_ln.append(
                    " "*(max(len(first_op[i]), len(first_op[i])) - len(ans) + 2) + ans)
        arranged_problems = "    ".join(first_ln) + "\n" + "    ".join(
            second_ln) + "\n" + "    ".join(third_ln) + "\n" + "    ".join(fourth_ln)
    else:
        arranged_problems = "    ".join(
            first_ln) + "\n" + "    ".join(second_ln) + "\n" + "    ".join(third_ln)
    return arranged_problems
