import httpx

# Stagecoach vehicle tracking API link
STAGECOACH_API_URL = "https://api.stagecoach-technology.net/vehicle-tracking/v1/vehicles/"

def get_stagecoach_vehicle_tracking_info(
        operator_code: str | None = None,
        fleet_number: int | None = None,
):
    try:
        response = httpx.get(STAGECOACH_API_URL, params={"services": ":*:::"}, timeout=5)
        response.raise_for_status()

        data = response.json()

        vehicles =  [
            {
                "fleet_number": int(service["fn"]),
                "operator_code": service["oc"],
                "latitude": float(service["la"]),
                "longitude": float(service["lo"]),
                "destination": service["dd"],
                "final_stop": service["fs"],
                "cancelled": bool(service["cd"]),
            }
            for service in data["services"]
        ]

        # If operator_code is provided, filter vehicles by operator code
        if operator_code is not None:
            vehicles = [
                vehicle for vehicle in vehicles
                if vehicle["operator_code"] == operator_code
            ]

        # If fleet_number is provided, filter vehicles by fleet_number
        if fleet_number is not None:
            vehicles = [
                vehicle for vehicle in vehicles
                if vehicle["fleet_number"] == fleet_number
            ]

        return vehicles

    except httpx.TimeoutException:
        print("Stagecoach API timed out.")
        return None
    except httpx.ConnectError:
        print("Could not connect to Stagecoach API")
        return None
    except httpx.HTTPStatusError as error:
        print(f"Stagecoach API returned HTTP {error.response.status_code}")
        return None

    except httpx.RequestError as error:
        print(f"Stagecoach API request failed: {error}")
        return None