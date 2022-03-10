extends Control

# Called when the node enters the scene tree for the first time.
func _ready():
	var button = get_node("Button")
	
	GlobalRulesets.initializeConfig_rulesets()
	GlobalAllRuleDoc.getAllRuleDoc()
	#self.get_node("Label").text = GlobalValues.currentRule
	for i in GlobalValues.rulesets:
		self.get_node("OptionButton").add_item(i)
	#Set current rule as the one to change?
	
	self.get_node("ActiveRuleLabel").text = "Selected Rule: " + GlobalValues.activeRule
#	for keyName in GlobalValues.rulesets:
#		self.get_node("OptionButton").add_item(keyName) 
	self.get_node("ScrollContainer/GridContainer").changeToRuleset(GlobalValues.activeRule)
	
	
func updateCurrentRule():
	pass


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass



func _on_AddNew_pressed():
	get_tree().change_scene("res://godot/scene/addNewRule.tscn")


func _on_Change_pressed():
	get_tree().change_scene("res://godot/scene/changeRule.tscn")


func _on_Remove_pressed():
	get_tree().change_scene("res://godot/scene/removeRule.tscn")


func _on_OptionButton_item_selected(index):
	self.get_node("ActiveRuleLabel").text = "Selected Rule: " + GlobalValues.rulesets[index]
	GlobalValues.activeRule = GlobalValues.rulesets[index]
	GlobalRulesets.updateActiveRuleset(GlobalValues.activeRule)
	
	# Change the current ruleset
	self.get_node("ScrollContainer/GridContainer").changeToRuleset(GlobalValues.activeRule)
	


func _on_RunButton_pressed():
	GlobalValues.runMain()


func _on_StopButton_pressed():
	GlobalValues.stopRunningMain()
