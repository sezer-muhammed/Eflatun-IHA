from dronekit import *
import time
import typing


class UAVMovementCommand():
    def __init__(self) -> None:
        pass


class UAVMovementCommandYAW(UAVMovementCommand):
    def __init__(self) -> None:
        super().__init__()


class UAVMovementCommandPITCH(UAVMovementCommand):
    def __init__(self) -> None:
        super().__init__()


class UAVMovementCommandROLL(UAVMovementCommand):
    def __init__(self) -> None:
        super().__init__()


class UAVMovementCommandSPEED(UAVMovementCommand):
    def __init__(self) -> None:
        super().__init__()


class UAVMovementCommandALTITUDE(UAVMovementCommand):
    def __init__(self) -> None:
        super().__init__()


class UAVMovementCommandSERVO(UAVMovementCommand):
    def __init__(self) -> None:
        super().__init__()


class EflatunUAV():
    def __init__(self, port, baudrate, wait_ready=True) -> None:
        self.vehicle = connect(ip=port, baud=baudrate, wait_ready=wait_ready)

    def summary() -> str:
        return NotImplementedError

    def arm() -> bool:
        return NotImplementedError

    def takeoff() -> float:
        return NotImplementedError

    def land() -> bool:
        return NotImplementedError

    def send_command(UAVMovementCommand: UAVMovementCommand) -> bool:
        return NotImplementedError
