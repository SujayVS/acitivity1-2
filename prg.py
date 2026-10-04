import operator
import random

def generate_arithmetic_problem():
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv
    }
    
    op_symbol = random.choice(list(operations.keys()))
    
    if op_symbol == '/':
        # Avoid division by zero and ensure clean integer division
        b = random.randint(1, 12)
        answer = random.randint(1, 12)
        a = b * answer
    elif op_symbol == '*':
        a = random.randint(1, 12)
        b = random.randint(1, 12)
        answer = operations[op_symbol](a, b)
    else:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        answer = operations[op_symbol](a, b)

    user_input = input(f"Solve: {a} {op_symbol} {b} = ")
    
    try:
        if int(user_input) == answer:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer was {answer}.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    generate_arithmetic_problem()