<html>
<head>
<title>City list - ${country.name}</title>
</head>
<body>
<h1>City list - ${country.name}</h1>
<ol>
<% cities_sorted = sorted(country.cities.all(), key=lambda x: x.name) %>
% for city in cities_sorted:
<li><a href="/countries/${country.slug}/cities/${city.slug}/">${city.name}</a></li>
% endfor
</ol>
</body>
</html>
