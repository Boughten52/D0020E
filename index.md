## Introduction

This project aims to provide rule-based activity recognition by using different sensors in the smart home environment called [Human Health and Activity Laboratory (H2Al)](https://www.researchgate.net/publication/328472171_H2Al-The_Human_Health_and_Activity_Laboratory) at [Luleå University of Technology (LTU)](https://www.ltu.se/). The project also aims to provide a way to easily connect different types of sensor data in the lab.

Rule-based activity recognition means to have a set of rules, which can be either true or false, and let them define a certain human behaviour. A rule-based scenario could for example look like this:

If
- a person is in the kitchen,
- the fridge has been opened recently, 
- and the stove is currently on.

Then
- assume that a person is currently preparing food.

A scenario could be a lot simpler or a lot more complex than this.

## Currently Supported Input

H2Al contains a number of different sensors which can provide input data for the rules. The are more sensors in the lab than the ones listed below, and we have tried to make it as easy as possible for a programmer to add new input sensors. This process is explained in the section [Adding New Input](#add_input). Input data is not restricted to only the type of sensor data found in the lab.

### WideFind

WideFind is a swedish positional system developed in Luleå. The system uses reference points to track a wireless receiver in a room. In this project we use vectors to measure the distance between the receiver and different objects in order to approximate where in the lab a receiver is located.

### Z-Wave (Fibaro)

In H2Al, Z-Wave sensors are found in e.g. doors and cabinets. Door sensors hold an internal states which says if the door is open or closed. The sensors are configured with a Fibaro Home Center 3 hub. Data, such as states, can be gathered from the Fibaro hub. We have not managed to make Fibaro send events when a state is changed so instead we use a thread which simulates an event once per second by gathering and forwarding the internal states. There are many other sensors configured with Fibaro (such as thermometers, moisture meters, power sockets etc.), but we have only managed to make the door and cabinet sensors work.

### Simulator

A simulator is provided for simulating a simple scenario. The simulator sends "fake" Z-Wave and WideFind data to the application and it can be used to test functionality. By changing the `Simulator.py` class it is possible to change to simulated events to one's liking. The simulator executes in its own thread.

## Currently Supported Output

Some gadgets in the lab can be used as output for a rule if we not only want to recognice a certain activity, but also have something happen during that activity. The processes of adding new output is explained in the section [Adding New Output](#add_output). An output could be virtually anything and is not restricted to be something in the lab.

### Philips Hue

Philips Hue is a smart lighting system with highly configurable light bulbs. By connecting to a bridge it is possible to change the brightness and color of a light bulb.

### Discord

By creating a webhook in a Discord server and connecting to that webhook it is possible to send messages to the server. This could be used to receive live updates from the lab while not being present there.

## Installation

_To be added_

### Creating the Config File

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

## Running the Application

_To be added_

## System Architecture

We provide a simplified class diagram for visualizing the overall structure of the application. Methods and attributes are not presented here.

![Image](/img/structure.drawio.png)

## <a name="add_input"></a>Adding New Input

_To be added_

## <a name="add_output"></a>Adding New Output

_To be added_

## Syntax Reference (remove later)

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```
