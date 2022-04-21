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


def SetOutputState(device: pyvisa.resources.serial.SerialInstrument,  state: bool):
    device.write('OUTPut:STATe ' + str(state))
    sleep(2)
    response = device.query('OUTPut:STATe?')
    print(f"Output State: {response}")


def SetVoltage(device: pyvisa.resources.serial.SerialInstrument, Volt: float):
    device.write(':VOLTage ' + str(Volt))
    sleep(2)
    response = device.query(':VOLTage?')
    print(f"Voltage: {response}")


def SetCurrent(device: pyvisa.resources.serial.SerialInstrument, Curr: float) -> None:
    device.write(':CURRent '+str(Curr))
    sleep(2)
    response = device.query(':CURRent?')
    print(f"Current: {response}")


def GetCurrent(device: pyvisa.resources.serial.SerialInstrument) -> float:
    response = device.query(':CURRent?')
    return response


def GetVoltage(device: pyvisa.resources.serial.SerialInstrument) -> float:
    response = device.query(':VOLTage?')
    return response


def stairs(device: pyvisa.resources.serial.SerialInstrument):
    for i in range(5):
        SetVoltage(device, i)
        sleep(2)


if __name__ == "__main__":
    supply = SelectDevice()
    DeviceInfo(supply)
    SetOutputState(supply, 1)
    SetVoltage(supply, 2.0)
    stairs(supply)
