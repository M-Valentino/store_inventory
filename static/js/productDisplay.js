let currProdOriginalBasicInfo = {
  name: "",
  category: "",
  upc: "",
  qty: "",
};

const openProductDetails = async (name, category, upc, qty) => {
  document.getElementById("basicInfoError").innerHTML = "";
  document.getElementById("descriptionUpdateError").innerHTML = "";
  document.getElementById("productDescription").value = "";

  document.getElementById("productDetailsModal").style.display = "initial";
  document.getElementById("product-name-h1").innerHTML = name;
  currProdOriginalBasicInfo.name = name;
  document.getElementById("categoryChange").value = category;
  currProdOriginalBasicInfo.category = category;
  document.getElementById("upcUpdate").value = upc;
  currProdOriginalBasicInfo.upc = upc;
  document.getElementById("qtyUpdate").innerHTML = qty;
  currProdOriginalBasicInfo.qty = qty;

  const extendedInfo = await fetchExtendedProductInfo(upc);
  console.log(extendedInfo);
  document.getElementById("productDescription").value = extendedInfo.message;
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
    const oldUPC = currProdOriginalBasicInfo.upc;
    const newUPC = document.getElementById("upcUpdate").value;
    params.append("oldUpc", oldUPC);
    if (!newUPC.match("/^d{12}$/")) {
      document.getElementById("basicInfoError").innerHTML =
        "UPCs must be a number 12 digits long";
      return;
    } else if (oldUPC !== newUPC) {
      params.append("newUpc", document.getElementById("upcUpdate").value);
    }

    const oldCategory = currProdOriginalBasicInfo.category;
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
        currProdOriginalBasicInfo.name,
        currProdOriginalBasicInfo.category,
        currProdOriginalBasicInfo.upc,
        currProdOriginalBasicInfo.qty
      );
      document.getElementById(
        "basicInfoError"
      ).innerHTML = `Error: ${json.message}`;
    } else {
      makeToast(`Updated ${currProdOriginalBasicInfo.name}`);
      document.getElementById("basicInfoError").innerHTML = "";
      handleInventoryDisplay();
      console.log(message);
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
  const upc = currProdOriginalBasicInfo.upc;
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
      makeToast(`Updated ${currProdOriginalBasicInfo.name}`);
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
