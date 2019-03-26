# notrack
from typing import Optional

import hal
import subprocess
import threading

import logging

logger = logging.getLogger("wpilib.cs")

__all__ = ["SwiftCameraServer"]


class SwiftCameraServer:

    def __init__(self):
        self._alive = False
        self._launched = False

    """
        Provides a way to launch an out of process cscore-based camera
        service instance, for streaming or for image processing.
        
        .. note:: This does not correspond directly to the wpilib
                  CameraServer object; that can be found as
                  :class:`cscore.CameraServer`. However, you should
                  not use cscore directly from your robot code, see
                  the documentation for details             
    """

    def is_alive(self) -> bool:
        """:returns: True if the CameraServer is still alive"""
        return self._alive

    def launch(self, vision_py: Optional[str] = None) -> None:
        """
            Launches the CameraServer process in autocapture mode or
            using a user-specified python script
        
            :param vision_py: If specified, this is the relative path to
                              a filename with a function in it
                              
            Example usage::
            
                wpilib.CameraServer.launch("vision.py:main")
            
            .. warning:: You must have robotpy-cscore installed, or this
                         function will fail without returning an error
                         (you will see an error in the console).
                         
        """

        if self._launched:
            return

        self._launched = True

        if hal.isSimulation():
            logger.info("Would launch CameraServer with vision_py=%s", vision_py)
            self._alive = True
        else:
            logger.info("Launching CameraServer process")

            # Launch the cscore launcher in a separate process
            import sys

            args = [sys.executable, "-m", "cscore"]

            # TODO: Get accurate reporting data from the other cscore process. For
            # now, just differentiate between users with a custom py file and those
            # who do not. cscore handle values indicate type with bits 24-30

            if vision_py:
                if not vision_py.startswith("/"):
                    vision_py = "/home/lvuser/py/" + vision_py
                args.append(vision_py)
                hal.report(hal.UsageReporting.kResourceType_PCVideoServer, 0x51)
            else:
                hal.report(hal.UsageReporting.kResourceType_PCVideoServer, 0x52)

            # We open a pipe to it so that when this process exits, it dies
            proc = subprocess.Popen(
                args, close_fds=True, stdin=subprocess.PIPE, cwd="/home/lvuser/py"
            )
            th = threading.Thread(target=self._monitor_child, args=(proc,))
            th.daemon = True
            th.start()

    def _monitor_child(self, proc: subprocess.Popen) -> None:
        proc.wait()
        logger.warning("CameraServer process exited with exitcode %s", proc.returncode)
        self._alive = False
