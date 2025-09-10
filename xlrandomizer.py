import pandas as pd
import os

if not os.path.exists('Output'):
	os.mkdir('Output')

all_files = list(filter(lambda x: x if x.endswith('.xlsx') else None, os.listdir()))

if not all_files:
	print('No excel file found.')
	exit()

file_dict = dict()
print('Excel files found:')
for index,i in enumerate(all_files):
	file_dict[index+1] = i
	print(f"{index+1}. {i}")
print("\nWhich file to randomize: ")
while True:
	try:
		choice = int(input(">> "))
		if choice > len(file_dict):
			print("Out of range, try again...")
		else:
			break
	except:
		print("Invalid input.")

df = pd.read_excel(file_dict[choice])

seed = 1
while True:
	random_df = df.sample(frac=1, random_state=seed)
	print(random_df)
	print('randomize more? [y/n]')
	while True:
		try:
			choice2 = input('>> ').lower()
			if choice2 == 'y':
				seed += 1
				print("\n\n\n")
				break
			elif choice2 == 'n':
				break
		except:
			print("Invalid input.")
	if choice2 == 'y':
		pass
	else:
		break

print('Enter output file name:')
choice3 = input('>> ')
random_df.to_excel(f"Output/{choice3}.xlsx", index=False)
print(f"File {choice3}.xlsx successfully randomized!")