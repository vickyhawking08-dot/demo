/* =========================================================
   APP STATE
========================================================= */

let conversation = [];

let currentIndex = 0;

let isProcessing = false;


/* =========================================================
   ELEMENTS
========================================================= */

const introScreen =
    document.getElementById("introScreen");

const chatScreen =
    document.getElementById("chatScreen");

const endScreen =
    document.getElementById("endScreen");

const startButton =
    document.getElementById("startButton");

const nextButton =
    document.getElementById("nextButton");

const restartButton =
    document.getElementById("restartButton");

const chatMessages =
    document.getElementById("chatMessages");

const typingIndicator =
    document.getElementById("typingIndicator");

const progressText =
    document.getElementById("progressText");

const progressFill =
    document.getElementById("progressFill");

const nextButtonText =
    document.getElementById("nextButtonText");


/* =========================================================
   LOAD CONVERSATION
========================================================= */

async function loadConversation() {

    try {

        const response =
            await fetch("/api/conversation");

        if (!response.ok) {
            throw new Error(
                "Failed to load conversation"
            );
        }

        const data =
            await response.json();

        conversation =
            data.conversation;

        progressText.textContent =
            `0 / ${conversation.length}`;

    } catch (error) {

        console.error(error);

        alert(
            "Conversation load aagala. Server check pannunga."
        );
    }
}


/* =========================================================
   START
========================================================= */

async function startConversation() {

    if (conversation.length === 0) {
        await loadConversation();
    }

    currentIndex = 0;

    introScreen.classList.add("hidden");

    endScreen.classList.add("hidden");

    chatScreen.classList.remove("hidden");

    resetChat();

    updateProgress();

    nextButton.disabled = false;

    nextButtonText.textContent = "Next";

    showNextMessage();
}


/* =========================================================
   RESET CHAT
========================================================= */

function resetChat() {

    chatMessages.innerHTML = `
        <div class="date-divider">
            <span>TODAY</span>
        </div>
    `;

    chatMessages.appendChild(
        typingIndicator
    );

    typingIndicator.classList.add("hidden");
}


/* =========================================================
   SHOW NEXT MESSAGE
========================================================= */

async function showNextMessage() {

    if (isProcessing) {
        return;
    }

    if (
        currentIndex >= conversation.length
    ) {
        showEndScreen();
        return;
    }

    isProcessing = true;

    nextButton.disabled = true;

    const message =
        conversation[currentIndex];

    showTyping(message);

    /*
        Small delay creates natural
        conversation typing effect.
    */

    const typingTime =
        Math.min(
            900,
            Math.max(
                450,
                message.message.length * 18
            )
        );

    await delay(typingTime);

    hideTyping();

    addMessage(message);

    currentIndex++;

    updateProgress();

    isProcessing = false;

    if (
        currentIndex >= conversation.length
    ) {

        nextButtonText.textContent =
            "Finish ❤️";

    } else {

        nextButtonText.textContent =
            "Next";
    }

    nextButton.disabled = false;

    scrollToBottom();
}


/* =========================================================
   ADD MESSAGE
========================================================= */

function addMessage(message) {

    const row =
        document.createElement("div");

    row.className =
        `message-row ${message.role}`;

    const content =
        document.createElement("div");

    content.className =
        "message-content";

    const avatar =
        document.createElement("div");

    avatar.className =
        "message-avatar";

    avatar.textContent =
        message.emoji;

    const bubble =
        document.createElement("div");

    bubble.className =
        "message-bubble";

    bubble.textContent =
        message.message;

    content.appendChild(avatar);

    content.appendChild(bubble);

    row.appendChild(content);

    chatMessages.insertBefore(
        row,
        typingIndicator
    );

    scrollToBottom();
}


/* =========================================================
   TYPING
========================================================= */

function showTyping(message) {

    const avatar =
        typingIndicator.querySelector(
            ".typing-avatar"
        );

    avatar.textContent =
        message.emoji;

    typingIndicator.classList.remove(
        "hidden"
    );

    scrollToBottom();
}


function hideTyping() {

    typingIndicator.classList.add(
        "hidden"
    );
}


/* =========================================================
   PROGRESS
========================================================= */

function updateProgress() {

    const total =
        conversation.length;

    const current =
        currentIndex;

    progressText.textContent =
        `${current} / ${total}`;

    const percentage =
        total === 0
            ? 0
            : (current / total) * 100;

    progressFill.style.width =
        `${percentage}%`;
}


/* =========================================================
   END SCREEN
========================================================= */

function showEndScreen() {

    chatScreen.classList.add(
        "hidden"
    );

    endScreen.classList.remove(
        "hidden"
    );
}


/* =========================================================
   RESTART
========================================================= */

function restartConversation() {

    currentIndex = 0;

    endScreen.classList.add(
        "hidden"
    );

    chatScreen.classList.remove(
        "hidden"
    );

    resetChat();

    updateProgress();

    nextButtonText.textContent =
        "Next";

    nextButton.disabled = false;

    showNextMessage();
}


/* =========================================================
   SCROLL
========================================================= */

function scrollToBottom() {

    setTimeout(() => {

        chatMessages.scrollTo({
            top: chatMessages.scrollHeight,
            behavior: "smooth"
        });

    }, 50);
}


/* =========================================================
   DELAY
========================================================= */

function delay(ms) {

    return new Promise(
        resolve => setTimeout(
            resolve,
            ms
        )
    );
}


/* =========================================================
   EVENT LISTENERS
========================================================= */

startButton.addEventListener(
    "click",
    startConversation
);

nextButton.addEventListener(
    "click",
    showNextMessage
);

restartButton.addEventListener(
    "click",
    restartConversation
);


/* =========================================================
   INITIAL LOAD
========================================================= */

loadConversation();
