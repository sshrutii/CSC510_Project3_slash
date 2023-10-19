async function fetchData() {
  const website = document.getElementById('website').value;
  const product = document.getElementById('product').value;
  const response = await fetch(`http://127.0.0.1:5050/${website}/${product}`);
  const data = await response.json();

  const resultsDiv = document.getElementById('results');
  resultsDiv.innerHTML = '';

  data.forEach(item => {
    // Replace spaces in the price with a dot
    let formattedPrice = item.price.replace(/\s+/g, '.');

    const itemDiv = document.createElement('div');
    
    if(website=="wm"){
      formattedPrice=formattedPrice.replace("Now.$.", "$");
      itemDiv.innerHTML = `<h3>${item.title}</h3><p>Price: ${formattedPrice}</p><a href="${item.link}" target="_blank">Link</a>`;
    }
    else{
      itemDiv.innerHTML = `<h3>${item.title}</h3><p>Price: ${formattedPrice}</p><a href="${item.link}" target="_blank">Link</a>`;
    }

    resultsDiv.appendChild(itemDiv);
  });
}

document.getElementById('fetchButton').addEventListener('click', fetchData);
