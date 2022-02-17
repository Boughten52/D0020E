import toml
import requests
from Output.Phue import Phue
from discord import Webhook, RequestsWebhookAdapter


class Output:

    def __init__(self):
        config = toml.load("config.toml")

        # -------- INSTANTIATE PHUE -------- #
        if config["phue"]["enabled"]:
            global phue
            phue = Phue(config["phue"]["ip"])
            print("Philips hue connected")

        # -------- INSTANTIATE DISCORD -------- #
        if config["discord"]["enabled"]:
            global webhook
            webhook = Webhook.from_url(config["discord"]["url"], adapter=RequestsWebhookAdapter())

    def lamps(self, output_argument):
        message = output_argument.split("_")
        name = message[0]
        id = int(message[1])
        action = message[2]
        if name == "lamp":
            if action == "on":
                phue.light_on(id)
                # print("Light " + str(id) + " on")
            if action == "off":
                phue.light_off(id)
                # print("Light " + str(id) + " off")
            if action == "green":
                phue.change_light(255, 0, 0, id)
                # print("Light " + str(id) + " yellow")
            if action == "purple":
                phue.change_light(255, 0, 255, id)
                # print("Light " + str(id) + " purple")
            if action == "blue":
                phue.change_light(0, 0, 255, id)
                # print("Light " + str(id) + " blue")
            if action == "disco":
                phue.disco(id)
                # print("Light " + str(id) + " disco")

    def discord(self, output_argument):
        message = output_argument
        webhook.send(message)

