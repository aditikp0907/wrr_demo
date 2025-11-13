import matplotlib.pyplot as plt
import time
from wrr import WRR

lb = WRR()
counts = {"w1": 0, "w2": 0, "w3": 0}

plt.ion()
fig, ax = plt.subplots()

while True:
    worker = lb.next()
    counts[worker] += 1

    ax.clear()
    ax.bar(counts.keys(), counts.values())
    ax.set_ylabel("Requests")
    ax.set_title("Weighted Round Robin Load Balancing")
    plt.pause(0.5)

    time.sleep(1)
