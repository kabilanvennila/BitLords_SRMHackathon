/* JS for text to speech */

document.querySelector("#resume").addEventListener("click", () => {
    window.speechSynthesis.resume();
});

document.querySelector("#pause").addEventListener("click", () => {
    window.speechSynthesis.pause();
});
