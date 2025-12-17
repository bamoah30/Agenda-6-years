sequence = [0, 1 ]

i = 0

while sequence[-1] < 50:
    next_value = sequence[i] + sequence[i + 1]
    sequence.append(next_value)
    i += 1

print(sequence)

