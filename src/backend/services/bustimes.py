import json
import httpx
from pathlib import Path

BUSTIMES_API_URL = "https://bustimes.org/api/vehicles/"
PROJECT_ROOT = Path(__file__).resolve().parents[3]

CACHE_DIR = PROJECT_ROOT / ".cache"
CACHE_DIR.mkdir(exist_ok=True)

def get_bustimes_vehicle_info(
    operator_code: str,
):
    cache_file = CACHE_DIR / f"{operator_code}.json"

    # If cache file exists for that operator_code return it.
    if cache_file.exists():
        print("Cache file found. Returning cached result.")
        with open(cache_file, "r") as file:
            return json.load(file)
    else:
        print("Cache file not found.")

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

        vehicles = [
            {
                "operatorCode": vehicle["operator"]["id"],
                "fleetNumber": int(vehicle["fleet_number"]),
                "double_decker": bool(vehicle["vehicle_type"]["double_decker"]) if vehicle["vehicle_type"] else False,
                "coach": bool(vehicle["vehicle_type"]["coach"]) if vehicle["vehicle_type"] else False,
                "electric": bool(vehicle["vehicle_type"]["electric"]) if vehicle["vehicle_type"] else False,
            }
            for vehicle in vehicles
        ]

        # Update cache
        with cache_file.open("w") as file:
            print("Updated cache.")
            json.dump(vehicles, file, indent=4)

        return vehicles

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