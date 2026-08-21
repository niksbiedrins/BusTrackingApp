from pydantic import BaseModel

class StagecoachVehicleTrackingInfo(BaseModel):
    fleet_number: int
    operator_code: str
    latitude: float
    longitude: float
    destination: str
    final_stop: str
    cancelled: bool