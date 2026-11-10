// Mobile menu toggle
document.addEventListener("click", (e) => {
  if (e.target.closest(".menu-toggle")) document.querySelector(".nav").classList.toggle("open");
});

// Click-to-load TikTok player: nothing is loaded from TikTok until the visitor clicks
document.addEventListener("click", (e) => {
  const btn = e.target.closest(".lite button");
  if (!btn) return;
  const box = btn.parentElement;
  const frame = document.createElement("iframe");
  frame.src = `https://www.tiktok.com/player/v1/${box.dataset.id}?autoplay=1&rel=0&description=0`;
  frame.allow = "autoplay; encrypted-media; fullscreen; picture-in-picture";
  frame.allowFullscreen = true;
  frame.title = btn.getAttribute("aria-label") || "TikTok video";
  box.replaceChildren(frame);
});

// Sort toggle on series pages (episodes are already in the HTML, oldest first)
document.querySelectorAll("[data-order]").forEach((b) => {
  b.addEventListener("click", () => {
    const list = document.getElementById("ep-list");
    const want = b.dataset.order;
    const current = list.dataset.order || "oldest";
    if (want !== current) {
      [...list.children].reverse().forEach((li) => list.appendChild(li));
      list.dataset.order = want;
    }
    document.querySelectorAll("[data-order]").forEach((x) => x.classList.toggle("on", x === b));
  });
});
