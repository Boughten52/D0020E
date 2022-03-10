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
	ruleIndex = index
	self.get_node("ScrollContainer/GridContainer").clearTree()
	var ruleset = GlobalValues.rulesets[index]
	self.get_node("ScrollContainer/GridContainer").changeToRuleset(ruleset)


# Used when remove is pressed
func _on_RemoveButton_pressed(index):
	var ruleset = GlobalValues.rulesets[ruleIndex]
	GlobalRulesets.removeRule(ruleset, index)
	
	# Reload, so changes can be seen
	#self.get_node("ScrollContainer/GridContainer").clearTree()
	self.get_node("ScrollContainer/GridContainer").changeToRuleset(ruleset)


# Currently not being used
#func _on_CheckBoxAll_toggled(button_checked):
#	print(button_checked)
#	# When button is checked
#	if button_checked:
#		# Check everything
#		pass
#	else:
#		# Uncheck everything
#		pass

# Removes the ruleset and reloads the scen
func _on_RemoveRuleset_pressed():
	var ruleset = GlobalValues.rulesets[ruleIndex]
	GlobalRulesets.removeRuleset(ruleset)
	get_tree().reload_current_scene()
