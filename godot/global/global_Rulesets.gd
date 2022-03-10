extends Node


# # # # # # # # # # # # # # # # # # # # 
# Get the config for all rulesets
func initializeConfig_rulesets():
	GlobalValues.config_rulesets = ConfigFile.new()
	# Load data from a file.
	var err = GlobalValues.config_rulesets.load(GlobalValues.filepath_rulesets)
	
	# If the file didn't load, ignore it.
	if err != OK:
		return
	
	# Save all ruleset names 
	# [ excluding userinfo and simulator]
	var sections = GlobalValues.config_rulesets.get_sections()
	sections = Array(sections)
	sections.erase("userinfo")
	sections.erase("simulator")

	GlobalValues.rulesets = sections
	#print(GlobalValues.rulesets)
	
	GlobalValues.activeRule = GlobalValues.config_rulesets.get_value("userinfo", "activeRule")
	#print(GlobalValues.activeRule)


# Updates which rule should be currently run
func updateActiveRuleset(rulename="No Rule selected"):
	initializeConfig_rulesets()
	GlobalValues.activeRule = rulename
	GlobalValues.config_rulesets.set_value( "userinfo", "activeRule", rulename )
	GlobalValues.config_rulesets.save(GlobalValues.filepath_rulesets)


# Update config for all rules
func updateRulesetInfo(rulesetName, input, output, outfunc, outputArg="", uniqOutArg=false):
	initializeConfig_rulesets()
	
	# If not uniq, we want to get the config_allRuleDoc
	if uniqOutArg==false:
		var arr1 = GlobalValues.config_allRuleDoc.get_value("predefined_outputArgument", "outputName")
		var index1 = arr1.find(output)
		var arr2 = GlobalValues.config_allRuleDoc.get_value("predefined_outputArgument", "outputArgument")
		outputArg = arr2[index1]
		
	var keys = ["inputName","outputName","outputFunction","outputArgument"]
	
	var inputNameArr  = []
	var outputNameArr = []
	var outputFuncArr = []
	var outputArgArr  = []
	
	
	if Array(GlobalValues.config_rulesets.get_sections()).has(rulesetName):
		# Get current input/output for the ruleset and append with new input

		inputNameArr  = GlobalValues.config_rulesets.get_value(rulesetName, keys[0])
		outputNameArr = GlobalValues.config_rulesets.get_value(rulesetName, keys[1])
		outputFuncArr = GlobalValues.config_rulesets.get_value(rulesetName, keys[2])
		outputArgArr  = GlobalValues.config_rulesets.get_value(rulesetName, keys[3])
	
		print(inputNameArr)
		# Error check to make sure the rule isn't a duplicate
		# This is done by going through all rules and making sure none are 
		# fully the same on all fronts (should work well with &rules)
		for i in range(inputNameArr.size()):
			if inputNameArr[i] == input && outputNameArr[i] == output && outputFuncArr[i] == outfunc && outputArgArr[i] == outputArg:
				print("The rule was a duplicate, Not saved")
				return -1
	print(inputNameArr)
	inputNameArr = Array(inputNameArr)
	print(inputNameArr)
	# Append the new rule
	inputNameArr.append(input)
	outputNameArr.append(output)
	outputFuncArr.append(outfunc)
	outputArgArr.append(outputArg)
	
	
	# Input everything into config
	GlobalValues.config_rulesets.set_value(rulesetName, keys[0], inputNameArr)
	GlobalValues.config_rulesets.set_value(rulesetName, keys[1], outputNameArr)
	GlobalValues.config_rulesets.set_value(rulesetName, keys[2], outputFuncArr)
	GlobalValues.config_rulesets.set_value(rulesetName, keys[3], outputArgArr)
	
	# Save the config to desierd place
	GlobalValues.config_rulesets.save(GlobalValues.filepath_rulesets)
	
	#print(GlobalValues.config_rulesets.get_value("userinfo", "user"))
	#print(GlobalValues.config_rulesets.get_value("rules_0","inputName"))
	
	#GlobalValues.rulesets = GlobalValues.config_rulesets.get_sections()

func changeRule(rulesetName, index, newInput, newOutput, isGeneral=false, outputArg=""):
	# The outfunction related to the output
	var outfunc
	
	# If not uniq, we want to get the config_allRuleDoc
	
	# Get the argument and outfunction of predef (aka not-General)
	# get the outfunction of general
	if !isGeneral:
		var arr1 = GlobalValues.config_allRuleDoc.get_value("predefined_outputArgument", "outputName")
		var index1 = arr1.find(newOutput)
		var arr2 = GlobalValues.config_allRuleDoc.get_value("predefined_outputArgument", "outputArgument")
		outputArg = arr2[index1]
		var arr3 = GlobalValues.config_allRuleDoc.get_value("predefined_outputArgument", "outputFunction")
		outfunc = arr3[index1]
	else:
		var arr1 = GlobalValues.config_allRuleDoc.get_value("general_outputArgument", "outputName")
		var index1 = arr1.find(newOutput)
		var arr3 = GlobalValues.config_allRuleDoc.get_value("general_outputArgument", "outputFunction")
		outfunc = arr3[index1]
	
	var keys = ["inputName","outputName","outputFunction","outputArgument"]
	
	var inputNameArr  = []
	var outputNameArr = []
	var outputFuncArr = []
	var outputArgArr  = []
	
	
	if Array(GlobalValues.config_rulesets.get_sections()).has(rulesetName):
		# Get current input/output for the ruleset and append with new input

		inputNameArr  = GlobalValues.config_rulesets.get_value(rulesetName, keys[0])
		outputNameArr = GlobalValues.config_rulesets.get_value(rulesetName, keys[1])
		outputFuncArr = GlobalValues.config_rulesets.get_value(rulesetName, keys[2])
		outputArgArr  = GlobalValues.config_rulesets.get_value(rulesetName, keys[3])
	
		print(inputNameArr)
		# Error check to make sure the rule isn't a duplicate
		# This is done by going through all rules and making sure none are 
		# fully the same on all fronts (should work well with &rules)
		for i in range(inputNameArr.size()):
			if inputNameArr[i] == newInput && outputNameArr[i] == newOutput && outputFuncArr[i] == outfunc && outputArgArr[i] == outputArg:
				print("Note: The rule was a duplicate")
				# Call to remove rule
				return -1
				
	print(inputNameArr)
	inputNameArr = Array(inputNameArr)
	print(inputNameArr)
	
	# Replace with the new rule
	inputNameArr[index]  = newInput
	outputNameArr[index] = newOutput
	outputFuncArr[index] = outfunc
	outputArgArr[index]  = outputArg
	
	
	# Input everything into config
	GlobalValues.config_rulesets.set_value(rulesetName, keys[0], inputNameArr)
	GlobalValues.config_rulesets.set_value(rulesetName, keys[1], outputNameArr)
	GlobalValues.config_rulesets.set_value(rulesetName, keys[2], outputFuncArr)
	GlobalValues.config_rulesets.set_value(rulesetName, keys[3], outputArgArr)
	
	# Save the config to desierd place
	GlobalValues.config_rulesets.save(GlobalValues.filepath_rulesets)
	
func removeRule(rulesetName, index=-1):
	if index < 0:
		# Remove all rules
		return
		
	var keys = ["inputName","outputName","outputFunction","outputArgument"]
	
	var inputNameArr  = []
	var outputNameArr = []
	var outputFuncArr = []
	var outputArgArr  = []
	
	if Array(GlobalValues.config_rulesets.get_sections()).has(rulesetName):
		# Get current input/output for the ruleset and append with new input
		inputNameArr  = GlobalValues.config_rulesets.get_value(rulesetName, keys[0])
		outputNameArr = GlobalValues.config_rulesets.get_value(rulesetName, keys[1])
		outputFuncArr = GlobalValues.config_rulesets.get_value(rulesetName, keys[2])
		outputArgArr  = GlobalValues.config_rulesets.get_value(rulesetName, keys[3])

	# Remove the rule at "index"
	inputNameArr.remove(index)
	outputNameArr.remove(index)
	outputFuncArr.remove(index)
	outputArgArr.remove(index)
	
	
	# Input everything into config
	GlobalValues.config_rulesets.set_value(rulesetName, keys[0], inputNameArr)
	GlobalValues.config_rulesets.set_value(rulesetName, keys[1], outputNameArr)
	GlobalValues.config_rulesets.set_value(rulesetName, keys[2], outputFuncArr)
	GlobalValues.config_rulesets.set_value(rulesetName, keys[3], outputArgArr)
	
	# Save the config to desierd place
	GlobalValues.config_rulesets.save(GlobalValues.filepath_rulesets)


func removeRuleset(rulesetName):
	GlobalValues.config_rulesets.erase_section(rulesetName)
	GlobalValues.config_rulesets.save(GlobalValues.filepath_rulesets)

# State is either true or false
func changeSimilator(state):
	GlobalValues.config_rulesets.set_value("simulator","enabled",state)
	GlobalValues.config_rulesets.save(GlobalValues.filepath_rulesets)
