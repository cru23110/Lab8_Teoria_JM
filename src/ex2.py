import pandas as pd
import matplotlib.pyplot as plt
from common import profile_function

"""
Ejercicio 2
Algoritmo:
if (n <= 1) return
for i in 1..n:
  for j in 1..n:
    print("Sequence"); break
El break hace que el interno ejecute 1 vez por i => O(n)
"""
def ex2_algo(n: int) -> int:
    if n <= 1:
        return 0
    counter = 0
    for i in range(1, n + 1):
        counter += 1
    return counter

def profile_and_save():
    ns = [10, 100, 1_000, 10_000, 100_000, 1_000_000]
    data = profile_function(ex2_algo, ns)
    df = pd.DataFrame(data, columns=["n", "seconds"])
    df.to_csv("results/ex2/times_ex2.csv", index=False)

    plt.figure()
    plt.plot(df["n"], df["seconds"], marker="o")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("n (log)")
    plt.ylabel("tiempo (s, log)")
    plt.title("Ejercicio 2: n vs tiempo")
    plt.grid(True, which="both", ls="--", linewidth=0.5)
    plt.savefig("results/ex2/plot_ex2.png", dpi=200)
    plt.close()

if __name__ == "__main__":
    profile_and_save()
