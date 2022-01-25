import toml

from Input.WidefindInput import WideFind
from fiblary3.client import Client


def main():

    config = toml.load("config.toml")

    # use config file-----------------------------------------------------------------------
    if config["useWideFind"]:
        print("Using WideFind")
        # widefind = WideFind("130.240.74.55", 1883)

    if config["usingFibaro"]:
        print("Using Fibaro")
        # fibaro = Fibaro("ip")


    # get sesor data -----------------------------------------------------------------------


    # modifiy sensor data and "send" on standard way


    # get standard data and "tolka" kanske skika vidare utan att tolka

    # read some config file to connect input id and output id





if __name__ == '__main__':
    main()
