extends Button


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


func _on_HomeButton_pressed():
	# if the similator is running
	if GlobalValues.config_rulesets.get_value("simulator","enabled"):
		GlobalRulesets.changeSimilator(false)
		GlobalValues.stopRunningMain()
		
	get_tree().change_scene("res://godot/scene/main.tscn")
