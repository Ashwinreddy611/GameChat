$(document).ready(function () {
  $('.sidenav').sidenav();
  $('.tooltipped').tooltip();
  $('.datepicker').datepicker({
    format: "dd mmmm, yyyy",
    yearRange: 10,
    showClearBtn: true,
    i18n: {
      done: "Select"
    }
  });
});
        