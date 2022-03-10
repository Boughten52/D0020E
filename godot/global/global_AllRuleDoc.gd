extends Node

# # # # # # # # # # # # # # # # # # # # # # # # # # #
# Get the config for documentation of all in/out puts
func initializeConfig_allRuleDoc():
	GlobalValues.config_allRuleDoc = ConfigFile.new()
	# Load data from a file.
	var err = GlobalValues.config_allRuleDoc.load(GlobalValues.filepath_allRuleDoc)
	
	# If the file didn't load, ignore it.
	if err != OK:
		return

# Updates all varibles related to all rules
func getAllRuleDoc():
	GlobalValues.config_allRuleDoc = ConfigFile.new()
	# Load data from a file.
	var err = GlobalValues.config_allRuleDoc.load(GlobalValues.filepath_allRuleDoc)
	# If the file didn't load, ignore it.
	if err != OK:
		return
	
	var section = GlobalValues.config_allRuleDoc.get_sections()
	section = Array(section)
	
	# Gets the index of ruletype [input] or [output]
	var inputIndex = section.find("input")
	var OuputPreDefIndex = section.find("predefined_outputArgument")
	var OuputGenIndex = section.find("general_outputArgument")
	
	# Checks all at once
	# If any of the three are missing then an 
	# Alert will be given to the user and 
	# the program will return -1 (error)
	if (inputIndex == -1 || OuputPreDefIndex == -1 || OuputGenIndex == -1):
		print("The ''documentation.toml'' file isn't complete")
		OS.alert("The \"documentation.toml\" file isn't complete")
		return -1
	
	var sKeys
	
	# Insert all Inputs
	sKeys = GlobalValues.config_allRuleDoc.get_section_keys(section[inputIndex])
	for i in sKeys:
		GlobalValues.allInputs[i] = GlobalValues.config_allRuleDoc.get_value(section[inputIndex], i)
	
	# Insert all Outputs
	sKeys = GlobalValues.config_allRuleDoc.get_section_keys(section[OuputPreDefIndex])
	for i in sKeys:
		GlobalValues.allOuputsPredef[i] = GlobalValues.config_allRuleDoc.get_value(section[OuputPreDefIndex], i)
	
	# Insert all Outputs
	sKeys = GlobalValues.config_allRuleDoc.get_section_keys(section[OuputGenIndex])
	for i in sKeys:
		GlobalValues.allOuputsGeneral[i] = GlobalValues.config_allRuleDoc.get_value(section[OuputGenIndex], i)

# # # # # # # # # # # # # # # # # # # # # # 
# Writes to the file containing all rules
# Using the function, we assume that 
# the function "getAllRules" has already been used
# and that an modification has been made to the varibles
# related to all rules
# TL;DR
# This Function saves "All Input/Output" varibles to 
# the file with all rules
func updateAllRuleDoc():
	#getAllRuleDoc()
	#GlobalValues.config_allRuleDoc
	
	var keys
	
	keys = GlobalValues.allInputs.keys()
	for i in keys:
		GlobalValues.config_allRuleDoc.set_value("input", i, GlobalValues.allInputs[i])
	
	keys = GlobalValues.allOuputsPredef.keys()
	for i in keys:
		GlobalValues.config_allRuleDoc.set_value("predefined_outputArgument", i, GlobalValues.allOuputsPredef[i])
	
	keys = GlobalValues.allOuputsGeneral.keys()
	for i in keys:
		GlobalValues.config_allRuleDoc.set_value("general_outputArgument", i, GlobalValues.allOuputsGeneral[i])
	
	GlobalValues.config_allRuleDoc.save(GlobalValues.filepath_rulesets)
