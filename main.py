import toml

from Input.Fibaro import Fibaro
from Input.WidefindInput import WideFind
from fiblary3.client import Client


def main():

    config = toml.load("config.toml")

    # use config file-----------------------------------------------------------------------
    if config["widefind"]["enabled"]:
        print("Using WideFind")
        widefind = WideFind(config["widefind"]["ip"], config["widefind"]["port"])
        widefind.run()

    if config["fibaro"]["enabled"]:
        print("Using Fibaro")
        fibaro = Fibaro(config["fibaro"]["ip"], config["fibaro"]["user"], config["fibaro"]["password"])

        print("Open doors:")
        for device in fibaro.getOpenDoors():
            print(device.id, device.name)

    # get sesor data -----------------------------------------------------------------------


    # modifiy sensor data and "send" on standard way


    # get standard data and "tolka" kanske skika vidare utan att tolka

    # read some config file to connect input id and output id





if __name__ == '__main__':
    main()
