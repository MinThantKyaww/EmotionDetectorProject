const form = document.querySelector("#emotion-form");
const result = document.querySelector("#result");

form.addEventListener("submit", async (event) => {
    event.preventDefault();
    result.textContent = "Analyzing…";
    try {
        const query = new URLSearchParams(new FormData(form));
        const response = await fetch(`emotionDetector?${query}`);
        if (!response.ok) {
            throw new Error("Emotion detection failed");
        }
        result.textContent = await response.text();
    } catch {
        result.textContent = "Analysis failed. Please try again.";
    }
});
