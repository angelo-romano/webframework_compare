<html>
<head>
<title>Country - ${country.name}</title>
</head>
<body>
<h1>${country.name}</h1>
<ul>
<% wikiurl = "http://en.wikipedia.org/wiki/" + country.wikiname %>
<li><strong>Country code:</strong> ${country.code}</li>
<li><strong>Currency:</strong> ${country.currency}</li>
<li><strong>Wikipedia page:</strong> <a href="${wikiurl}">${wikiurl}</a></li>
<li><strong>List of cities:</strong> <a href="/countries/${country.slug}/cities/">here</a></strong></li>
</ul>
</body>
</html>
