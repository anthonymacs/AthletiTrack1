// Register the service worker
if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    navigator.serviceWorker
      .register("/static/js/service-worker.js")
      .then((reg) => console.log("Service Worker registered:", reg.scope))
      .catch((err) => console.error("Service Worker registration failed:", err));
  });
}

// Handle install prompt
let deferredPrompt;
const installBtn = document.getElementById("installBtn");

// Hide the button initially
if (installBtn) installBtn.style.display = "none";

window.addEventListener("beforeinstallprompt", (e) => {
  e.preventDefault();
  deferredPrompt = e;
  console.log("beforeinstallprompt fired");

  if (installBtn) {
    installBtn.style.display = "block";
    installBtn.removeAttribute("disabled");
  }
});

if (installBtn) {
  installBtn.addEventListener("click", async () => {
    if (!deferredPrompt) {
      console.log("No install prompt available yet");
      return;
    }

    deferredPrompt.prompt();
    const { outcome } = await deferredPrompt.userChoice;
    console.log(`User response to install prompt: ${outcome}`);

    // Reset the prompt
    deferredPrompt = null;

    // Hide button after user’s choice
    installBtn.style.display = "none";
  });
}
