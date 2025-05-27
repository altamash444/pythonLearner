import os, random, string

directory = "Clear The Clutter"
if directory in os.listdir():
	pass
else:
	os.mkdir(directory)

def listAll():
	print("The files are")
	print(os.listdir("Clear The Clutter"))
	
def clearAll():
	directory = "Clear The Clutter"
	for file in os.listdir(directory):
		filepath = os.path.join(directory, file)
		os.remove(filepath)
	if not os.listdir(directory):
		print("All files removed!")

def createFiles(extension, nof):
	for i in range(nof):
		filename = (random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+extension)
		
		dirname = "Clear The Clutter"
		filespath = os.path.join(dirname, filename)
		file = open(filespath, "w")
		file.close()
	print(f"{nof} random {extension} files created successfully!")

def manageFiles(extension):
	index = 0
	for file in os.listdir("Clear The Clutter"):
		print(index)
		if file.endswith(extension):
			index += 1
			filepath = os.path.join("Clear The Clutter", file)
			newfilepath = os.path.join("Clear The Clutter", str(index)+extension)
			os.rename(filepath, newfilepath)
	print(f"{index} files renamed successfully!")
	
## To create files ('extension_type',number_of_files)
#createFiles(".png", 10)

## To rename all the files in order with input as extension
#manageFiles(".png")

## To delete all the files in the folder
#clearAll()

## To list all the files in the directory
#listAll()