def rim_to_int(s):
    rim = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0

    for i in range(len(s)):
        if i < len(s) - 1 and rim[s[i]] < rim[s[i + 1]]:
            total -= rim[s[i]]
        else:
            total += rim[s[i]]

    return total

s = "MCMXCI"
print(rim_to_int(s))