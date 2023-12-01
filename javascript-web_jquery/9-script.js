const $ = window.$;

function DocumentReady () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data, textStatus) {
    $('div#hello').text(data.hello);
  });
}

$(document).ready(DocumentReady);
