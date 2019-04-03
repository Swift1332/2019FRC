from cscore import CameraServer

def main():
    cs = CameraServer.getInstance()
    cs.startAutomaticCapture(dev=0)
    cs.waitForever()