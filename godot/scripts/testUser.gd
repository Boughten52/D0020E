extends Control


# Called when the node enters the scene tree for the first time.
func _ready():
	GlobalRulesets.initializeConfig_rulesets()
	GlobalAllRuleDoc.getAllRuleDoc()
	#self.get_node("Label").text = GlobalValues.currentRule
	self.get_node("OptionButton").add_item("No Rule Selected")
	for i in GlobalValues.rulesets:
		self.get_node("OptionButton").add_item(i)
	#Set current rule as the one to change?
	print(GlobalValues.currentRule)


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass

# Run the simulator
func _on_RunSimButton_pressed():
	GlobalRulesets.changeSimilator(true)
	GlobalValues.runMain()
	



func _on_StopSimButton_pressed():
	GlobalRulesets.changeSimilator(false)
	GlobalValues.stopRunningMain()


func _on_OptionButton_item_selected(index):
	#self.get_node("ActiveRuleLabel").text = "Selected Rule: " + GlobalValues.rulesets[index]
	GlobalValues.activeRule = GlobalValues.rulesets[index-1]
	print(GlobalValues.activeRule)
	GlobalRulesets.updateActiveRuleset(GlobalValues.activeRule)

