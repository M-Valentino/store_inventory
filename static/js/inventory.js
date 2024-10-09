const populateInventoryTable = (inventoryList) => {
  let tbody = document.getElementById("inventoryList");
  tbody.innerHTML = "";

  inventoryList.map((product, index) => {
    let tr = document.createElement("tr");

    let tdNum = document.createElement("td");
    tdNum.textContent = index + 1;
    tr.appendChild(tdNum);

    let tdName = document.createElement("td");
    tdName.textContent = product.name;
    tr.appendChild(tdName);

    let tdCategory = document.createElement("td");
    tdCategory.textContent = product.category;
    tr.appendChild(tdCategory);

    let tdUPC = document.createElement("td");
    tdUPC.textContent = product.upc;
    tr.appendChild(tdUPC);

    let tdQty = document.createElement("td");
    tdQty.textContent = product.qty;
    tr.appendChild(tdQty);

    tbody.appendChild(tr);
  });
};

const fetchInventory = async (categories, searchTerm) => {
  try {
    const params = new URLSearchParams();
    if (categories.length > 0) {
      params.append("category", categories.join(","));
    }

    params.append("search", searchTerm);

    const response = await fetch(`/inventory?${params.toString()}`, {
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

const getCheckedCategories = () => {
  const checkboxes = document.querySelectorAll('input[name="category"]');
  const checkedCategories = [];

  checkboxes.forEach((checkbox) => {
    if (checkbox.checked) {
      checkedCategories.push(checkbox.value);
    }
  });

  console.log("Checked Categories: " + checkedCategories.join(", "));
  return checkedCategories;
};

function debounce(func, delay) {
  let timeout;
  return function (...args) {
    const context = this;
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(context, args), delay);
  };
}

const getSearchTerm = () => {
  const searchTerm = document.getElementById("searchInput").value;
  return searchTerm || "";
};

const handleInventoryDisplay = async () => {
  const searchTerm = getSearchTerm();
  const checkedCategories = getCheckedCategories();
  const inventoryList = await fetchInventory(checkedCategories, searchTerm);
  populateInventoryTable(inventoryList);
};

const debouncedHandleInventoryDisplay = debounce(handleInventoryDisplay, 300);

const clearSearchInput = () => {
  document.getElementById("searchInput").value = "";
  debouncedHandleInventoryDisplay();
};

window.addEventListener("load", function () {
  document.getElementById("searchInput").value = "";
  handleInventoryDisplay();

  const checkboxes = document.querySelectorAll('input[name="category"]');
  checkboxes.forEach((checkbox) => {
    checkbox.addEventListener("change", debouncedHandleInventoryDisplay);
  });
});
