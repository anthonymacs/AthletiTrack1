const CACHE_NAME = "athletitrack-cache-v1";
const ASSETS_TO_CACHE = [
  "/",
  "/static/css/style.css",    // update path to your CSS
  "/static/js/app.js",        // update path to your JS
  "/static/icons/icon-192x192.png",
  "/static/icons/icon-512x512.png"
];

// Install Event
self.addEventListener("install", (event) => {
  console.log("Service Worker installing...");
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS_TO_CACHE);
    })
  );
  self.skipWaiting(); // activate immediately
});

// Activate Event
self.addEventListener("activate", (event) => {
  console.log("Service Worker activated.");
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            return caches.delete(key);
          }
        })
      )
    )
  );
});

// Fetch Event
self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );
});
