const fetchInventory = async () => {
  try {
    const response = await fetch("/inventory", {
      method: "GET",
    });
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    const json = await response.json();
    console.log(json);
  } catch (e) {
    console.warn(e);
  }
};

fetchInventory();