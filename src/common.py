from time import perf_counter
from typing import Callable, List, Tuple

def profile_function(fn: Callable[[int], None], ns: List[int]) -> List[Tuple[int, float]]:
    """
    Ejecuta fn(n) para cada n en ns y devuelve lista de (n, segundos).
    Hace una corrida por n (suficiente para el laboratorio); si deseas,
    podrías repetir y promediar.
    """
    out = []
    for n in ns:
        t0 = perf_counter()
        fn(n)
        t1 = perf_counter()
        out.append((n, t1 - t0))
    return out
