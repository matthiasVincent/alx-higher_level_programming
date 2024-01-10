$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  $('UL#list_movies').append($.map(data.results , function(movie)
  {
    return `<li>${movie.title}</li>`}));
});
