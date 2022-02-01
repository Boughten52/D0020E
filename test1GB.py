import toml



def testFunction1(arg):
    print(arg)



def testFunction2(arg):
    print("aaaaaaaaa")
    print(arg)
    print("bbbbbbbbb")




config = toml.load("config.toml")


currentUserList = "rules_" + str(config["userinfo"]["user"])

inputFunction = config[currentUserList]["inputFunction"]
inputArgument = config[currentUserList]["inputArgument"]
inputName = config[currentUserList]["inputName"]
outputName = config[currentUserList]["outputName"]
outputFunction = config[currentUserList]["outputFunction"]
outputArgument = config[currentUserList]["outputArgument"]


data = "door_42_open"
data = "apa"

if data in inputName:
    indexList = []
    i = 0
    for e in inputName:
        if data == e:
            indexList.append(i)
        i = i+1

    for index in indexList:
        eval(outputFunction[index])(outputArgument[index]) # eval is unsafe in a way



