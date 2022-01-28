  const copyText = document.querySelector('.copy-text button');
  const popup = document.querySelector('.popup');
  
  copyText.addEventListener('click', () => {
    popup.classList.add('active');
    //copyToClipBoard();
  });
