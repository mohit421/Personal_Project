function toggleButton(selector){
    const gameBtn = document.querySelector(selector);
    const btnGame = gameBtn.classList.contains('is-toggled');
    if(!btnGame){
        // before turning this button ON, check if there's 
        // already a button that's turned ON and turn it OFF.
        turnOffPreviousButton();

        gameBtn.classList.add("is-toggled");
    }
    else{
        gameBtn.classList.remove('is-toggled');
    }
}
       
function turnOffPreviousButton() {
    const previousBtn = document.querySelector(".is-toggled")
    if (previousBtn) {
        previousBtn.classList.remove('is-toggled')
    }
}