def out(pattern, s):
    pat = {}
    for i in pattern:
        if i not in pat:
            pat[i] = 1
        else:
            pat[i] += 1
    hash = {i:0 for i in pattern}
    count = left = 0
    for right in range(len(s)):
        if s[right] in hash:
            hash[s[right]] += 1
            count += 1
            if hash[s[right]] > 1:
                hash[s[right]] -= 1
                count = sum(hash.values())
        elif sum(hash.values()) >= 1:
            count += 1
        if hash == pat and len(pat) == count:
            print(hash, s[:right], count)
            return True
        print(hash, s[:right], count)
    return False

if __name__ == "__main__":
    print(out("ab", "eidbaooo") == True)
    print(out("ab", "eidboaoo") == False)
    print(out("a", "ab") == True)
    print(out("adc", "dcda") == True)
    print(out("ky", "ainwkckifykxlribaypk") == True)
    print(out("hello", "ooolleoooleh") == False)
    print(out("abc", "ccccbbbbaaaa") == False)