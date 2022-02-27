# USB History Logger
# Reg Path reference: winreg.HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\USBSTOR

import winreg

registryConnection = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
keyInfo = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\\CurrentControlSet\\Enum\\USBSTOR")
keyValue = winreg.QueryInfoKey(keyInfo)
numberOfKeys = 0

usbHistoryFile = open('USB_History.txt', 'a')

# Prints first subkey. Skipped in loop due to index of 0.

firstSubKey = winreg.EnumKey(keyInfo, 0)
usbHistoryFile.write(str(firstSubKey) + "\n")
print(firstSubKey)

# Print subkeys

while True:
        try:
            numberOfKeys += 1
            subKey = winreg.EnumKey(keyInfo, numberOfKeys)
            # prints USB history subkeys
            for i in range (numberOfKeys):
                print(subKey)
                usbHistoryFile.write(str(subKey) + "\n")
                break
        except WindowsError:
            break
        
winreg.CloseKey(registryConnection)
