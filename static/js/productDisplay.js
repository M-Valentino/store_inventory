let currentProductOriginalDetails = {
  name: "",
  category: "",
  upc: "",
}

const openProductDetails = (name, category, upc, qty) => {
  document.getElementById("productDetailsModal").style.display = "initial";
  document.getElementById("product-name-h1").innerHTML = name;
  currentProductOriginalDetails.name = name;
  document.getElementById('categoryChange').value = category;
  currentProductOriginalDetails.category = category;
  document.getElementById('upcUpdate').value = upc;
  currentProductOriginalDetails.upc = upc;
  document.getElementById('qtyUpdate').innerHTML = qty;
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
    const oldUPC = currentProductOriginalDetails.upc;
    const newUPC = document.getElementById('upcUpdate').value;
    params.append("oldUpc", oldUPC);
    if (oldUPC !== newUPC) {
      params.append("newUpc", document.getElementById('upcUpdate').value);
    }

    const oldCategory = currentProductOriginalDetails.category;
    const newCategory = document.getElementById('categoryChange').value;
    if (oldCategory !== newCategory) {
      params.append("newCategory", newCategory);
    }

    const response = await fetch(`/data/basicProductInfo/?${params.toString()}`, {
      method: "POST",
    });
    const json = await response.json();

    if (json.message !== "success") {
      document.getElementById("basicInfoError").innerHTML = `Error: ${json.message}`;
    }
    openProductDetails();
  } catch (e) {
    console.warn(e);
  }
}
