const images = [
  "https://picsum.photos/id/1015/300/200",
  "https://picsum.photos/id/1025/300/200",
  "https://picsum.photos/id/1035/300/200",
  "https://picsum.photos/id/1045/300/200",
];

let currentIndex = 0;
const slider = document.getElementById("slider");
const prevBtn = document.getElementById("prev");
const nextBtn = document.getElementById("next");
const indicator = document.getElementById("indicator");
const thumbnailsDiv = document.getElementById("thumbnails");

function updateSlider() {
  slider.src = images[currentIndex];
  indicator.textContent = `${currentIndex + 1} / ${images.length}`;

  document.querySelectorAll(".thumb").forEach((thumb, index) => {
    thumb.classList.toggle("active", index === currentIndex);
  });
}

images.forEach((img, index) => {
  const thumb = document.createElement("img");
  thumb.src = img;
  thumb.classList.add("thumb");
  thumb.addEventListener("click", () => {
    currentIndex = index;
    updateSlider();
  });
  thumbnailsDiv.appendChild(thumb);
});


slider.src = images[currentIndex];

prevBtn.addEventListener("click", () => {
  currentIndex--;
  if(currentIndex < 0) {
    currentIndex = images.length -1;
  } // 마지막으로 순환
  slider.src = images[currentIndex];
  updateSlider();
});

nextBtn.addEventListener("click", () => {
  currentIndex++;
  if(currentIndex >= images.length) {
    currentIndex = 0;
  } // 처음으로 순환
  slider.src = images[currentIndex];
  updateSlider();
});

updateSlider();
