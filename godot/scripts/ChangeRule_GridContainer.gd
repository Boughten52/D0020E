extends GridContainer

# Called when the node enters the scene tree for the first time.
func _ready():
	GlobalRulesets.initializeConfig_rulesets()
	#changeToRuleset("rules_0")

var inputNodes = []
var outputNodes = []
var outputArgNodes = []
var changeNodes = []

func changeToRuleset(ruleset):
	#var index = Button.new()
	var input = Label.new()
	var output = Label.new()
	var outputArg = Label.new()
	var change = Button.new()
	
	# Get the ruleset selected
	GlobalValues.inputArr = GlobalValues.config_rulesets.get_value(ruleset, "inputName")
	GlobalValues.outputArr = GlobalValues.config_rulesets.get_value(ruleset, "outputName")
	GlobalValues.outputArgArr = GlobalValues.config_rulesets.get_value(ruleset, "outputArgument")
	
	clearTree()
	
	for i in range(GlobalValues.inputArr.size()):
		# For Index
#		index.SIZE_EXPAND
#		index.text = String(i)
#		add_child(index)
#		index = Button.new()
		
		# For Input
		input.SIZE_FILL
		input.text = GlobalValues.inputArr[i].replace("&","\n")
		add_child(input)
		inputNodes.append(input)
		input = Label.new()
		
		# For Output Name
		output.SIZE_EXPAND_FILL
		output.text = GlobalValues.outputArr[i]
		add_child(output)
		outputNodes.append(output)
		output = Label.new()
		
		# For Output Arg
		outputArg.SIZE_FILL
		outputArg.text = GlobalValues.outputArgArr[i]
		add_child(outputArg)
		outputArgNodes.append(outputArg)
		outputArg = Label.new()
		
		# For Output
		change.SIZE_EXPAND
		change.text = "Change"
		#change.add_constant_override("ruleIndex", i)
		var controlNode = get_node("/root/Control")
		change.connect("pressed", controlNode, "_on_ChangeButton_pressed", [i])
		add_child(change)
		changeNodes.append(change)
		change = Button.new()


# Clear all nodes currently being displayed
func clearTree():
	for i in inputNodes:
		i.queue_free()
	inputNodes.clear()
	
	for i in outputNodes:
		i.queue_free()
	outputNodes.clear()
	
	for i in outputArgNodes:
		i.queue_free()
	outputArgNodes.clear()
	
	for i in changeNodes:
		print(i.get_constant("ruleIndex"))
		i.queue_free()
	changeNodes.clear()
