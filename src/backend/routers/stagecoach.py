from typing import Annotated
from fastapi import APIRouter, Query

from typing import Iterable

from services.stagecoach import get_stagecoach_vehicle_tracking_info
from services.bustimes import get_bustimes_vehicle_info

from models.stagecoach import StagecoachVehicleTrackingInfo
from models.bustimes import VehicleInfo

router = APIRouter(tags=["stagecoach"])

@router.get("/api/stagecoach/vehicle-tracking", response_model=list[StagecoachVehicleTrackingInfo])
def vehicle_tracking(
        operator_code: Annotated[str, Query(min_length=1, max_length=5, pattern=r"^[a-zA-Z]+$")],
        fleet_number: Annotated[int | None, Query(ge=1)] = None,
):
    bustimes_vehicle_info = get_bustimes_vehicle_info(operator_code=operator_code)
    stagecoach_vehicle_tracking_info = get_stagecoach_vehicle_tracking_info(operator_code=operator_code, fleet_number=fleet_number)

    # Check if we fetched the functions
    if bustimes_vehicle_info is not None:
        print("Fetcehd get_bustimes_vehicle_info() successfully")

    if stagecoach_vehicle_tracking_info is not None:
        print("Fetched stagecoach vehicle tracking_info() successfully")

    to_return = []

    # Combine both list of dictionaries into one dictionary
    for service in stagecoach_vehicle_tracking_info:
        for vehicle in bustimes_vehicle_info:

            if service["fleet_number"] == vehicle["fleet_number"]:
                to_return.append({
                    **service,
                    **vehicle,
                })

    return to_return