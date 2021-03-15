
def get_sub_palindrome(string: str) -> str:
    if string == string[::-1]:
        return string
    window = len(string) - 1
    while window >= 1:
        for i in range(0, len(string) - window + 1):
            sub_s = string[i:window+i]
            if sub_s == sub_s[::-1]:
                return sub_s
        window -= 1
