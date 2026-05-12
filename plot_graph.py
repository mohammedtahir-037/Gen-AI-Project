import matplotlib.pyplot as plt
import re

loss_values = []

# Read log file
with open("training_log.txt", "r") as f:
    for line in f:
        match = re.search(r"Loss:\s([0-9.]+)", line)
        if match:
            loss_values.append(float(match.group(1)))

# Plot
plt.plot(loss_values)
plt.xlabel("Steps")
plt.ylabel("Loss")
plt.title("Training Loss Graph")

plt.savefig("loss_graph.png")
plt.show()
