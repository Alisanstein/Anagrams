def is_anagram(s1,s2):
    lis1 = sorted(s1)
    lis2 = sorted(s2)

    if lis1 == lis2 :
        return True

    else:
        return False