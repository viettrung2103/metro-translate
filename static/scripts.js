document.addEventListener("DOMContentLoaded", () => {
  const translateBtn = document.getElementById("translate-btn");
  translateBtn.addEventListener("click", async () => {
    const inputText = document.getElementById("input-text").value;
    try {
      const response = await fetch("/translate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: inputText }),
      });
      const data = await response.json();
      document.getElementById("output-text").value = data.translation;
    } catch (error) {
      console.error("Translation error:", error);
    }
  });
});
