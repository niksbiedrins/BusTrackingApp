from typing import Annotated
from fastapi import APIRouter, Query
from services.bustimes import get_bustimes_vehicle_info
from models.bustimes import VehicleInfo

router = APIRouter(tags=["stagecoach"])

@router.get("/api/bustimes/vehicle-info", response_model=list[VehicleInfo])
def vehicle_info(
        operator_code: Annotated[str, Query(min_length=1, max_length=5, pattern=r"^[a-zA-Z]+$")],
):
    return get_bustimes_vehicle_info(operator_code=operator_code)
