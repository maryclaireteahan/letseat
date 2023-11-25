let main = document.getElementById("main");
let messageRowContainer = document.getElementById("message-row-container");
let messageRow = document.getElementById("message-row");
let message = document.getElementById("message");
let messageButton = document.getElementById("message-button");



//Create the button
let closeBtn = document.createElement("button");
closeBtn.classList.add("close-btn");
closeBtn.innerHTML = "X";

if (messageRow instanceof Element) {
  messageRow.appendChild(closeBtn);
} else {
  console.error('messageRow is not a valid DOM element');
}

/**
 * Function is run when button is clicked. 
 * It removes the Rules div.
 */
function closeBtnClick(event) {
    main.removeChild(messageRowContainer);
}
closeBtn.addEventListener("click", closeBtnClick);

