let currProdOriginalInfo = {
  name: "",
  category: "",
  upc: "",
  qty: "",
  id: "",
};

const openProductDetails = async (name, category, upc, qty) => {
  document.getElementById("basicInfoError").innerHTML = "";
  document.getElementById("descriptionUpdateError").innerHTML = "";
  document.getElementById("productDescription").value = "";

  document.getElementById("productDetailsModal").style.display = "initial";
  document.getElementById("product-name-h1").innerHTML = name;
  currProdOriginalInfo.name = name;
  document.getElementById("categoryChange").value = category;
  currProdOriginalInfo.category = category;
  document.getElementById("upcUpdate").value = upc;
  currProdOriginalInfo.upc = upc;
  document.getElementById("qtyUpdate").innerHTML = qty;
  currProdOriginalInfo.qty = qty;

  const extendedInfo = await fetchExtendedProductInfo(upc);
  document.getElementById("productDescription").value = extendedInfo.message;
  currProdOriginalInfo.id = extendedInfo.id;
};

const closeProductDetails = () => {
  document.getElementById("productDetailsModal").style.display = "none";
};

const closeAddProduct = () => {
  document.getElementById("addProductModal").style.display = "none";
};

document.getElementById("underlayPD").addEventListener("click", function () {
  closeProductDetails();
});

document.getElementById("underlayAP").addEventListener("click", function () {
  closeAddProduct();
});

const updateBasicInfo = async () => {
  try {
    const params = new URLSearchParams();
    const oldUPC = currProdOriginalInfo.upc;
    const newUPC = document.getElementById("upcUpdate").value;
    params.append("oldUpc", oldUPC);
    if (upcNotValid(newUPC)) {
      document.getElementById("basicInfoError").innerHTML =
        "UPCs must be a number 12 digits long";
      return;
    } else if (oldUPC !== newUPC) {
      params.append("newUpc", document.getElementById("upcUpdate").value);
    }

    const oldCategory = currProdOriginalInfo.category;
    const newCategory = document.getElementById("categoryChange").value;
    if (oldCategory !== newCategory) {
      params.append("newCategory", newCategory);
    }

    const response = await fetch(
      `/data/basicProductInfo/?${params.toString()}`,
      {
        method: "POST",
      }
    );
    const json = await response.json();

    if (json.message !== "success") {
      openProductDetails(
        currProdOriginalInfo.name,
        currProdOriginalInfo.category,
        currProdOriginalInfo.upc,
        currProdOriginalInfo.qty
      );
      document.getElementById(
        "basicInfoError"
      ).innerHTML = `Error: ${json.message}`;
    } else {
      makeToast(`Updated ${currProdOriginalInfo.name}`);
      currProdOriginalInfo.upc = newUPC;
      document.getElementById("basicInfoError").innerHTML = "";
      handleInventoryDisplay();
    }
  } catch (e) {
    console.warn(e);
  }
};

const showAddProductModal = () => {
  document.getElementById("addProductModal").style.display = "initial";
};

const fetchExtendedProductInfo = async (upc) => {
  try {
    const params = new URLSearchParams();
    params.append("upc", upc);

    const response = await fetch(`/data/extendedInfo?${params.toString()}`, {
      method: "GET",
    });

    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    const json = await response.json();
    return json;
  } catch (e) {
    console.warn(e);
  }
};

const updateExtendedProductInfo = async () => {
  const description = document.getElementById("productDescription").value;
  const upc = currProdOriginalInfo.upc;
  let descriptionError = document.getElementById("descriptionUpdateError");

  try {
    const formData = new FormData();
    formData.append("upc", upc);
    formData.append("description", btoa(description));

    const response = await fetch(`/data/extendedInfo/`, {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      descriptionError.innerHTML = response.status;
    }
    const json = await response.json();
    if (json.message === "success") {
      makeToast(`Updated ${currProdOriginalInfo.name}`);
    } else {
      descriptionError.innerHTML = json.message;
    }

    return json;
  } catch (e) {
    console.warn(e);
  }
};

const makeToast = (message) => {
  let toast = document.getElementById("toast");
  const toastMessage = document.getElementById("toastMessage");
  toastMessage.innerHTML = message;

  toast.style.display = "block";
  setTimeout(() => {
    toast.style.display = "none";
    // Same as toast CSS animation duration
  }, 3500);
};

const upcNotValid = (str) => {
  return !str.match(/^\d{12}$/);
};

const addProduct = async () => {
  try {
    const newProductName = document
      .getElementById("newProductName")
      .value.trim();
    const newProductUPC = document.getElementById("newProductUPC").value.trim();
    const newProductCategory =
      document.getElementById("newProductCategory").value;
    const newProductDesc = document
      .getElementById("newProductDesc")
      .value.trim();
    const basicInfoError = document.getElementById("basicInfoError");

    basicInfoError.innerHTML = "";

    if (!newProductName) {
      basicInfoError.innerHTML = "Product name is required.";
      return;
    }
    if (upcNotValid(newProductUPC)) {
      basicInfoError.innerHTML = "UPC must be a 12-digit number.";
      return;
    }

    const formData = new FormData();
    formData.append("name", newProductName);
    formData.append("upc", newProductUPC);
    formData.append("category", newProductCategory);
    formData.append("description", newProductDesc);

    const response = await fetch("/data/product/", {
      method: "POST",
      body: formData,
    });

    const json = await response.json();

    if (json.message !== "success") {
      basicInfoError.innerHTML = `Error: ${json.message}`;
    } else {
      makeToast(`Product ${newProductName} added successfully!`);
      closeAddProduct();
      handleInventoryDisplay();
    }
  } catch (e) {
    console.warn(e);
    document.getElementById("basicInfoError").innerHTML =
      "An error occurred. Please try again.";
  }
};

const addSale = () => {
  const soldQty = document.getElementById("soldQty").value;
  const dateSold = document.getElementById("dateSold").value;

  if (!soldQty || soldQty < 1) {
    return;
  }

  if (!dateSold) {
    return;
  }

  const data = {
    id: currProdOriginalInfo.id,
    soldQty: soldQty,
    dateSold: dateSold,
  };

  fetch("/data/sale/", {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((result) => {
      if (result.message === "success") {
        makeToast("Sale Added.");
        openProductDetails(
          currProdOriginalInfo.name,
          currProdOriginalInfo.category,
          currProdOriginalInfo.upc,
          currProdOriginalInfo.qty - soldQty
        );
        handleInventoryDisplay();
      } else {
        console.error(`Error: ${result.message}`);
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
};

const addRestock = () => {
  const restockQty = document.getElementById("restockQty").value;
  const dateRestocked = document.getElementById("dateRestocked").value;

  if (!restockQty || restockQty < 1) {
    return;
  }

  if (!dateRestocked) {
    return;
  }

  const data = {
    id: currProdOriginalInfo.id,
    restockQty: restockQty,
    dateRestocked: dateRestocked,
  };

  fetch("/data/restock/", {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((result) => {
      if (result.message === "success") {
        makeToast("Restock Added.");
        openProductDetails(
          currProdOriginalInfo.name,
          currProdOriginalInfo.category,
          currProdOriginalInfo.upc,
          currProdOriginalInfo.qty + restockQty
        );
        handleInventoryDisplay();
      } else {
        console.error(`Error: ${result.message}`);
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
};
