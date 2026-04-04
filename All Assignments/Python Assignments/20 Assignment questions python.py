# BEGINNER LEVEL: STRINGS FUNDAMENTALS

# 1. Length of a String
s = input("Enter a string: ")
print("Length of string:", len(s))





# 2. Uppercase & Lowercase
s = input("Enter a string: ")
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())





# 3. Count a Character
s = input("Enter a string: ")
ch = input("Enter a character to count: ")
print(f"Character '{ch}' appears:", s.count(ch), "times")





# 4. First & Last Character
s = input("Enter a string: ")
if not s:
    print("Empty string!")
else:
    print("First character:", s[0])
    print("Last character:", s[-1])





# 5. Check Substring Presence
s = input("Enter main string: ")
sub = input("Enter substring to check: ")
print("Substring present?", sub in s)






# 6. Slice a String
s = input("Enter a string: ")
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))
print("Sliced string:", s[start:end])






# 7. Reverse a String
s = input("Enter a string: ")
print("Reversed string:", s[::-1])






# 8. Replace Substring
s = input("Enter a string: ")
old = input("Enter word to replace: ")
new = input("Enter new word: ")
print("Updated string:", s.replace(old, new))





# 9. Split and Join
s = input("Enter a sentence: ")
words = s.split()
joined = "-".join(words)
print("Split & Joined:", joined)





# 10. Strip Whitespace
s = input("Enter a string with spaces: ")
print("Stripped string:", s.strip())






# INTERMEDIATE LEVEL: STRING TASKS

# 1. Count Vowels & Consonants
s = input("Enter a string: ")
vowels = consonants = 0
for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
print("Vowels:", vowels, "Consonants:", consonants)





# 2. Palindrome Check (Ignore case & non-alphanumerics)
s = input("Enter a string: ")
normalized = ''.join(ch.lower() for ch in s if ch.isalnum())
is_palindrome = normalized == normalized[::-1]
print("Is palindrome:", is_palindrome)





# 3. Title Case (Manual)
s = input("Enter a sentence: ")
words = s.split()
title_case = ' '.join(word[0].upper() + word[1:].lower() if word else '' for word in words)
print("Title case:", title_case)





# 4. Find All Indices of a Substring (Allow Overlaps)
s = input("Enter main string: ")
sub = input("Enter substring to find: ")
indices = [i for i in range(len(s)-len(sub)+1) if s[i:i+len(sub)] == sub]
print("Substring indices:", indices)





# 5. Character Frequency Dictionary (case-insensitive, skip spaces)
s = input("Enter a string: ")
freq = {}
for ch in s.lower():
    if ch != ' ':
        freq[ch] = freq.get(ch,0)+1
print("Character frequency dict:", freq)




# 6. Anagram Checker (ignore spaces, punctuation, case)
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
clean1 = sorted(ch.lower() for ch in s1 if ch.isalpha())
clean2 = sorted(ch.lower() for ch in s2 if ch.isalpha())
print("Are anagrams:", clean1 == clean2)





# 7. Compress Repeated Characters (RLE-lite)
s = input("Enter a string: ")
if s:
    result = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result += s[i-1] + str(count)
            count = 1
    result += s[-1] + str(count)
else:
    result = ""
print("Compressed string:", result)






# 8. Longest Word in a Sentence
s = input("Enter a sentence: ")
tokens = s.split()
longest = ""
for token in tokens:
    word = ''.join(ch for ch in token if ch.isalpha())
    if len(word) > len(longest):
        longest = word
print("Longest word:", longest)





# 9. Remove Duplicate Characters but Keep Order
s = input("Enter a string: ")
seen = set()
res = ''
for ch in s:
    if ch not in seen:
        res += ch
        seen.add(ch)
print("String after removing duplicates:", res)






# 10. Mask Email Username
email = input("Enter email: ")
if '@' in email:
    username, domain = email.split('@',1)
    if len(username) > 2:
        masked = username[0] + '*'*(len(username)-2) + username[-1]
    else:
        masked = username
    masked_email = masked + '@' + domain
    print("Masked email:", masked_email)
else:
    print("Invalid email format")