let main = document.getElementById("main");
let messageRowContainer = document.getElementById("message-row-container");
let messageRow = document.getElementById("message-row");

//Create the button
let closeBtn = document.createElement("button");
closeBtn.classList.add("close-btn");
closeBtn.innerHTML = "X";

if (messageRow instanceof Element) {
  messageRow.appendChild(closeBtn);
}

/**
 * Function is run when button is clicked. 
 * It removes the alert.
 */
function closeBtnClick(event) {
    main.removeChild(messageRowContainer);
}
closeBtn.addEventListener("click", closeBtnClick);

