// Predefined FAQ responses
const faqResponses = {
  "what are your working hours?":
    "Our working hours are Monday to Friday, from 9 AM to 6 PM.",
  "how do i reset my password?":
    "To reset your password, go to the login page and click on 'Forgot Password'. Follow the instructions from there.",
  "where can i check my order status?":
    "You can check your order status by logging into your account and navigating to the 'My Orders' section.",
  "i want to speak to a live agent":
    "Sure! Redirecting you to a live agent now... Please wait.",
  "can i return a product?":
    "Yes, you can return a product within 30 days of purchase as long as it meets our return conditions.",
};

// Fallback response for questions not in the FAQ
const fallbackResponse =
  "I'm sorry, I don't have an answer to that. Let me connect you to a live agent.";

// Script to handle sending messages and displaying bot responses
document.getElementById("send-btn").addEventListener("click", function () {
  sendMessage();
});

document
  .getElementById("user-input")
  .addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
      sendMessage();
    }
  });

function sendMessage() {
  const userInput = document.getElementById("user-input");
  const message = userInput.value.trim().toLowerCase(); // Convert user message to lowercase

  if (message !== "") {
    // Display user's message
    appendMessage(userInput.value, "user-message");

    // Clear input field
    userInput.value = "";

    // Simulate bot response
    setTimeout(() => {
      botResponse(message);
    }, 1000);
  }
}

function appendMessage(message, className) {
  const chatWindow = document.getElementById("chat-window");
  const newMessage = document.createElement("div");
  newMessage.classList.add("chat-message", className);
  newMessage.textContent = message;
  chatWindow.appendChild(newMessage);

  // Scroll chat window to the bottom
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

function botResponse(userMessage) {
  let response = faqResponses[userMessage] || fallbackResponse;
  appendMessage(response, "bot-message");
}
