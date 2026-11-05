"""Видача решти жадібним алгоритмом і динамічним програмуванням."""

COINS = (50, 25, 10, 5, 2, 1)


def find_coins_greedy(amount: int) -> dict[int, int]:
    """Видає решту, починаючи з найбільшого номіналу."""
    if not isinstance(amount, int) or amount < 0:
        raise ValueError("Сума має бути невід’ємним цілим числом")

    change = {}
    remaining = amount
    for coin in COINS:
        count, remaining = divmod(remaining, coin)
        if count:
            change[coin] = count
        if remaining == 0:
            break
    return change


def find_min_coins(amount: int) -> dict[int, int]:
    """Видає решту за допомогою мінімальної кількості монет."""
    if not isinstance(amount, int) or amount < 0:
        raise ValueError("Сума має бути невід’ємним цілим числом")

    # Монета номіналом 1 гарантує, що достатньо щонайбільше amount монет.
    min_counts = [0] + [amount + 1] * amount
    last_coins = [0] * (amount + 1)

    for subtotal in range(1, amount + 1):
        for coin in COINS:
            if coin <= subtotal:
                count = min_counts[subtotal - coin] + 1
                if count < min_counts[subtotal]:
                    min_counts[subtotal] = count
                    last_coins[subtotal] = coin

    change = {}
    remaining = amount
    while remaining > 0:
        coin = last_coins[remaining]
        change[coin] = change.get(coin, 0) + 1
        remaining -= coin
    return change


if __name__ == "__main__":
    for amount in (113, 10_113, 100_113):
        print(f"Сума — {amount}")
        greedy_change = find_coins_greedy(amount)
        optimal_change = find_min_coins(amount)
        print(f"  Жадібний алгоритм — {greedy_change} ({sum(greedy_change.values())} монет)")
        print(f"  Динамічне програмування — {optimal_change} ({sum(optimal_change.values())} монет)")
