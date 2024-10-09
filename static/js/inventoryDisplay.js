const populateInventoryTable = (inventoryList) => {
  let tbody = document.getElementById("inventoryList");
  tbody.innerHTML = "";

  inventoryList.map((product, index) => {
    let tr = document.createElement("tr");
    tr.classList.add("hover-rows");
    tr.onclick = () => openProductDetails(product.upc);

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

const fetchInventory = async (categories, searchTermObj) => {
  try {
    const params = new URLSearchParams();
    if (categories.length > 0) {
      params.append("category", categories.join(","));
    }

    params.append("searchTerm", searchTermObj.searchTerm);
    params.append("searchBy", searchTermObj.searchBy);
    params.append("sortBy", document.getElementById("sortByBtn").innerHTML);

    const response = await fetch(`/data/inventory?${params.toString()}`, {
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
  const searchBy =
    document.querySelector('input[name="searchBy"]:checked').value || "";
  return { searchTerm: searchTerm, searchBy: searchBy };
};

const handleInventoryDisplay = async () => {
  const searchTerm = getSearchTerm();
  const checkedCategories = getCheckedCategories();
  const inventoryList = await fetchInventory(checkedCategories, searchTerm);
  populateInventoryTable(inventoryList);
};

const debouncedHandleInventoryDisplay = debounce(handleInventoryDisplay, 300);

const showOrHideClearButton = () => {
  const searchInput = document.getElementById("searchInput").value;
  let clearInput = document.getElementById("clear-input");
  if (searchInput === "") {
    clearInput.style.display = "none";
  } else {
    clearInput.style.display = "initial";
  }
};

const clearSearchInput = () => {
  document.getElementById("searchInput").value = "";
  showOrHideClearButton();
  debouncedHandleInventoryDisplay();
};

const toggleSortMenu = () => {
  let sortMenu = document.getElementById("sortMenu");
  let currentDisplay = window.getComputedStyle(sortMenu).display;

  if (currentDisplay === "none") {
    sortMenu.style.display = "initial";
  } else {
    sortMenu.style.display = "none";
  }
};

const setSort = (currentSort) => {
  document.getElementById("sortByBtn").innerText = currentSort;
  document.getElementById("sortMenu").style.display = "none";
};

const determineTableHeight = () => {
  const headerHeight = document.getElementById("site-header").clientHeight;
  const bodyHeight = window.innerHeight;
  // 8 acounts for margin-bottom in the header
  const availableHeight = bodyHeight - headerHeight - 8;

  document.getElementById("table-container").style.height =
    availableHeight + "px";
};

window.addEventListener("load", function () {
  determineTableHeight();
  document.getElementById("searchInput").value = "";
  handleInventoryDisplay();
});

window.onresize = function (event) {
  determineTableHeight();
};

document
  .getElementById("searchInput")
  .addEventListener("change", showOrHideClearButton);

document.querySelectorAll(".sort-by-item").forEach((item) => {
  console.log(1);
  item.addEventListener("click", function () {
    setSort(this.getAttribute("data-value"));
    debouncedHandleInventoryDisplay();
  });
});

const checkboxes = document.querySelectorAll('input[name="category"]');
checkboxes.forEach((checkbox) => {
  checkbox.addEventListener("change", debouncedHandleInventoryDisplay);
});
