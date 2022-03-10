extends PopupDialog

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.

# Position of the mouse
var mousePos

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	# Change the position of box so it follows mouse
	
	mousePos = get_viewport().get_mouse_position()
	mousePos[0] = mousePos[0]+5
	mousePos[1] = mousePos[1]+5
	
	self.set_position( mousePos )

# Show and hide box 
func _on_CheckButton_mouse_entered():
	self.visible = true

func _on_CheckButton_mouse_exited():
	self.visible = false
