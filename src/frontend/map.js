import { getLiveTrackingData } from "./api.js";

// Map
const map = L.map("map").setView([57.2274, -2.534], 8);

// Init map
L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution:
    '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(map);

// Get tracking data
async function renderBusMarkers(operatorCode) {
  const data = await getLiveTrackingData(operatorCode);

  for (const bus of data) {
    let vehicleType;
    const electric = bus["electric"] ? "Electric" : "Diesel";

    if (bus["coach"]) {
      vehicleType = "Coach";
    } else if (bus["double_decker"]) {
      vehicleType = "Double decker";
    } else {
      vehicleType = "Single decker";
    }

    L.marker([bus.latitude, bus.longitude])
      .addTo(map)
      .bindPopup(
        `
        <b>${bus["service_number"]} to ${bus["destination"] || bus["final_stop"]}</b><br>
        ${vehicleType}, ${electric}
        `,
      );
  }
}

// init rendering
renderBusMarkers("SBLB");
