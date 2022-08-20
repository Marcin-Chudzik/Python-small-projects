""" WARNING! BEFORE YOU START IT!
PROGRAM IS CREATING A LOT OF NEW FILES AND IT'S TAKING SOME TIME.
PLEASE, BE AWARE OF IT."""
import sys

try:
    import matplotlib.pyplot as plt
except:
    if sys.platform == "linux":
        print("For linux (Debian/Ubuntu/Mint):")
        print("sudo apt install python3-pip")
        print("sudo -H pip3 install matplotlib")
    else:
        print("For Windows:")
        print("pip install matplotlib")
        print("pip install msvc-runtime")
    sys.exit(__status=2)

# Standard modules
import os
import pickle
import json
from random import random, randint, seed
from datetime import datetime
from math import sin, cos


# Helpfully functions
def data_saving(data, file_name="data/data_file.dat"):
    with open(file_name, "wb") as p:
        pickle.dump(data, p)


def read_test_data(file="data/data_file.dat"):
    if not os.path.isfile(file):
        return None

    with open(file, "rb") as p:
        data = pickle.load(p)
    return data


def calculate(lst, fun):
    out = []

    for x in lst:
        value = eval(fun)
        out.append(value)
    return out


def save_json(data, file_name="data/data_file.dat"):
    with open(file_name, "w") as outfile:
        json.dump(data, outfile)


def graph_description(data_x, data_y, file_name="graph.png", graph_name="Standard graph"):
    plt.figure(figsize=(40, 20), dpi=30)
    plt.scatter(data_x, data_y)
    plt.xlabel("data_x")
    plt.ylabel("data_y")
    plt.title(file_name)
    plt.grid()
    plt.tight_layout()
    plt.savefig(file_name)
    plt.close("all")


# Setting a constant seed for random number generator to generate every time this same numbers.
seed(84376529347523)
start_time = datetime.now()

# Start
scores = {"Application": "Testing program", "Author": "Marcin Chudzik",
          "sys.version": f"{sys.version} | hexversion {sys.hexversion} | api {sys.api_version}",
          "sys.version_info": str(sys.version_info), "os.uname": "", "Start": str(start_time), "Stop": None,
          "Delta_time": None, "Time in every 1000 enumerates": {}}

if sys.platform == "linux":
    scores["os.uname"] = str(os.uname())

print("Test start:")
for score in scores:
    print(f"{score}: {scores[score]}")
print("-" * 40)
# 200 basics points
data_x = [x for x in range(-100, 100)]
data_saving(data_x, "data/entering_data.dat")

for i in range(1, 10000):
    # Reading basic data
    data_x = read_test_data("data/entering_data.dat")
    if i % 1000 == 0:
        time_now = datetime.now() - start_time
        scores["Time in every 1000 enumerates"][i] = str(time_now)
        print(f"Calculating 1000: {i}")

    if i % 2 == 0:
        fun = str(f"sin({randint(1, 10)}*x*x+{random() * i}*x-{i ** randint(1, 4)})")
        data_y = calculate(data_x, fun)
    else:
        fun = str(f"cos({randint(1, i)}*x*x*(-1)+{randint(1, i)}*x+{i})")
        data_y = calculate(data_x, fun)

    data_saving(data_y, f"data/Entering data{i}.dat")
    graph_description(data_x, data_y, f"Graph{i}.png")

stop_time = datetime.now()
scores["Stop"] = str(stop_time)
scores["Delta_time"] = str(stop_time - start_time)
save_json(scores)
