extends Control


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	GlobalValues.loadFilePaths()
	GlobalRulesets.initializeConfig_rulesets()
	GlobalAllRuleDoc.initializeConfig_allRuleDoc()
	
	GlobalRulesets.changeSimilator(false)
	
	VisualServer.set_default_clear_color(Color(0.34, 0.2, 0.57, 1.0))
	
	var buttonUSER = get_node("ButtonUSER")
	buttonUSER.connect("pressed", self, "_button_pressed_USER")
	
	var buttonTEST = get_node("ButtonTEST")
	buttonTEST.connect("pressed", self, "_button_pressed_TEST")
	
	var buttonADMIN = get_node("ButtonADMIN")
	buttonADMIN.connect("pressed", self, "_button_pressed_ADMIN")
	
# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func _button_pressed_USER():
	get_tree().change_scene("res://godot/scene/user.tscn")
	
func _button_pressed_TEST():
	#self.get_node("AudioStreamPlayer").play()
	#self.get_node("AudioStreamPlayer").stop()

	get_tree().change_scene("res://godot/scene/testUser.tscn")
	#GlobalRulesets.updateActiveRuleset("rules_0")
	
#	print(GlobalValues.rulesets)
#	GlobalValues.loadFilePaths()
	
func _button_pressed_ADMIN():
	GlobalAllRuleDoc.initializeConfig_allRuleDoc()
	get_tree().change_scene("res://godot/scene/admin.tscn")
	#GlobalValues.updateAllRules()
