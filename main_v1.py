name = str(input("City name: ")).lower()
f = open("tribe_city_names.txt", "r")
lines = f.readlines()
f.close()
replacements = lines[-1][13:].split(",")
for i in range(len(replacements)):
	replacements[i] = replacements[i].split(";")lines = lines[:-1]
def replace_accents(name):
	for replac in replacements:
		if replac[0] in name:
			name = name.replace(replac[0], replac[1])
			return True, name
	return False, name
replacing = True
while replacing == True:
	replacing, name = replace_accents(name)
for i in range(len(lines)):
	if lines[i] == "Special Characters\n":
		spec_char = lines[i+1:]
		for j in range(len(spec_char)):
			spec_char[j] = spec_char[j].split(",")
			spec_char[j][-1] = spec_char[j][-1].strip("\n")
		lines = lines[:i]
		break
scores = {}
lines2 = []
for line in lines:
	lines2.append(line.split(","))
	lines2[-1][-1] = lines2[-1][-1].strip("/n")
for line in lines2:
	score = 0
	line2 = line[1:]
	temp_name = name
	for syllable in line2:
		if syllable in temp_name:
			score += 1
	scores[line[0]] = score
for i in spec_char:
	for j in i[1:]:
		if j in name:
			scores[i[0]] += 99
best_score = 0
best_tribes = []
for tribe in scores:
	if scores[tribe] > best_score:
		best_score = scores[tribe]
		best_tribes = [tribe]
	elif scores[tribe] == best_score:
		best_tribes.append(tribe)
print(best_tribes)
