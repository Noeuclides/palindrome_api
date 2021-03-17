
def expansionFromCenter(string: str, left: int, right: int) -> int:
    while (left >= 0 and right < len(string)
           ) and string[left] == string[right]:
        left -= 1
        right += 1
    return right - left - 1


def get_sub_palindrome(string: str) -> str:
    start = 0
    end = 0
    for i in range(len(string)):
        odd_limit = expansionFromCenter(string, i, i)
        even_limit = expansionFromCenter(string, i, i + 1)
        limit = max(odd_limit, even_limit)
        if limit > end - start:
            start = i - (limit - 1) // 2
            end = i + limit // 2
        if end == len(string) - 1:
            break

    return string[start:end + 1]
