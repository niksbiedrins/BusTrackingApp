from fastapi import APIRouter
from services.stagecoach import get_stagecoach_vehicle_tracking_info

router = APIRouter()

@router.get("/api/stagecoach/vehicle-tracking")
def vehicle_tracking(
        operator_code: str | None = None,
        fleet_number: int | None = None
):
    return get_stagecoach_vehicle_tracking_info(operator_code=operator_code, fleet_number=fleet_number)
