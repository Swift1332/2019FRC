from wpilib.interfaces import PIDSource


class SwiftCanEncoder(PIDSource):
    def __init__(self, canEncoder):
        self.sourceType = PIDSource.PIDSourceType.kDisplacement
        self._encoder = canEncoder
        
    def setPIDSourceType(self, pidSource: PIDSource.PIDSourceType) -> None:
        self.sourceType = pidSource
    
    def getPIDSourceType(self) -> PIDSource.PIDSourceType:
        return self.sourceType

    def pidGet(self) -> float:
        return self.get() * 1.0
    
    def reset(self) -> None:
        # TODO handle CAN errors        
        self._encoder.setPosition(0.0)

    def get(self) -> int:
        if self.sourceType == PIDSource.PIDSourceType.kDisplacement:
            return self._encoder.getPosition()
        elif self.sourceType == PIDSource.PIDSourceType.kRate:
            return self._encoder.getVelocity()

    def setReverseDirection(self, reverseDirection: bool) -> None:
        self._encoder._inverted = bool

    def  getDirection(self) -> bool:
        v = self._encoder.getVelocity()
        if v == abs(v):
            return True
        return False

    def getRate(self) -> float:
        return self._encoder.getVelocity()

    def getDistance(self) -> float:
        return self._encoder.getPosition() * 1.0

    def setDistancePerPulse(self, distancePerPulse: float) -> None:
        self._encoder.setPositionConversionFactor(distancePerPulse)
        self._encoder.setVelocityConversionFactor(distancePerPulse)

    def getDistancePerPulse(self) -> float:
        if self.sourceType == PIDSource.PIDSourceType.kDisplacement:
            return self._encoder.getPositionConversionFactor()
        elif self.sourceType == PIDSource.PIDSourceType.kRate:
            return self._encoder.getVelocityConversionFactor()

    def setPosition(self, position) -> float:
        self._encoder.setPosition(position)




