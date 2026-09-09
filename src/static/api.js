export async function getLiveTrackingData(operatorCode) {
  try {
    const params = new URLSearchParams({ operator_code: operatorCode });

    const response = await fetch(`/api/stagecoach/vehicle-tracking/?${params}`);

    if (!response.ok) {
      throw new Error(
        `Request failed: ${response.status} ${response.statusText}`,
      );
    }

    const data = await response.json();

    return data;
  } catch (error) {
    console.error(error);
  }
}
