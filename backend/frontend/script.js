const chatBox = document.getElementById("chat-box");

const input = document.getElementById("user-input");


async function sendMessage() {

    const question = input.value.trim();


    if (!question) {
        return;
    }


    // Show user question

    addMessage(question, "user");

    input.value = "";


    // Show loading

    const loadingMessage = addMessage(
        "Thinking...",
        "bot"
    );


    try {

        const response = await fetch(
            "http://127.0.0.1:8000/chat",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    question: question
                })
            }
        );


        const data = await response.json();


        loadingMessage.remove();


        addMessage(
            data.answer,
            "bot"
        );


    } catch (error) {

        loadingMessage.remove();


        addMessage(
            "Sorry, I couldn't connect to the AI server.",
            "bot"
        );

        console.error(error);
    }
}


function addMessage(text, sender) {

    const message = document.createElement("div");

    message.classList.add(
        "message",
        sender
    );


    const avatar = document.createElement("div");

    avatar.classList.add("avatar");

    avatar.textContent =
        sender === "bot" ? "🩺" : "👤";


    const bubble = document.createElement("div");

    bubble.classList.add("bubble");

    bubble.textContent = text;


    message.appendChild(avatar);

    message.appendChild(bubble);


    chatBox.appendChild(message);


    chatBox.scrollTop =
        chatBox.scrollHeight;


    return message;
}


input.addEventListener(
    "keydown",
    function(event) {

        if (event.key === "Enter") {

            sendMessage();

        }

    }
);