import ctypes
import platform
if platform.system() == "Windows":
    d=ctypes.CDLL("./bin/logjam64.dll")
elif platform.system() == "Linux":
    d=ctypes.CDLL("./bin/logjam64.so")
elif platform.system() == "Darwin":
    d=ctypes.CDLL("./bin/logjam64.dylib")
print(d.LogMessage("This is a Test of the Logging Function".encode('ascii')))
print(d.LogMessage("This is also a Test of the Logging Function".encode('ascii')))
print(d.LogMessage("This is also a Test of the Logging Function".encode('ascii')))
print(d.LogMessage("This is also a Test of the Logging Function".encode('ascii')))
print(d.LogMessage("This is also a Test of the Logging Function".encode('ascii')))
print(d.LogMessage("This is also a Test of the Logging Function".encode('ascii')))
print(d.LogMessage("This is also a Test of the Logging Function".encode('ascii')))


