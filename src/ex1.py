import pandas as pd
import matplotlib.pyplot as plt
from common import profile_function

"""
Ejercicio 1
Algoritmo:
for (i = n/2; i <= n; i++)
  for (j = 1; j + n/2 <= n; j++)
    for (k = 1; k <= n; k = k*2)
      counter++
Complejidad teórica esperada: O(n^2 log n)
"""
def ex1_algo(n: int) -> int:
    counter = 0
    i_start = n // 2
    for i in range(i_start, n + 1):
        j = 1
        j_limit = n - (n // 2)
        while j <= j_limit:
            k = 1
            while k <= n and n > 0:
                counter += 1
                k *= 2
            j += 1
    return counter

def profile_and_save():
    ns = [10, 50, 100, 200, 500, 1000, 2000]
    data = profile_function(ex1_algo, ns)
    df = pd.DataFrame(data, columns=["n", "seconds"])
    df.to_csv("results/ex1/times_ex1.csv", index=False)
    plt.figure()
    plt.plot(df["n"], df["seconds"], marker="o")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("n (log)")
    plt.ylabel("tiempo (s, log)")
    plt.title("Ejercicio 1: n vs tiempo")
    plt.grid(True, which="both", ls="--", linewidth=0.5)
    plt.savefig("results/ex1/plot_ex1.png", dpi=200)
    plt.close()

if __name__ == "__main__":
    profile_and_save()
