# declare and fill out function here
def youngest_student2(dict):
	youngest = 999
	yname = "Ryan"
	for x, y in dict.items():
		if (y < youngest):
			youngest = y
			yname = x
	return yname

# test case
students = {"Drake": 21, "Alice": 18, "Bob": 20, "Charlie": 19, "David": 22, "Jay": 20}
print(youngest_student2(students))  # Expected output: "Alice"
