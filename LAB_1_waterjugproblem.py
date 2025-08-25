# Variable declaration for initial amounts in jugs
jug_a = 0
jug_b = 0

# Variable declaration for capacities of the jugs
jug_a_capacity = 7
jug_b_capacity = 4

# Variable declaration for the target value to achieve
target_value = 3

# List to track each step taken during the process
steps = []

# Loop until either jug_a or jug_b contains the target value
while jug_a != target_value and jug_b != target_value:
    
    # If Jug B is empty, fill it to its full capacity
    if jug_b == 0:
        jug_b = jug_b_capacity
        steps.append("Fill Jug B")
    
    # Else if Jug A is not full, pour water from Jug B to Jug A
    elif jug_a < jug_a_capacity:
        # Calculate how much water can be poured without overflowing Jug A
        pour_amount = min(jug_b, jug_a_capacity - jug_a)
        jug_a += pour_amount  # Add poured water to Jug A
        jug_b -= pour_amount  # Subtract poured water from Jug B
        steps.append(f"Pour {pour_amount} from Jug B to Jug A")
    
    # If Jug A is full, empty it completely
    else:
        jug_a = 0
        steps.append("Empty Jug A")

# After exiting the loop, record the final state as success
steps.append(f"Success: Jug A = {jug_a}, Jug B = {jug_b}")

# Output all the steps taken to reach the target
for step in steps:
    print(step)