## Rule-Based Activity Recognition

This project aims to provide rule-based activity recognition by using different sensors in the smart home environment called [Human Health and Activity Laboratory (H2Al)](https://www.researchgate.net/publication/328472171_H2Al-The_Human_Health_and_Activity_Laboratory) at [Luleå University of Technology (LTU)](https://www.ltu.se/). The project also aims to provide a way to easily connect different types of sensor data in the lab.

Rule-based activity recognition means to have a set of rules, which can be either true or false, and let them define a certain human behaviour. A rule-based scenario could for example look like this:

If
- a person is in the kitchen,
- the fridge has been opened recently, 
- and the stove is currently on.

Then
- assume that a person is currently preparing food.

A scenario could be a lot simpler or a lot more complex than this.

## Table of Contents

- [Currently Supported Input](#currently_supported_input)
  - [WideFind](#widefind)
  - [Z-Wave (Fibaro)](#z-wave)
  - [Simulator](#simulator)
- [Currently Supported Output](#currently_supported_output)
  - [Philips Hue](#philips_hue)
  - [Discord](#discord)
- [Installation](#installation)
  - [Creating the Config File](#creating_the_config_file)
- [Running the Application](#running_the_application)
- [System Architecture](#system_architecture)
- [Adding New Input](#add_input)
- [Adding New Output](#add_output)

## <a name="currently_supported_input"></a>Currently Supported Input

H2Al contains a number of different sensors which can provide input data for the rules. The are more sensors in the lab than the ones listed below, and we have tried to make it as easy as possible for a programmer to add new input sensors. This process is explained in the section [Adding New Input](#add_input). Input data is not restricted to only the type of sensor data found in the lab.

### <a name="widefind"></a>WideFind

WideFind is a swedish positional system developed in Luleå. The system uses reference points to track a wireless receiver in a room. In this project we use vectors to measure the distance between the receiver and different objects in order to approximate where in the lab a receiver is located.

### <a name="z-wave"></a>Z-Wave (Fibaro)

In H2Al, Z-Wave sensors are found in e.g. doors and cabinets. Door sensors hold an internal states which says if the door is open or closed. The sensors are configured with a Fibaro Home Center 3 hub. Data, such as states, can be gathered from the Fibaro hub. We have not managed to make Fibaro send events when a state is changed so instead we use a thread which simulates an event once per second by gathering and forwarding the internal states. There are many other sensors configured with Fibaro (such as thermometers, moisture meters, power sockets etc.), but we have only managed to make the door and cabinet sensors work.

### <a name="simulator"></a>Simulator

A simulator is provided for simulating a simple scenario. The simulator sends "fake" Z-Wave and WideFind data to the application and it can be used to test functionality. By changing the `Simulator.py` class it is possible to change to simulated events to one's liking. The simulator executes in its own thread.

## <a name="currently_supported_output"></a>Currently Supported Output

Some gadgets in the lab can be used as output for a rule if we not only want to recognice a certain activity, but also have something happen during that activity. The processes of adding new output is explained in the section [Adding New Output](#add_output). An output could be virtually anything and is not restricted to be something in the lab.

### <a name="philips_hue"></a>Philips Hue

Philips Hue is a smart lighting system with highly configurable light bulbs. By connecting to a bridge it is possible to change the brightness and color of a light bulb.

### <a name="discord"></a>Discord

By creating a webhook in a Discord server and connecting to that webhook it is possible to send messages to the server. This could be used to receive live updates from the lab while not being present there.

## <a name="installation"></a>Installation

- Clone the main branch of the project repository or download it as a Zip
- Create a file called `config.toml` in the root directory (see [Creating the Config File](#creating_the_config_file))
- On Windows:
  - Run `D0020E_Interface.exe`
- On other operating systems:
  - Download [Godot Engine](https://godotengine.org/) and use it to open the project file `project.godot`
  - Compile the project for your operating system

### <a name="creating_the_config_file"></a>Creating the Config File

In order for the application to connect to the different sensors and gadgets, it is necessary to create a config file in the application root directory and call it `config.toml`. This file must look exactly like this:

```markdown
[widefind]
enabled = true
ip = "..."
port = ...

[fibaro]
enabled = true
ip = "http://.../api/"
user = "..."
password = "..."

[phue]
enabled = true
ip = "..."

[discord]
enabled = true
url = "..."
```

Replace the dots with the necessary information. When adding new input or output functionality it is recommended to add connection information, such as ip addresses or URL:s, to the `config.toml` in the same way as shown above and then read the information to the main application. This should be done to keep sensitive information from being displayed in the application itself. Full tutorials for adding input and output can be found in sections [Adding New Input](#add_input) and [Adding New Output](#add_output).

## <a name="running_the_application"></a>Running the Application

When starting `D0020E_Interface.exe` the user will be presented with three choices: `USER`, `TEST` and `ADMIN`. No rulesets are defined when starting for the first time so press `USER` and then `Add New` to make new rules. Name your ruleset to `rule_#`, replacing the hash with any text. Then choose desired input and desired output for a rule. Input and ouput can be combined in any manner. Press `Save` to save this rule to the specified ruleset. If you want to add more rules to this set, choose the newly created ruleset, choose input and output and press save again. Add as many rules as you like. If `discord_0_send` is chosen you will have to write a message to send to the Discord webhook in the box `OutPut Argument for General`.

See `EXPLANATIONS.toml` for mapping between ID and physical object. Door 42 is for example the front door to H2Al. `EXPLANATIONS.toml` should also be updated when new input or output is added to make it clear which ID corresponds to which object.

Press the cogwheel to go back and press `USER` again to see all created rulesets. Choose your ruleset and press `Run Selected Rule` to start the application for the selected ruleset. Press `Stop Selected Rule` to stop the application. Rulesets can be changed and removed.

If you want to run a simulator in order to test a specific ruleset, go to the start menu and choose `TEST`. Choose the ruleset you want to test and press `Run Simulator` to start the simulation. The simulator's default configuration is to send Z-Wave door and WideFind position updates for about a minute. The simuator can be edited by changing the messages in the file `/Input/Simulator.py`.

The `ADMIN` panel currently doesn't let you do anything special. Here you can also modify rulesets like on the `USER` panel and the plan is to expand it sometime in the future.

## <a name="system_architecture"></a>System Architecture

The class diagram below presents an overview of the system architecture.

![Image](/img/structure.png)

When running the program `D0020E_Interface.exe` it reads all defined input and output from `documentation.toml`. When rulesets are created in the application they are saved to `config_rules.toml`. This file is then read by the `Main` object when starting the program, since it contains the rules for this run. Upon starting a run, the `Main` and `Output` objects also read the file `config.toml` which contains necessary setup information.

## <a name="add_input"></a>Adding New Input

These last two sections are intended for administrators and those who have some programming knowledge as they involve changing the source code and thereby the program structure.

## <a name="add_output"></a>Adding New Output

_To be added_
