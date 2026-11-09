// Mobile menu toggle
document.addEventListener("click", (e) => {
  if (e.target.closest(".menu-toggle")) {
    document.querySelector(".nav").classList.toggle("open");
  }
});

// Avatar fallback: if the image is missing, keep the pink circle
document.querySelectorAll("img[data-avatar]").forEach((img) => {
  img.addEventListener("error", () => { img.removeAttribute("src"); img.alt = ""; });
});

const DATA_URL = (document.body.dataset.root || "") + "data/series-videos.json";
const PAGE_SIZE = 12;

function videoId(url) {
  const m = url.match(/\/video\/(\d+)/);
  return m ? m[1] : null;
}

async function loadData() {
  const res = await fetch(DATA_URL, { cache: "no-cache" });
  return res.json();
}

// Series overview: fill in episode counts
async function initOverview() {
  const counts = document.querySelectorAll("[data-count]");
  if (!counts.length) return;
  const data = await loadData();
  counts.forEach((el) => {
    const s = data.series.find((x) => x.slug === el.dataset.count);
    if (s) el.textContent = s.videos.length + (s.videos.length === 1 ? " episode" : " episodes");
  });
}

// Single series page: render the video grid
async function initSeries() {
  const grid = document.getElementById("videos");
  if (!grid) return;
  const data = await loadData();
  const s = data.series.find((x) => x.slug === grid.dataset.slug);
  if (!s) return;

  const total = s.videos.length;
  document.getElementById("count").textContent = total + (total === 1 ? " episode" : " episodes");

  // Episode numbers are fixed by the oldest-first order in the JSON
  const items = s.videos.map((url, i) => ({ url, ep: i + 1 }));
  let order = "oldest";
  let shown = PAGE_SIZE;
  const moreBtn = document.getElementById("more");

  function render() {
    const list = order === "oldest" ? items : [...items].reverse();
    grid.innerHTML = list.slice(0, shown).map((v) => {
      const id = videoId(v.url);
      return `<div class="video">
        <div class="frame"><iframe loading="lazy" src="https://www.tiktok.com/player/v1/${id}?rel=0&description=0" allow="encrypted-media; fullscreen; picture-in-picture" allowfullscreen title="${s.name} episode ${v.ep}"></iframe></div>
        <div class="ep"><span>Ep ${v.ep}</span><a href="${v.url}" target="_blank" rel="noopener">Open on TikTok</a></div>
      </div>`;
    }).join("");
    moreBtn.style.display = shown >= list.length ? "none" : "inline-block";
  }

  document.querySelectorAll("[data-order]").forEach((b) => {
    b.addEventListener("click", () => {
      order = b.dataset.order;
      shown = PAGE_SIZE;
      document.querySelectorAll("[data-order]").forEach((x) => x.classList.toggle("on", x === b));
      render();
    });
  });
  moreBtn.addEventListener("click", () => { shown += PAGE_SIZE; render(); });
  render();
}

initOverview();
initSeries();

// Contact form: submit without leaving the page
const form = document.getElementById("contact");
if (form) {
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const status = document.getElementById("form-status");
    status.textContent = "Sending...";
    try {
      const res = await fetch(form.action, { method: "POST", body: new FormData(form), headers: { Accept: "application/json" } });
      const json = await res.json();
      if (json.success) { form.reset(); status.textContent = "Thanks. I'll get back to you soon."; }
      else { status.textContent = "Something went wrong. Please DM me on Instagram instead."; }
    } catch {
      status.textContent = "Something went wrong. Please DM me on Instagram instead.";
    }
  });
}
