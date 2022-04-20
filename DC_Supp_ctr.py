from time import sleep
import pyvisa


def SelectDevice():

    rm = pyvisa.ResourceManager()

    if (len(rm.list_resources()) == 1):
        device = rm.open_resource(rm.list_resources()[0])
    else:
        num_of_res = 0
        for res in rm.list_resources:
            print(f"{num_of_res}. {res}")
        num_of_res = input("Select device (by num): ")
        device = rm.open_resource(rm.list_resources(num_of_res))
    return device


def DeviceInfo(device: pyvisa.resources.serial.SerialInstrument):
    print(device.query('*idn?'))


def SetOutputState(device: pyvisa.resources.serial.SerialInstrument):
    device.write('OUTPut:STATe ON')
    sleep(2)
    response = device.query('OUTPut:STATe ON?')
    print(f"Output State: {response}")


def SetVoltage(device: pyvisa.resources.serial.SerialInstrument):
    device.write(':VOLTage 2.0')
    sleep(2)
    response = device.query(':VOLTage?')
    print(f"Voltage: {response}")


def SetCurrent(device: pyvisa.resources.serial.SerialInstrument):
    device.write(':CURRent 2.0')
    sleep(2)
    response = device.query(':CURRent?')
    print(f"Current: {response}")


if __name__ == "__main__":
    supply = SelectDevice()
    # DeviceInfo(supply)
    # SetOutputState(supply)
    # SetVoltage(supply)
