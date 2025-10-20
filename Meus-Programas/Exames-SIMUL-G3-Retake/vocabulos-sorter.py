def cap_keep_spaces(s):
    for i, ch in enumerate(s):
        if ch.isalpha():
            return s[:i] + ch.upper() + s[i+1:].lower()
    return s

with open("vocabulos-unsorted.txt", "r", encoding="utf-8") as f:
    linhas = [cap_keep_spaces(l.rstrip("\n")) for l in f if l.strip()]

with open("vocabulos-sorted.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(sorted(linhas)) + "\n")