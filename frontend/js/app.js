
  window.onload = document.getElementById('searchBtn').addEventListener('click', function (e){
    e.preventDefault();
    var searchParam = document.getElementById('searchParameter').value;
    console.log(searchParam);
    if(searchParam == "" ){
        var toastEl = document.getElementById('liveToast');
        var toast = new bootstrap.Toast(toastEl);
        toast.show(); // Display the toast
        return;
    }

    // TODO: Fetch data
    fetch ("http://127.0.0.1:5000/search/"+searchParam).then(response => console.log(response))


    // TODO: Display fetched data on html
    
  });
  
