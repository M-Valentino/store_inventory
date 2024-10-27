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
  makeSalesChart();
  JsBarcode("#barcode", upc);
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
      document.getElementById("basicInfoError").innerHTML = "";

      currProdOriginalInfo.upc = newUPC;
      currProdOriginalInfo.category = newCategory;
      openProductDetails(
        currProdOriginalInfo.name,
        currProdOriginalInfo.category,
        currProdOriginalInfo.upc,
        currProdOriginalInfo.qty
      );
      
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
          parseInt(currProdOriginalInfo.qty) + parseInt(restockQty)
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

const makeSalesChart = () => {
  // Clear existing chart
  document.getElementById("my_dataviz").innerHTML = "";

  // set the dimensions and margins of the graph
  var margin = { top: 30, right: 20, bottom: 20, left: 20 },
    width = 800 - margin.left - margin.right,
    height = 300 - margin.top - margin.bottom;

  // append the svg object to the body of the page
  var svg = d3
    .select("#my_dataviz")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  svg
    .append("text")
    .attr("x", width / 2)
    .attr("y", 0 - margin.top / 2)
    .attr("text-anchor", "middle")
    .style("font-size", "16px")
    .style("font-weight", "bolder")
    .style("color", "#000000a0")
    .text("Sales over Time");

  //Read the data
  d3.csv(
    `/data/sales?productId=${currProdOriginalInfo.id}`,

    // When reading the csv, I must format variables:
    function (d) {
      return { date: d3.timeParse("%Y-%m-%d")(d.date), value: d.sale };
    },

    // Now I can use this dataset:
    function (data) {
      // Add X axis --> it is a date format
      var x = d3
        .scaleTime()
        .domain(
          d3.extent(data, function (d) {
            return d.date;
          })
        )
        .range([0, width]);
      svg
        .append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));

      // Add Y axis
      var y = d3
        .scaleLinear()
        .domain([
          0,
          d3.max(data, function (d) {
            return +d.value;
          }),
        ])
        .range([height, 0]);
      svg.append("g").call(d3.axisLeft(y));

      // Add the line
      svg
        .append("path")
        .datum(data)
        .attr("fill", "none")
        .attr("stroke", "steelblue")
        .attr("stroke-width", 1.5)
        .attr(
          "d",
          d3
            .line()
            .x(function (d) {
              return x(d.date);
            })
            .y(function (d) {
              return y(d.value);
            })
        );
    }
  );
};
