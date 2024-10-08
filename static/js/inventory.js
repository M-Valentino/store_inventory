const populateInventoryTable = (inventoryList) => {
  let tbody = document.getElementById("inventoryList");
  inventoryList.map((product, index) => {
    let tr = document.createElement("tr");

    let tdNum = document.createElement("td");
    tdNum.textContent = index;
    tr.appendChild(tdNum);

    let tdName = document.createElement("td");
    tdName.textContent = product.name;
    tr.appendChild(tdName);

    let tdUPC = document.createElement("td");
    tdUPC.textContent = product.upc;
    tr.appendChild(tdUPC);

    let tdCount = document.createElement("td");
    tdCount.textContent = product.count;
    tr.appendChild(tdCount);

    tbody.appendChild(tr);
  });
};

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
    return json;
  } catch (e) {
    console.warn(e);
  }
};

const handleInventoryDisplay = async () => {
  const inventoryList = await fetchInventory();
  populateInventoryTable(inventoryList);
};

handleInventoryDisplay();