# D0020E - Rule-based activity recognition

This project is a part of the course D0020E at Luleå University of Technology.

The purpose of the project is to provide a configurable system for setting up rules for activity recognition
in the Human Health and Activity Laboratory (H2Al) at LTU. H2Al is like a smart home containing multiple different
sensors and tools, and it is used for e.g. studying human behaviour. The lab is currently lacking a system that
easily connects different types of sensors and this project aims to meet that need.

***

## Input

### WideFind

WideFind is a swedish positional system developed in Luleå. The system uses reference points to
track a wireless receiver in a room. In this project we use vectors to measure the distance between the receiver and
different objects in order to approximate where in the lab a receiver is located.

### Z-Wave (Fibaro Home Center 3)

In the lab, Z-Wave sensors are found in e.g. doors and cabinets. They hold their internal state which in the case
of a door says if it's open or closed. The sensors are configured with a Fibaro Home Center 3 hub which is where
information is gathered from. There are many other sensors configured with Fibaro (such as thermometers,
moisture meters, power sockets etc.), but we have only managed to get the doors working.

***

## Output

### Philips Hue

Philips Hue is a smart lighting system with highly configurable light bulbs. By connecting to a bridge it is possible
to change the brightness and color of the light bulbs via programming. 

### Discord 

Discord has built in support for webhooks which lets one write in a server channel. By connecting to the webhook
it is possible to send messages to a Discord server.

***

## Installation and use

_To be added_

***

## Adding new input

_To be added_

***

## Adding new output

_To be added_
