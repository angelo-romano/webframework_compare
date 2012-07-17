<html>
<head>
<title>Country list</title>
</head>
<body>
<h1>Country list</h1>
<ol>
<% countries_sorted = sorted(countries, key=lambda o: o.name) %>
% for country in countries_sorted:
<li><a href="/countries/${country.slug}/">${country.name}</a></li>
% endfor
</ol>
</body>
</html>
