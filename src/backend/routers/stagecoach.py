from typing import Annotated
from fastapi import APIRouter, Query
from services.stagecoach import get_stagecoach_vehicle_tracking_info
from models.stagecoach import StagecoachVehicleTrackingInfo

router = APIRouter(tags=["stagecoach"])

@router.get("/api/stagecoach/vehicle-tracking", response_model=list[StagecoachVehicleTrackingInfo])
def vehicle_tracking(
        operator_code: Annotated[str | None, Query(min_length=1, max_length=5, pattern=r"^[a-zA-Z]+$")] = None,
        fleet_number: Annotated[int | None, Query(ge=1)] = None,
):
    return get_stagecoach_vehicle_tracking_info(operator_code=operator_code, fleet_number=fleet_number)
