$(document).ready(function () {
  setTimeout(function () {
    $("#messageModal").modal("show");
  }, 1000);
  setTimeout(function () {
    $("#mainToast").toast("show");
  }, 1500);
});

$(window).on("load", function () {
  $(".main-page-content").fadeIn(2000);
});

const scrollSpy = new bootstrap.ScrollSpy(document.body, {
  target: "#guideNavbar",
});
