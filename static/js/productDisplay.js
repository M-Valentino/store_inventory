let currProdOriginalBasicInfo = {
  name: "",
  category: "",
  upc: "",
  qty: "",
}

const openProductDetails = (name, category, upc, qty) => {
  document.getElementById("basicInfoError").innerHTML = "";

  document.getElementById("productDetailsModal").style.display = "initial";
  document.getElementById("product-name-h1").innerHTML = name;
  currProdOriginalBasicInfo.name = name;
  document.getElementById('categoryChange').value = category;
  currProdOriginalBasicInfo.category = category;
  document.getElementById('upcUpdate').value = upc;
  currProdOriginalBasicInfo.upc = upc;
  document.getElementById('qtyUpdate').innerHTML = qty;
  currProdOriginalBasicInfo.qty = qty;
};

const closeProductDetails = () => {
  document.getElementById("productDetailsModal").style.display = "none";
};

document.getElementById("underlay").addEventListener("click", function () {
  closeProductDetails();
});

const updateBasicInfo = async () => {
  try {
    const params = new URLSearchParams();
    const oldUPC = currProdOriginalBasicInfo.upc;
    const newUPC = document.getElementById('upcUpdate').value;
    params.append("oldUpc", oldUPC);
    if (oldUPC !== newUPC) {
      params.append("newUpc", document.getElementById('upcUpdate').value);
    }

    const oldCategory = currProdOriginalBasicInfo.category;
    const newCategory = document.getElementById('categoryChange').value;
    if (oldCategory !== newCategory) {
      params.append("newCategory", newCategory);
    }

    const response = await fetch(`/data/basicProductInfo/?${params.toString()}`, {
      method: "POST",
    });
    const json = await response.json();

    if (json.message !== "success") {
      openProductDetails(
        currProdOriginalBasicInfo.name, 
        currProdOriginalBasicInfo.category, 
        currProdOriginalBasicInfo.upc, 
        currProdOriginalBasicInfo.qty
      );
      document.getElementById("basicInfoError").innerHTML = `Error: ${json.message}`;
    } else {
      document.getElementById("basicInfoError").innerHTML = "";
      handleInventoryDisplay();
    }
  } catch (e) {
    console.warn(e);
  }
}
