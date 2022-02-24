from tkinter import *
from tkinter.ttk import Combobox

import toml


class Element:
    def __init__(self, obj, marginStepsLeft, marginStepsRight, marginStepsUp,
                 marginStepsDown):  # not actually margin but...
        self.obj = obj
        self.marginStepsLeft = marginStepsLeft
        self.marginStepsRight = marginStepsRight
        self.marginStepsUp = marginStepsUp
        self.marginStepsDown = marginStepsDown


class Level:
    def __init__(self, levels, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        nameList = []
        for e in levels:
            nameList.append(e.name)
        if name in nameList:
            i = nameList.index(name)
            self.x = levels[i].x
            self.y = levels[i].y


class KeyValue:
    def __init__(self, keyName, value):
        self.keyName = keyName
        self.value = value


class ConfigData:
    def __init__(self, configFileName):
        self.configFileName = configFileName
        config_rules = toml.load(self.configFileName)
        self.data = []
        self.rules_lst = []
        self.rules_lst_content = []
        for e in config_rules.keys():
            self.rules_lst.append(e)
            a = KeyValue(e, [])
            self.data.append(a)

        i = -1
        for e in config_rules:
            i = i + 1
            for ee in config_rules[e]:
                if i == 0:
                    self.rules_lst_content.append(ee)
                a = KeyValue(ee, " ")
                self.data[i].value.append(a)
                self.data[i].value[-1].value = config_rules[e][ee]

    def writeTo(self):
        f = open(self.configFileName, 'w')
        for e in self.data:
            str = "[" + e.keyName + "]\n"
            f.write(str)
            for ee in e.value:
                try:  # if value at bottom are list or similar
                    lastIndex = len(ee.value) - 1
                    i = -1
                    str = ee.keyName + " = ["
                    for tmp in ee.value:
                        i = i + 1
                        if i == lastIndex:
                            str = str + "\"" + tmp + "\""
                        else:
                            str = str + "\"" + tmp + "\","
                    str = str + "]\n"
                except:  # if value at bottom are 1 object/thing/number/string
                    str = str + ee.keyName
                    str = str + " = " + "% s" % ee.value + "\n"
                f.write(str)
            f.write("\n\n")
        f.close()


class MyWindow:
    def __init__(self, win):
        self.win = win

        self.stepSize = 50

        self.lp_defaultStartX = 50
        self.lp_x = 0
        self.lp_y = 0

        self.elementsAndLevels = self.initElementsAndLevels()
        self.levels = self.initLevels()

        self.complexity = ["simple"]
        self.complexityFunctions = ["simpleFunction"]

        cd = ConfigData("config_new.toml")

        i = -1
        ii = -1
        for e in cd.data:
            i = i + 1
            if e.keyName == "userinfo":
                ii = -1
                for ee in e.value:
                    ii = ii + 1
                    if ee.keyName == "user":
                        break
                break
        tmp = []
        tmp.append("")
        cd.data[i].value[ii].value = tmp
        i = -1
        ii = -1
        for e in cd.data:
            i = i + 1
            if e.keyName == "actiive_rule_set":
                ii = -1
                for ee in e.value:
                    ii = ii + 1
                    if ee.keyName == "rule":
                        break
                break

        tmp = []
        tmp.append("")
        cd.data[i].value[ii].value = tmp

        cd.writeTo()

        obj = Label(self.win, text="write userID", font=("Helvetica", 16))
        self.addObject(obj, 0, 5, 0, 0, True)

        obj = Combobox(self.win)
        self.cb0 = obj
        self.addObject(obj, 0, 3, 0, 0, True)

        obj = Button(win, text='Apply', command=self.setUserIDAndNext)
        self.addObject(obj, 0, 1, 0, 0, False)

    def initElementsAndLevels(self):
        elementsAndLevels = []
        return elementsAndLevels

    def addToElementsAndLevels(self, e):
        self.elementsAndLevels.append(e)

    def initLevels(self):
        levels = []
        return levels

    def addLevel(self, level):
        self.levels.append(level)

    def addObject(self, obj, marginStepsLeft, marginStepsRight, marginStepsUp, marginStepsDown,
                  booleanNewLineResetX):
        if booleanNewLineResetX:
            self.lp_x = self.lp_defaultStartX
            self.lp_y = self.lp_y + self.stepSize
        element = Element(obj, marginStepsLeft, marginStepsRight, marginStepsUp, marginStepsDown)
        x = self.lp_x + (marginStepsLeft * self.stepSize)
        y = self.lp_y + (marginStepsUp * self.stepSize)

        # update lp
        self.lp_x = x + (marginStepsRight * self.stepSize)
        self.lp_y = y + (marginStepsDown * self.stepSize)

        # place
        obj.place(x=x, y=y)

        # add element in some storage
        self.addToElementsAndLevels(element)

        print(len(self.elementsAndLevels))

    def addNewLevel(self, level):
        self.elementsAndLevels.append(level)
        self.levels.append(level)

    def changeToLevel(self, level):
        name = level.name
        nameListLevels = []
        level_index = -1
        for e in self.levels:
            level_index = level_index + 1
            nameListLevels.append(e.name)
            if name == e.name:
                break
        elementsAndLevels_index = -1
        for e in self.elementsAndLevels:
            elementsAndLevels_index = elementsAndLevels_index + 1
            try:
                if name == e.name:
                    break
            except:
                pass

        if (name in nameListLevels):
            size = len(self.elementsAndLevels)
            for ii in range(elementsAndLevels_index, size):
                try:
                    self.elementsAndLevels[ii].obj.place_forget()
                except:
                    pass
            self.elementsAndLevels = self.elementsAndLevels[0:elementsAndLevels_index + 1]
            self.levels = self.levels[0:level_index + 1]

            self.lp_x = level.x
            self.lp_y = level.y
        else:
            self.addNewLevel(level)

    # ---------------------------------------------------------------------------

    def setUserIDAndNext(self):
        level = Level(self.levels, "level_setUserIDAndNext", self.lp_x, self.lp_y)
        self.changeToLevel(level)
        self.userID = self.cb0.get()
        str = "userID = " + self.userID
        obj = Label(self.win, text=str, font=("Helvetica", 16))
        self.addObject(obj, 0, 5, 0, 0, False)

        cd = ConfigData("config_new.toml")
        i = -1
        ii = -1
        for e in cd.data:
            i = i + 1
            if e.keyName == "userinfo":
                ii = -1
                for ee in e.value:
                    ii = ii + 1
                    if ee.keyName == "user":
                        break
                break

        cd.data[i].value[ii].value = self.userID
        cd.writeTo()

        obj = Label(self.win, text="choose complexity", font=("Helvetica", 16))
        self.addObject(obj, 0, 5, 0, 0, True)

        obj = Combobox(self.win, values=self.complexity, state="readonly")
        self.currentComplexity = obj
        self.addObject(obj, 0, 3, 0, 0, True)

        obj = Button(self.win, text='Apply', command=self.userComplexityFunction)
        self.addObject(obj, 0, 1, 0, 0, False)

    def userComplexityFunction(self):
        str = ""
        if self.userID == 0:
            str = "test_"
        elif self.userID == 1:
            str = "admin_"
        else:
            str = "user_"

        complexity = self.currentComplexity.get()
        str = "self." + str + complexity + "_function"

        eval(str)()

    def test_simple_function(self):
        pass

    def admin_simple_function(self):
        pass

    def user_simple_function(self):
        level = Level(self.levels, "level_user_simple_function", self.lp_x, self.lp_y)
        self.changeToLevel(level)

        obj = Label(self.win, text="rules", font=("Helvetica", 16))
        self.addObject(obj, 0, 2, 0, 0, True)

        obj = Button(self.win, text='update', command=self.user_simple_function)
        self.addObject(obj, 0, 2, 0, 0, False)

        rules_lst = []
        config_rules = toml.load("config_rules.toml")
        for e in config_rules.keys():
            rules_lst.append(e)
        rules_lst2 = []
        string = "rules_" + self.userID
        for e in rules_lst:
            if e.startswith(string, 0):
                rules_lst2.append(e)

        obj = Combobox(self.win, values=rules_lst2, state="readonly")
        self.cbRules = obj
        self.addObject(obj, 0, 3, 0, 0, True)

        obj = Button(self.win, text='delete', command=self.simpleDeleteFunction)
        self.addObject(obj, 0, 1, 0, 0, False)

        obj = Button(self.win, text='show/change', command=self.simpleShowCangeFunction)
        self.addObject(obj, 0, 2, 0, 0, False)

        obj = Button(self.win, text='copy to new', command=self.simpleCopyFunction)
        self.addObject(obj, 0, 2, 0, 0, False)

        obj = Button(self.win, text='new', command=self.simpleNewRuleSet)
        self.addObject(obj, 0, 1, 0, 0, False)

        obj = Button(self.win, text='activate', command=self.simpleActivateRuleFuction)
        self.addObject(obj, 0, 2, 0, 0, False)

        level = Level(self.levels, "level_user_simple_function_end", self.lp_x, self.lp_y)
        self.changeToLevel(level)

        tmp = toml.load("config_new.toml")
        active_rule = tmp["actiive_rule_set"]["rule"][0]
        str = "active rule now: " + active_rule
        obj = Label(self.win, text=str, font=("Helvetica", 16))
        self.addObject(obj, 0, 7, 0, 0, False)

    def simpleDeleteFunction(self):
        level = Level(self.levels, "level_user_simple_function_end", self.lp_x, self.lp_y)
        self.changeToLevel(level)

        self.preeSimpleDeleteFunction()

    def preeSimpleDeleteFunction(self):
        level = Level(self.levels, "level_preeSimpleDeleteFunction", self.lp_x, self.lp_y)
        self.changeToLevel(level)

        ruleSetName = self.cbRules.get()

        str = "are you sure you want to delete: " + ruleSetName
        obj = Label(self.win, text=str, font=("Helvetica", 16))
        self.addObject(obj, 0, 6, 0, 0, True)

        obj = Button(self.win, text='yes', command=self.deleteRuleSet)
        self.addObject(obj, 0, 1, 0, 0, True)

    def simpleCopyFunction(self):
        level = Level(self.levels, "level_user_simple_function_end", self.lp_x, self.lp_y)
        self.changeToLevel(level)

        self.preeSimpleCopyFunction()

    def preeSimpleCopyFunction(self):
        level = Level(self.levels, "level_preeSimpleCopyFunction", self.lp_x, self.lp_y)
        self.changeToLevel(level)

        obj = Label(self.win, text="write end of rule name for copied version", font=("Helvetica", 16))
        self.addObject(obj, 0, 7, 0, 0, True)

        lst = []
        obj = Combobox(self.win, values=lst)
        self.newCopiedRuleNameObj = obj
        self.addObject(obj, 0, 3, 0, 0, True)

        obj = Button(self.win, text='add', command=self.newCopiedRuleSetFunction)
        self.addObject(obj, 0, 1, 0, 0, False)

    def simpleShowCangeFunction(self):
        level = Level(self.levels, "level_user_simple_function_end", self.lp_x, self.lp_y)
        self.changeToLevel(level)

        self.preeSimpleShowCangeFunction()

    def preeSimpleShowCangeFunction(self):
        level = Level(self.levels, "level_preeSimpleShowCangeFunction", self.lp_x, self.lp_y)
        self.changeToLevel(level)

        obj = Label(self.win, text="showing rule, you may edit", font=("Helvetica", 16))
        self.addObject(obj, 0, 7, 0, 0, True)

    def simpleNewRuleSet(self):
        level = Level(self.levels, "level_user_simple_function_end", self.lp_x, self.lp_y)
        self.changeToLevel(level)

        self.preeSimpleNewRuleSet()

    def preeSimpleNewRuleSet(self):
        level = Level(self.levels, "level_preeSimpleNewRuleSet", self.lp_x, self.lp_y)
        self.changeToLevel(level)

        obj = Label(self.win, text="write end of new rule name", font=("Helvetica", 16))
        self.addObject(obj, 0, 7, 0, 0, True)

        lst = []
        obj = Combobox(self.win, values=lst)
        self.newRuleNameObj = obj
        self.addObject(obj, 0, 3, 0, 0, True)

        obj = Button(self.win, text='add', command=lambda: self.add_new_ruleSet(self.userID))
        self.addObject(obj, 0, 1, 0, 0, False)

    def simpleActivateRuleFuction(self):
        level = Level(self.levels, "level_user_simple_function_end", self.lp_x, self.lp_y)
        self.changeToLevel(level)

        self.preeSimpleActivateRuleFuction()

    def preeSimpleActivateRuleFuction(self):
        level = Level(self.levels, "level_preeSimpleActivateRuleFuction", self.lp_x, self.lp_y)
        self.changeToLevel(level)

        cd = ConfigData("config_new.toml")
        i = -1
        ii = -1
        for e in cd.data:
            i = i + 1
            if e.keyName == "actiive_rule_set":
                ii = -1
                for ee in e.value:
                    ii = ii + 1
                    if ee.keyName == "rule":
                        break
                break

        tmp = []
        tmp.append(self.cbRules.get())
        cd.data[i].value[ii].value = tmp
        cd.writeTo()

        tmp = toml.load("config_new.toml")
        active_rule = tmp["actiive_rule_set"]["rule"][0]
        str = "active rule now: " + active_rule
        obj = Label(self.win, text=str, font=("Helvetica", 16))
        self.addObject(obj, 0, 7, 0, 0, False)

    # ---------------------------------------------------------------------------

    def deleteRuleSet(self):
        level = Level(self.levels, "level_deleteRuleSet", self.lp_x, self.lp_y)
        self.changeToLevel(level)

        ruleSetName = self.cbRules.get()
        cd = ConfigData("config_rules.toml")
        i = -1
        booleanDeleted = False
        for e in cd.data:
            i = i + 1
            if e.keyName == ruleSetName:
                cd.data.pop(i)
                cd.writeTo()
                booleanDeleted = True
                break
        if booleanDeleted:
            str = "deleted rule: " + ruleSetName
            obj = Label(self.win, text=str, font=("Helvetica", 16))
            self.addObject(obj, 0, 7, 0, 0, False)

            cd = ConfigData("config_new.toml")
            i = -1
            ii = -1
            for e in cd.data:
                i = i + 1
                if e.keyName == "actiive_rule_set":
                    ii = -1
                    for ee in e.value:
                        ii = ii + 1
                        if ee.keyName == "rule":
                            break
                    break

            tmp = cd.data[i].value[ii].value[0]
            if tmp == ruleSetName:
                cd.data[i].value[ii].value[0] = ""
                cd.writeTo()
        else:
            str = "could not deleted rule: " + ruleSetName
            obj = Label(self.win, text=str, font=("Helvetica", 16))
            self.addObject(obj, 0, 7, 0, 0, False)

    def newCopiedRuleSetFunction(self):  # will only work if "last value" is a list (something like that)
        level = Level(self.levels, "level_newCopiedRuleSetFunction", self.lp_x, self.lp_y)
        self.changeToLevel(level)
        name = self.newCopiedRuleNameObj.get()
        ruleName = "rules_" + self.userID + "_" + name

        cd = ConfigData("config_rules.toml")
        if ruleName in cd.rules_lst:
            obj = Label(self.win, text="that rule already exist, change name", font=("Helvetica", 16))
            self.addObject(obj, 0, 7, 0, 0, False)
        else:
            ruleSetName = self.cbRules.get()
            a = KeyValue(ruleName, [])
            for e in cd.data:
                if e.keyName == ruleSetName:
                    a.value = e.value  # ops!!!!!!!!!!!!!!!!! this is only if you write directly back to the config and read from config
                    break

            cd.data.append(a)

            cd.writeTo()

            str = "new copied ruleSet was created: " + ruleName
            obj = Label(self.win, text=str, font=("Helvetica", 16))
            self.addObject(obj, 0, 7, 0, 0, False)

    def add_new_ruleSet(self, userID):
        level = Level(self.levels, "level_add_new_ruleSet", self.lp_x, self.lp_y)
        self.changeToLevel(level)
        name = self.newRuleNameObj.get()
        ruleName = "rules_" + userID + "_" + name

        cd = ConfigData("config_rules.toml")

        if ruleName in cd.rules_lst:
            obj = Label(self.win, text="that rule already exist, change name", font=("Helvetica", 16))
            self.addObject(obj, 0, 7, 0, 0, False)
        else:
            a = KeyValue(ruleName, [])
            for e in cd.rules_lst_content:
                aa = KeyValue(e, [])
                a.value.append(aa)
            cd.data.append(a)

            cd.writeTo()

            str = "new ruleSet was created: " + ruleName
            obj = Label(self.win, text=str, font=("Helvetica", 16))
            self.addObject(obj, 0, 7, 0, 0, False)


window = Tk()
mywin = MyWindow(window)
window.title('Hello Python')
window.geometry("700x700+10+20")
window.mainloop()
