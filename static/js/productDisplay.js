const openProductDetails = (upc) => {
  document.getElementById("productDetailsModal").style.display = "initial";
};

const closeProductDetails = () => {
  document.getElementById("productDetailsModal").style.display = "none";
};

document.getElementById("underlay").addEventListener("click", function () {
  closeProductDetails();
});
