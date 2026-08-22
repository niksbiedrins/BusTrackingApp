import httpx

BUSTIMES_API_URL = "https://bustimes.org/api/vehicles/"


def get_bustimes_vehicle_info(
    operator_code: str,
    fleet_number: int | None = None
):
    params = {
        "operator": operator_code
    }

    try:
        vehicles = []
        first_request = True
        next_link = BUSTIMES_API_URL

        while next_link:
            if first_request:
                response = httpx.get(next_link, params=params, timeout=5)
                first_request = False
            else:
                response = httpx.get(next_link, timeout=5)

            response.raise_for_status()

            data = response.json()
            vehicles.extend(data["results"])

            next_link = data["next"]

        # Filter fleet number, if provided
        if fleet_number is not None:
            vehicles = [
                vehicle
                for vehicle in vehicles
                if vehicle.get("fleet_number") == fleet_number
            ]

        return [
            {
                "operatorCode": vehicle["operator"]["id"],
                "fleetNumber": int(vehicle["fleet_number"]),
                "double_decker": bool(vehicle["vehicle_type"]["double_decker"]) if vehicle["vehicle_type"] else False,
                "coach": bool(vehicle["vehicle_type"]["coach"]) if vehicle["vehicle_type"] else False,
                "electric": bool(vehicle["vehicle_type"]["electric"]) if vehicle["vehicle_type"] else False,
            }
            for vehicle in vehicles
        ]

    except httpx.TimeoutException:
        print("Bustimes API timed out.")
        return None

    except httpx.ConnectError:
        print("Could not connect to Bustimes API")
        return None

    except httpx.HTTPStatusError as error:
        print(
            f"Bustimes API returned HTTP "
            f"{error.response.status_code}"
        )
        return None

    except httpx.RequestError as error:
        print(f"Bustimes API request failed: {error}")
        return None
