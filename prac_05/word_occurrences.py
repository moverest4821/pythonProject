word_count = {}
text = input("Text: ")
rows = text.split()
for row in rows:
    frequency = word_count.get(row, 0)
    word_count[row] = frequency +1

rows = list(word_count.keys())
rows.sort()

max_length = max(len(row)for row in rows)
for row in rows:
    print("{:{}} : {}".format(row, max_length, word_count[row]))