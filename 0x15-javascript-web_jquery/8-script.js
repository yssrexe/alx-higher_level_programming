$(document).ready(function () {
  $.get(
    'https://swapi-api.alx-tools.com/api/films/?format=json',
    function (data, status) {
      if (status === 'success') {
        data.results.forEach((movie) => {
          $('#list_movies').append('<li>' + movie.title + '</li>');
        });
      }
    }
  );
});
