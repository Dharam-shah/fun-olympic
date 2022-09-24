// sidebar collapse
$('#sidebarCollapse').on('click', function () {
  $('#sidebar').toggleClass('active');
});


$('#sidebarCollapse').on('click', function () {
  if ($('.hidden').length > 0) {
    $('.hidden').removeClass('hidden');
  } else {
    $('.remove-margin').addClass('hidden');
  }
  // $('.full-width').css('margin-left', '300px');
  // $('.full-width').css('margin-left', '0');
});

// $('#sidebarCollapse').on('click', function () {
//   $('.full-width').css('margin-left', '300px');
// });