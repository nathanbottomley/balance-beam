import matplotlib.pyplot as plt
import pandas as pd

JOINT_ACCOUNT_NAME = "Shared Account"

data = pd.read_csv("transactions.csv")

data["Date"] = pd.to_datetime(data["Date"], format="%d/%m/%Y")
data = data.sort_values(by="Date")
data["Amount"] = data.apply(
    lambda x: x["Amount"] / 2 if x["Account"] == JOINT_ACCOUNT_NAME else x["Amount"],
    axis=1,
)
data["Cumulative Amount"] = data["Amount"].cumsum()

# Step 3: Visualize Cumulative Balance Over Time
plt.figure(figsize=(12, 6))
plt.plot(data["Date"], data["Cumulative Amount"], marker="o", linestyle="-")
plt.title("Cumulative Balance Over Time")
plt.xlabel("Date")
plt.ylabel("Cumulative Amount")
plt.grid(True)
plt.tight_layout()
plt.show()
