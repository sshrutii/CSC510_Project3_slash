async function fetchData() {
  const website = document.getElementById('website').value;
  const product = document.getElementById('product').value;
  const response = await fetch(`http://127.0.0.1:5050/${website}/${product}`);
  const data = await response.json();

  const resultsDiv = document.getElementById('results');
  resultsDiv.innerHTML = '';

  data.forEach(item => {
    // Remove spaces and add a dot to the price
    const formattedPrice = item.price.replace(/\s/g, '').replace('$', '$ ');
    const itemDiv = document.createElement('div');
    itemDiv.innerHTML = `<h3>${item.title}</h3><p>Price: ${formattedPrice}</p><a href="${item.link}" target="_blank">Link</a>`;
    resultsDiv.appendChild(itemDiv);
  });
}

document.getElementById('fetchButton').addEventListener('click', fetchData);
