"""
Ejercicio 3
Algoritmo:
for (i=1; i<=n/3; i++)
  for (j=1; j<=n; j+=4)
    print("Sequence")
Iteraciones ~ (n/3)*(n/4) => O(n^2)
"""

from common import profile_function
import pandas as pd
import matplotlib.pyplot as plt

def ex3_algo(n: int) -> int:
    counter = 0
    outer = n // 3
    j_steps = (n + 3) // 4  # ceil(n/4) sin float
    for _ in range(outer):
        # no imprimimos, solo contamos para no pagar IO
        counter += j_steps
    return counter

def profile_and_save():
    ns = [1, 10, 100, 1000, 10_000, 100_000, 1_000_000]
    data = profile_function(ex3_algo, ns)
    df = pd.DataFrame(data, columns=["n", "seconds"])
    df.to_csv("results/ex3/times_ex3.csv", index=False)

    plt.figure()
    plt.plot(df["n"], df["seconds"], marker="o")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("n (log)")
    plt.ylabel("tiempo (s, log)")
    plt.title("Ejercicio 3: n vs tiempo")
    plt.grid(True, which="both", ls="--", linewidth=0.5)
    plt.savefig("results/ex3/plot_ex3.png", dpi=200)
    plt.close()

if __name__ == "__main__":
    profile_and_save()
