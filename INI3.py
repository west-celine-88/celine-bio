# Rosalind challenge "Strings and Lists"
# Given: A string s of length at most 200 letters and four integers a, b, c and d.
# Return: The slice of this string from indices a through b and c through d (with space in between), inclusively.
# In other words, we should include elements s[b] and s[d] in our slice.

# Download dataset and set equal to variable string
string = "kyz2QcBCcbkLACSH4TQx1d6Gyce1aai6BttCorvussHeAJhJFRqEF0VlmnBUsVtx11DZ9OpgE4h8SOy2sF3zrt8XmEWhiyZxUzpjFXiapxBIQ5HSpQTNypurpurascensWLAJgrGnDaxwOoRUoIveCiMfKYWg2sEGJbI."

# Input indices
a = 35
b = 40 + 1
c = 117
d = 128 + 1

slice = str(string[a:b] + ' ' + string[c:d])
print(slice)
