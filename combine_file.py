import os
count = 0
sum = 0
# Open the output file in write mode
with open("background_data.txt", 'r') as the_file:
    for line in the_file:
        line = line.strip()
        try:
            sum += int(line)
            count += 1
        except:
            pass

print(sum)
print(count)
print(sum/count)
