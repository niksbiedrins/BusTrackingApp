from pydantic import BaseModel


class StagecoachVehicleTrackingInfo(BaseModel):
    fleet_number: int
    service_number: str
    operator_code: str
    latitude: float
    longitude: float
    destination: str
    final_stop: str
    cancelled: bool
    operator_code: str
    fleet_number: int
    double_decker: bool
    coach: bool
    electric: bool
