extends Control

# Called when the node enters the scene tree for the first time.
func _ready():
	GlobalRulesets.initializeConfig_rulesets()
	GlobalAllRuleDoc.getAllRuleDoc()
	#self.get_node("Label").text = GlobalValues.currentRule
	for i in GlobalValues.rulesets:
		self.get_node("OptionButton").add_item(i)
	#Set current rule as the one to change?

var ruleIndex = 0
func _on_OptionButton_item_selected(index):
	self.get_node("ChangeWindow").visible = false
	ruleIndex = index
	self.get_node("ScrollContainer/GridContainer").clearTree()
	var ruleset = GlobalValues.rulesets[index]
	self.get_node("ScrollContainer/GridContainer").changeToRuleset(ruleset)


# Used when change is pressed
var extraInput = []
var curIndex
func _on_ChangeButton_pressed(index):
	curIndex = index
	
	# Show Old Rule Input
	var inputNode = self.get_node("ChangeWindow/ScrollContainer/HBoxContainer/VBoxInName")
	inputNode.get_node("OLD_InputName").text = GlobalValues.inputArr[index].replace("&","\n")

	# Show Old Rule Ouput 
	var outputNode = self.get_node("ChangeWindow/ScrollContainer/HBoxContainer/VBoxOutName")
	outputNode.get_node("OLD_OutputName").text = GlobalValues.outputArr[index]

	# Show Old Rule Ouput Argument
	var outArgNode = self.get_node("ChangeWindow/ScrollContainer/HBoxContainer/VBoxOutArg")
	outArgNode.get_node("OLD_OutputArg").text = GlobalValues.outputArgArr[index]

	# Clear old
	if extraInput.size() > 0: 
		for i in extraInput:
			inputNode.remove_child(i)
		extraInput.empty()

	# Set all index one can choose
	# Set the shown one to current
	# Extra boxes can be shown 
	# Have "None" at top so one can remove extra
	var currentInput = GlobalValues.inputArr[index].split("&")
	
	# Puts all possible inputs into choice of input
	inputNode.get_node("EditInputName").clear()
	inputNode.get_node("EditInputName").add_item("None")
	for i in GlobalValues.allInputs["input"]:
		inputNode.get_node("EditInputName").add_item(i)
		
	# Select the curret input 
	var indexInput = GlobalValues.allInputs["input"].find(currentInput[0])
	inputNode.get_node("EditInputName").select(indexInput+1)
	
	# Add Extra input option if rule to change
	# has more than one input
	if currentInput.size() > 1:
		for j in range(currentInput.size()-1):
			var editInput = OptionButton.new()
			editInput = inputNode.get_node("EditInputName").duplicate()
			indexInput = GlobalValues.allInputs["input"].find(currentInput[j+1])
			editInput.select(indexInput+1)
			extraInput.append(editInput)
			inputNode.add_child_below_node(inputNode.get_node("EditInputName"), editInput)
	
	# Set so one can choose any output
	# Set so that current is being shown
	# Puts all possible inputs into choice of input
	outputNode.get_node("EditOutputName").clear()
	
	for i in GlobalValues.allOuputsGeneral["outputName"]:
		outputNode.get_node("EditOutputName").add_item(i)
	
	for i in GlobalValues.allOuputsPredef["outputName"]:
		outputNode.get_node("EditOutputName").add_item(i)
		
	# Find index of the output
	# first check if general then predef
	var indexOutput = GlobalValues.allOuputsGeneral["outputName"].find(GlobalValues.outputArr[index])
	outputNode.get_node("EditOutputName").select(indexOutput)
	
	var size = 0
	if indexOutput == -1:
		size = GlobalValues.allOuputsGeneral["outputName"].size()
		indexOutput = GlobalValues.allOuputsPredef["outputName"].find(GlobalValues.outputArr[index])
	
	# Select curret output
	outputNode.get_node("EditOutputName").select(indexOutput+size)
	
	# Show output argument
	outArgNode.get_node("EditOuputArg").text = GlobalValues.outputArgArr[index]
	
	self.get_node("ChangeWindow").visible = true
	

func _on_AddInput_pressed():
	var inputNode = self.get_node("ChangeWindow/ScrollContainer/HBoxContainer/VBoxInName")
	var editInput = OptionButton.new()
	editInput = inputNode.get_node("EditInputName").duplicate()
	#editInput.text = "None"
	#print("Selected Id",editInput.get_selected_id())
	extraInput.append(editInput)
	inputNode.add_child_below_node(inputNode.get_node("EditInputName"), editInput)


func _on_SaveButton_pressed():
	var ruleset = GlobalValues.rulesets[ruleIndex]
	
	# For check if there is an input selected
	var hasInput = false

	var inputNode = self.get_node("ChangeWindow/ScrollContainer/HBoxContainer/VBoxInName/EditInputName")
	var newInput = []
	
	# If "none" NOT selected
	if inputNode.get_selected_id() > 0:
		newInput.append(GlobalValues.allInputs["input"][inputNode.get_selected_id()-1])
		hasInput = true
	
	for node in extraInput:
		if node.get_selected_id() > 0:
			
			# Check to see if input has been found before
			if !hasInput: 
				newInput.append(GlobalValues.allInputs["input"][node.get_selected_id()-1])
				
			# Check to make sure the input doesn't exist
			elif newInput.find(GlobalValues.allInputs["input"][node.get_selected_id()-1]):
				newInput.append("&")
				newInput.append(GlobalValues.allInputs["input"][node.get_selected_id()-1])
			
			hasInput = true
			
	newInput = String(newInput).replace(" ", "").replace(",", "").replace("[", "").replace("]", "")
	
	# Check if there has been an input selected
	# if not, then we won't save and a window will be shown
	if !hasInput:
		print("MISSING: NO INPUT SELECTED")
		self.get_node("MissingInOutPut").visible = true
		return -1
	
	# # # #
	# check if selected output is general or not
	# As general is first in options, we use the size to help
	#
	# --- NEW OUTPUT --- #
	var isGeneral = true
	var outputNode = self.get_node("ChangeWindow/ScrollContainer/HBoxContainer/VBoxOutName/EditOutputName")
	var newOutput
	
	var outGenNum = GlobalValues.allOuputsGeneral["outputName"].size()
	var outID = outputNode.get_selected_id()
	# If outputID is more than the number of general outputs
	# Then it's a predef output
	if outID >= outGenNum: # For predef Output
		newOutput = GlobalValues.allOuputsPredef["outputName"][outputNode.get_selected_id()-outGenNum]
		isGeneral = false
	else: # For gen Output
		newOutput = GlobalValues.allOuputsGeneral["outputName"][outputNode.get_selected_id()]
	
	# --- NEW OUTPUT ARG --- #
	var outArgNode = self.get_node("ChangeWindow/ScrollContainer/HBoxContainer/VBoxOutArg/EditOuputArg")
	var newOutArg  = outArgNode.text
	
	# Save the changes of the rule
	GlobalRulesets.changeRule(ruleset, curIndex, newInput, newOutput, isGeneral, newOutArg)
	GlobalValues.loadFilePaths()
	
	# After all is saved
	# Close the window and reload ruleset so changes can be seen
	self.get_node("ChangeWindow").visible = false
	self.get_node("ScrollContainer/GridContainer").changeToRuleset(ruleset)
