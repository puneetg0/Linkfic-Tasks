"""Beginner-friendly solutions for the Day 14 coding exercises."""

from dataclasses import dataclass


@dataclass
class Node:
    value: int
    next: "Node | None" = None


def merge_sorted_lists(first: Node | None, second: Node | None) -> Node | None:
    """Merge two sorted linked lists by reusing their nodes."""
    placeholder = Node(0)
    tail = placeholder

    while first is not None and second is not None:
        if first.value <= second.value:
            tail.next = first
            first = first.next
        else:
            tail.next = second
            second = second.next
        tail = tail.next

    tail.next = first if first is not None else second
    return placeholder.next


def best_time_to_buy_and_sell(prices: list[int]) -> int:
    """Return the best one-time profit, or zero when prices only fall."""
    if len(prices) < 2:
        return 0

    lowest_price = prices[0]
    best_profit = 0

    for price in prices[1:]:
        best_profit = max(best_profit, price - lowest_price)
        lowest_price = min(lowest_price, price)

    return best_profit


def print_list(head: Node | None) -> None:
    values = []
    while head is not None:
        values.append(str(head.value))
        head = head.next
    print(" -> ".join(values) if values else "(empty)")


if __name__ == "__main__":
    left = Node(1, Node(3, Node(5)))
    right = Node(2, Node(4, Node(6)))
    print("Merged linked list:")
    print_list(merge_sorted_lists(left, right))

    print("Best stock profit:", best_time_to_buy_and_sell([7, 1, 5, 3, 6, 4]))
