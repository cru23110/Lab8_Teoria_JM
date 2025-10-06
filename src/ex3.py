import pandas as pd
import matplotlib.pyplot as plt
from common import profile_function

"""
Ejercicio 3
Algoritmo:
for (i=1; i<=n/3; i++)
  for (j=1; j<=n; j+=4)
    print("Sequence")
Iteraciones ~ (n/3)*(n/4) => O(n^2)
"""
def ex3_algo(n: int) -> int:
    counter = 0
    outer = n // 3
    for _ in range(outer):
        j = 1
        while j <= n:
            counter += 1  # simulación de 'print' sin I/O
            j += 4
    return counter

def profile_and_save():
    ns = [20, 40, 80, 160, 320, 640, 1280]
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
