"""Обчислення визначеного інтеграла методом Монте-Карло."""

from collections.abc import Callable
from random import Random


def monte_carlo_integral(
    function: Callable[[float], float],
    a: float,
    b: float,
    y_max: float,
    samples: int,
    *,
    seed: int | None = None,
) -> float:
    """Оцінює інтеграл на [a, b] для функції зі значеннями від 0 до y_max."""
    if not a < b or not y_max > 0:
        raise ValueError("Прямокутник має мати додатну ширину й висоту")
    if not isinstance(samples, int) or samples <= 0:
        raise ValueError("Кількість точок має бути додатним цілим числом")

    rng = Random(seed)
    hits = 0
    for _ in range(samples):
        x = rng.uniform(a, b)
        y = rng.uniform(0, y_max)
        if y < function(x):
            hits += 1

    rectangle_area = (b - a) * y_max
    return rectangle_area * (hits / samples)


def f(x: float) -> float:
    return x**2


if __name__ == "__main__":
    a, b = 0, 2
    exact = (b**3 - a**3) / 3
    print(f"Аналітичне значення — {exact:.8f}\n")
    print("| Кількість точок | Оцінка Монте-Карло | Абсолютна похибка |")
    print("|---:|---:|---:|")
    for samples in (1_000, 10_000, 100_000, 1_000_000):
        estimate = monte_carlo_integral(f, a, b, f(b), samples, seed=42)
        error = abs(estimate - exact)
        print(f"| {samples} | {estimate:.8f} | {error:.8f} |")
