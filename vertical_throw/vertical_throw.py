import matplotlib.pyplot as plt
import numpy as np


# Defining function to load data.
def read_datas():
    def float_input(user_info, user_prompt, min_value):
        print("---[ LOADING DATA....]------------------")
        print(user_info)
        user_input = input(user_prompt)
        if user_input.count(".") > 1:
            return None
        if not user_input.replace(".", "").isdecimal():
            return None
        # converting user_input into float.
        user_value = float(user_input)
        if user_value < min_value:
            print(f"Value {user_value} is lower then predicted {min_value}.")
            return None
        # returns user_value if is correct.
        return user_value

    # defining required variables.
    h_start = None
    v_start = None
    h_min = 10  # Minimal height
    v_min = 2  # Minimal speed

    while h_start is None:
        h_start = float_input(
            "Not corrected value for h_start. Type float (E.g. 3.14)",
            "Input starting height (in m, min. 10): ",
            h_min
        )
    while v_start is None:
        v_start = float_input(
            "Not corrected value for v_start. Type float (E.g. 3.14)",
            "Input starting speed (in m/s, min. 2): ",
            v_min
        )
    return h_start, v_start


initial_values = None
while initial_values is None:
    print("Please, input values needed to generate graph.")
    initial_values = read_datas()

print("We have it! Data is read, we can continue.")
H_START, V_START = initial_values
# Calculating the most important values.
g = 9.81  # m/s^2
total_time = ((2 * H_START) / g) ** (1 / 2)
max_range = V_START * total_time
# Calculating successive values Y for X every 1/100 of total_range.
x_points = np.arange(0, max_range, max_range / 100)
y_points = H_START - ((g / 2) * (x_points / V_START) ** 2)
# Adding graph with start and end place.
title = f"""Graph of vertical throw with V_START = {V_START} m/s (g = {g} m/s^2)
            Fly time = {round(total_time, 4)} s"""
# Graph setups
plt.scatter(0, H_START, label=f"H_START={H_START} m")
plt.scatter(max_range, 0, label=f"max_range={round(max_range, 3)} m")
plt.plot(x_points, y_points, marker="+", color="red", label="Next points in distance.")
plt.grid()
plt.title(title)
plt.xlabel("Distance in meters")
plt.ylabel("Height in meters")
plt.legend()
plt.show()
