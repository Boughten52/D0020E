extends Control

# Called when the node enters the scene tree for the first time.
func _ready():
	# Create scrollcontainers for Input and Output
	# Take names from global dir
	var node = self.get_node("ScrollContainerINPUT").get_node("VBoxContainer")
	
	var rule_scene = load("res://godot/scene/HBoxForRules.tscn")
	var rule 
	
	# Error check, error if no input
	var err = GlobalAllRuleDoc.getAllRuleDoc()
	if err == -1:
		return
	
	# For the INPUTS
	for keyName in GlobalValues.allInputs["input"]:
		rule = rule_scene.instance()
		rule.get_node("Label").text = keyName
		node.add_child(rule)
	
	# For the OUTPUTS_PREDEF
	node = self.get_node("ScrollContainerOUTPUT_PREDEF").get_node("VBoxContainer")
	for keyName in GlobalValues.allOuputsPredef["outputName"]:
		rule = rule_scene.instance()
		rule.get_node("Label").text = keyName
		node.add_child(rule)
	
	# For the OUTPUTS_GEN
	node = self.get_node("ScrollContainerOUTPUT_GEN").get_node("VBoxContainer")
	for keyName in GlobalValues.allOuputsGeneral["outputName"]:
		rule = rule_scene.instance()
		rule.get_node("Label").text = keyName
		node.add_child(rule)
	
	
	# if nothing found in dir
	# create popup and inform of such
	
	GlobalRulesets.initializeConfig_rulesets()
	GlobalAllRuleDoc.getAllRuleDoc()
	print("ALL THE rulesets")
	self.get_node("Label").text = GlobalValues.currentRule
	for i in GlobalValues.rulesets:
		print(i)
		self.get_node("OptionButton").add_item(i)


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass

var id = 0
func _on_ButtonSAVE_pressed():
	get_node("Saved").visible = false
	get_node("NotSaved").visible = false
	# bool varibels to check 
	# what the user has choosen
	var checkBoxPressed
	var checkButtonPressed 
	
	# If no Input has been choosen then we should not check output
	# And if there is no Output chossen then there is no rule to save
	var createOutput = false
	var hasOutput = false
	
	#Save things in name and array
	var rulename
	var inputName = ""
	var outputName = ""
	var outputfunc = ""
	var outputArg = ""
	
	# Get The name of the rule
	var node = get_node("Label").text
	
	# Check if the node begins with the right format
	if node.begins_with("rules_"):
		rulename = node
	else:
		print("BAD name: Please use a proper name format 'rules_'")
		get_node("NotSaved").visible = true
		return -1
	
	# Get the child nodes for the input
	var inputNode = get_node("ScrollContainerINPUT").get_node("VBoxContainer").get_children()
	# Go through each node to check what has been choosen
	for Hbox in inputNode:
		checkBoxPressed = Hbox.find_node("CheckBox").pressed
		
		# Mark that we should create output
		# Save the choosen inputs in 'input'
		if checkBoxPressed:
			createOutput = true
			if inputName == "":
				inputName = Hbox.get_node("Label").text
			else:
				inputName = inputName +"&"+ Hbox.get_node("Label").text
	
	
	# Check if output should be made
	if createOutput != true:
		print("No Input, Nothing to save")
		get_node("NotSaved").visible = true
		return -1
	
	
	# Get all the outputs
	
	# OutputNode for PREDEF
	var outputNode = get_node("ScrollContainerOUTPUT_PREDEF").get_node("VBoxContainer").get_children()
	# Go through each node to check what has been choosen
	for Hbox in outputNode:
		checkBoxPressed = Hbox.find_node("CheckBox").pressed
		
		if checkBoxPressed:
			hasOutput = true
			outputName = Hbox.get_node("Label").text
			
			var predefArr = GlobalValues.allOuputsPredef["outputName"]
			var index = predefArr.find(outputName)
			outputfunc = GlobalValues.allOuputsPredef["outputFunction"][index]
			
			GlobalRulesets.updateRulesetInfo(rulename, inputName, outputName, outputfunc)
	
	
	# OutputNode for GENERAL
	outputNode = get_node("ScrollContainerOUTPUT_GEN").get_node("VBoxContainer").get_children()
	# Go through each node to check what has been choosen
	for Hbox in outputNode:
		checkBoxPressed = Hbox.find_node("CheckBox").pressed
		
		if checkBoxPressed:
			hasOutput = true
			outputName = Hbox.get_node("Label").text
			
			var genArr = GlobalValues.allOuputsGeneral["outputName"]
			var index = genArr.find(outputName)
			outputfunc = GlobalValues.allOuputsGeneral["outputFunction"][index]
			
			outputArg = self.get_node("LineEdit").text
			
			GlobalRulesets.updateRulesetInfo(rulename, inputName, outputName, outputfunc, outputArg, true)
	
	
	if hasOutput != true:
		print("No Output, Nothing to save")
		get_node("NotSaved").visible = true
		return -1
	
	#Call save config and display save
	
	get_node("Saved").visible = true
	
############## END OF SAVE ###################

func _on_OptionButton_item_selected(index):
	# A ruleset has been displayed
	# Show it
	var arr = GlobalValues.rulesets
	print(arr[index])
	
	self.get_node("Label").text = arr[index]
	get_node("Saved").visible = false
	get_node("NotSaved").visible = false
	


func _on_ButtonKill_pressed():
	OS.kill(id)
