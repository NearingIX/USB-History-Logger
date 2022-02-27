# USB History Logger
# Reg Path reference: winreg.HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\USBSTOR

import winreg

registryConnection = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
keyInfo = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\\CurrentControlSet\\Enum\\USBSTOR")
numberOfKeys = 0

# Prints first subkey. Skipped in loop due to index of 0.

def printFirstSubKey():
    firstSubKey = winreg.EnumKey(keyInfo, 0)
    usbHistoryFile = open('USB_History.txt', 'a')
    usbHistoryFile.write(str(firstSubKey) + "\n")
    print(firstSubKey)

# Print subkeys
def printSubKey():
    while True:
        try:
            global numberOfKeys, i, keyInfo, registryConnection
            numberOfKeys += 1
            usbHistoryFile = open('USB_History.txt', 'a')
            subKey = winreg.EnumKey(keyInfo, numberOfKeys)
            # openSubKey = winreg.OpenKey(keyInfo, subKey)
            # prints USB history subkeys
            for i in range (numberOfKeys):
                print(subKey)
                usbHistoryFile.write(str(subKey) + "\n")
                break
        except WindowsError:
            break

printFirstSubKey()           
printSubKey()
winreg.CloseKey(registryConnection)
