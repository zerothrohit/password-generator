function copyFunction() {

    var copyText = document.getElementById("yourPass");
    const popup = document.querySelector(".popup");
    popup.classList.add("active");
    copyText.select();
    copyText.setSelectionRange(0, 99999);   
    navigator.clipboard.writeText(copyText.value);
    
  }

  
  window.onload=function(){
    const popup = document.querySelector(".popup");
    popup.addEventListener("animationend", () => {
      popup.classList.remove("active");
    });
  }


