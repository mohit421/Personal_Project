function toggleButton(selector){
    const gameBtn = document.querySelector(selector);
    const btnGame = gameBtn.classList.contains('is-toggled');
    if(!btnGame){
        gameBtn.classList.add('is-toggled');
    }
    else{
        gameBtn.classList.remove('is-toggled');
    }
}
       