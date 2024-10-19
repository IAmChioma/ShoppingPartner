
window.onload = document.getElementById('searchBtn').addEventListener('click', function (e) {
  e.preventDefault();
  var searchParam = document.getElementById('searchParameter').value;
  console.log(searchParam);
  if (searchParam == "") {
    var toastEl = document.getElementById('liveToast');
    var toast = new bootstrap.Toast(toastEl);
    toast.show(); // Display the toast
    return;
  }

  // TODO: Fetch data
  fetch("http://127.0.0.1:5000/search/" + searchParam)
    .then(response => {
      return response.json();
    })
    .then(data => {
      SetProductCard(data);
    })
    .catch(error => console.log(error));

  // Display fetched data on html

  function SetProductCard(data) {
    document.getElementById("my-products").innerHTML = "";
    for (let i = 0; i < data.length; i++) {
      const card = document.createElement("div");
      card.classList = "col m-2";


      const content = `
  <div class="col m-2">
  <div class="card" style="width: 18rem;">
      <div class="card-img-top" src="" alt="Card image Cap">
          <div class="card-header">
              <img class="card-img-top" src="${data[i].img_url}" alt="Card image Cap" />
          </div>
          <div class="card-body">
              <h5 class="card-title">${data[i].title}</h5>
              <p class="card-text">${data[i].price}</p>
            
              <a href="${data[i].link}" class="btn btn-primary" target="_blank">Go to site</a>
          </div>
      </div>
  </div>
</div>

    `;
      document.getElementById("my-products").innerHTML += content;

    }

  }
});

