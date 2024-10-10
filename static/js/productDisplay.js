const openProductDetails = (name, category, upc, qty) => {
  document.getElementById("productDetailsModal").style.display = "initial";
  document.getElementById("product-name-h1").innerHTML = name;
  document.getElementById('categoryChange').value = category;
  document.getElementById('upcUpdate').value = upc;
  document.getElementById('qtyUpdate').innerHTML = qty;
};

const closeProductDetails = () => {
  document.getElementById("productDetailsModal").style.display = "none";
};

document.getElementById("underlay").addEventListener("click", function () {
  closeProductDetails();
});
