from collections import deque


def is_palindrome(text: str) -> bool:
    cleaned = "".join(ch.lower() for ch in text if ch != " ")

    dq = deque(cleaned)

    while len(dq) > 1:
        left = dq.popleft()
        right = dq.pop()
        if left != right:
            return False

    return True


if __name__ == "__main__":
    s = input("Введіть рядок для перевірки: ")
    if is_palindrome(s):
        print("Цей рядок є паліндромом.")
    else:
        print("Цей рядок нпе є паліндромом.")
