const $ = window.$;

$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, textStatus) {
  for (let i = 0; i < data.results.length; i++) {
    const movieTitle = data.results[i].title;
    const listItem = $('<li></li>').text(movieTitle);
    $('ul#list_movies').append(listItem);
  }
});
