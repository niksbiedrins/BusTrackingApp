from pydantic import BaseModel

class VehicleInfo(BaseModel):
    operator_code: str
    fleet_number: int
    double_decker: bool
    coach: bool
    electric: bool