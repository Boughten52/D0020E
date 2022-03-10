extends Node

var filepath_allRuleDoc = 'res://godot/files/documentation.toml'
var filepath_rulesets = 'res://godot/files/config_rules.toml'


var config_allRuleDoc
var config_rulesets

var activeRule = "No Rule selected"

# All inputs, 
# Is to contain all possible inputs that the program takes
var allInputs = {}

# All Outputs Pre-Defined,
# where the "outputArgument" is predefined
var allOuputsPredef = {}

# All Outputs General,
# Where on rulecreation, one has to define what the 
# "outputArgument" should be for that specific rule
var allOuputsGeneral = {}

# Array with all ruleset names
var rulesets

# For the ruleset selected
var inputArr 
var outputArr
var outputArgArr

#var homeScene = ""

# USER INFO
var userId = 0
var currentRule = "No rule is active"
# 0 = TEST
# 1 = ADMIN
# 2 = USER
# 3 = USER ?

var id = 0

func runMain():
	OS.kill(id)
	id = OS.execute("python", ["main.py"], false)
	
func stopRunningMain():
	OS.kill(id)

# Gets the filepath for allRuleDoc and rulesets
# From "filepaths.txt" which should in the same
# folder as main.py and godot_interface
func loadFilePaths():
	var file = File.new()
	file.open("filepaths.txt", File.READ)
	var content = file.get_as_text()
	file.close()
	content = content.replacen(" ","")
	
	for path in content.split("\n"):
		if path.begins_with("filepath_allRuleDoc"):
			filepath_allRuleDoc = path.substr(path.find("=") + 1)
			print("ALL:",filepath_allRuleDoc)
		if path.begins_with("filepath_rulesets"):
			print("foundSets")
			filepath_rulesets = path.substr(path.find("=") + 1)
			print("RULE:",filepath_rulesets)
	
	
