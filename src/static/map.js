import { getLiveTrackingData } from "./api.js";

const OPERATOR_CODE = "SBLB";
const UPDATE_BUS_MARKERS_SECONDS = 30;

// Map
const map = L.map("map").setView([57.2274, -2.534], 8);

// Init map
L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution:
    '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(map);

// Bus marker layer
const busLayer = L.layerGroup().addTo(map);

function getMarkerRotation(heading) {
  const numericHeading = Number(heading);

  if (!Number.isFinite(numericHeading)) {
    return 0;
  }

  const normalizedHeading = ((numericHeading % 360) + 360) % 360;

  return normalizedHeading < 180
    ? normalizedHeading - 90
    : normalizedHeading - 270;
}

// create bus icon
function createBusIcon(serviceNumber, heading) {
  const rotation = getMarkerRotation(heading);

  return L.divIcon({
    className: "bus-icon",
    html: `
      <div class="bus-marker" style="transform: rotate(${rotation}deg)">
        <span class="bus-marker-span">${serviceNumber}</span>
      </div>
    `,
    iconSize: [24, 16],
    iconAnchor: [12, 8],
  });
}

// Get tracking data
async function renderBusMarkers(operatorCode) {
  console.log("Updated locations!");

  const data = await getLiveTrackingData(operatorCode);

  // only clear once we have the new data
  busLayer.clearLayers();

  for (const bus of data) {
    let vehicleType;
    const electric = bus["electric"] ? "Electric" : "Diesel";

    // determine the type of bus
    if (bus["coach"]) {
      vehicleType = "Coach";
    } else if (bus["double_decker"]) {
      vehicleType = "Double decker";
    } else {
      vehicleType = "Single decker";
    }

    L.marker([bus.latitude, bus.longitude], {
      icon: createBusIcon(bus["service_number"], bus["heading"]),
    })
      .addTo(busLayer)
      .bindPopup(
        `
        <b>${bus["service_number"]} to ${bus["destination"] || bus["final_stop"]}</b><br>
        ${vehicleType}, ${electric}
        `,
      );
  }
}

// init render
renderBusMarkers("SBLB");

// Then update every 30 seconds
setInterval(
  () => renderBusMarkers(OPERATOR_CODE),
  UPDATE_BUS_MARKERS_SECONDS * 1000,
);
