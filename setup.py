from lib2to3.pgen2.token import OP
import os
from turtle import fd

# Change this values according to your Project.
ModuleName = os.path.split(os.path.split(__file__)[0])[1]
ModuleDisplayName = ModuleName.replace('-', ' ')
ModuleDescription = ""
ModuleAuthorName = ""

ScriptName = os.path.split(__file__)[1]

# Check name
if ' ' in ModuleName:
	raise NameError("Module name have space.")
elif ModuleName == 'Magisk-Module-Template':
	raise NotImplementedError()

def makeTree(source = '.'):
	tree = []
	for p in os.listdir(source):
		if os.path.isdir(os.path.join(source, p)) and not p in ['.git', '.vs']:
			for path in makeTree(os.path.join(source, p)):
				tree.append(path)
		elif os.path.isfile(os.path.join(source, p)) and not p in [ScriptName]:
			tree.append(os.path.join(source, p))
	return tree

for f in makeTree():
	with open(f, 'r') as file:
		fData = file.read()
	
	hasModified = False
	# Replace module name
	if '@(ModuleName)' in fData:
		fData = fData.replace('@(ModuleName)', ModuleName)
		hasModified = True
	# Replace module display name
	if '@(ModuleDisplayName)' in fData:
		fData = fData.replace('@(ModuleDisplayName)', ModuleDisplayName)
		hasModified = True
	#Replace module description
	if '@(ModuleDescription)' in fData:
		fData = fData.replace('@(ModuleDescription)', ModuleDescription)
		hasModified = True
	# Replace module author name
	if '@(ModuleAuthorName)' in fData:
		fData = fData.replace('@(ModuleAuthorName)', ModuleAuthorName)
		hasModified = True
	
	# Do modifications
	if hasModified:
		with open(f, 'w') as file:
			file.write(fData)

