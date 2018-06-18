words = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
short_num = [1, 5, 6, 7, 8, 9, 15, 16, 19]

words = words.replace('.', '').split(" ")
ans = {}
for i in range(len(words)):
    if i in short_num:
        ans[i + 1] = words[i][:1]
    else:
        ans[i + 1] = words[i][:2]
print(ans)
