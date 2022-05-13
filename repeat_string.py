def repeated_string(s, n):
    rest = n % len(s)
    in_s = n // len(s)
    a = s.count('a')
    b = s[:rest]
    result = a * in_s + b.count('a')
    return result
