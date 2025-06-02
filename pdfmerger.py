import os
from pypdf import PdfWriter

path = "SamplePdf/"
outputDir = "OutputPdf/"

if os.path.exists(path):
	pass
else:
	os.mkdir(path)
if os.path.exists(outputDir):
	pass
else:
	os.mkdir(outputDir)

print(f"Drop the input pdf files in {path} for operations.")
inputFiles = os.listdir(path)
inputFiles.sort()
if inputFiles:
	print(f"The files in directory are: \n{inputFiles}")
	choice = str(input("Merge them? y/n\n--> "))
	choice = choice.lower()
	if choice == "y":
		outputName = str(input("Enter output PDF name: "))
		outputPath = os.path.join(outputDir, outputName+".pdf")
		merger = PdfWriter()
		for file in inputFiles:
			merger.append(f"{path}{file}")
		merger.write(outputPath)
		print("PDF successfully merged.")
	elif choice == "n":
		print("Program exited.")
		exit()
	else:
		print("Error: Invalid input.")
		exit()
else:
	print("There are no files in directory.")