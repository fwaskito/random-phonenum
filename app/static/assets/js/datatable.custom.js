$(document).ready(function () {
  if ($("#dataTable").length) {
    var table = $("#dataTable").DataTable({
      dom: "Bfrtip",
      buttons: [
        "csv",
        {
          extend: "excel",
          title: "",
        },
      ],
      responsive: true,
    });
  }
});
