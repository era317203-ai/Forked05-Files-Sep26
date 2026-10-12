old = open(r"Task 1\old.txt", "r")
new = open(r"Task 1\new.txt", "r")
# list_old [] = old
old_lines = [line.rstrip("\n") for line in old]
new_lines = [line.rstrip("\n") for line in new]
old.close
new.close
print(old_lines)
diff = open (r"Task 1\diff.txt", "w")
old_index = 0
new_index = 0
while old_index < len(old_lines) and new_index < len(new_lines):
    if old_lines[old_index] == new_lines[new_index]:
        diff.write(old_lines[old_index] + "\n")
        old_index +=1
        new_index +=1
    elif old_lines[old_index] not in new_lines:
        diff.write("-" + old_lines[old_index] + "\n")
        old_index +=1
    else:
        diff.write("+" + new_lines[new_index] + "\n")
        new_index +=1
diff.close
