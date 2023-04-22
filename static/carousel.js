const carouselSlide = document.querySelector('.carousel-slide');
const carouselImages = document.querySelectorAll('.carousel-slide img');

// Set initial position
let counter = 1;
carouselSlide.style.transform = `translateX(-${counter * 100 / 3}%)`;

// Button event listeners
document.querySelector('.carousel-next').addEventListener('click', () => {
  if (counter >= carouselImages.length - 1) return;
  carouselSlide.style.transition = 'transform 0.5s ease';
  counter++;
  carouselSlide.style.transform = `translateX(-${counter * 100 / 3}%)`;
});

document.querySelector('.carousel-prev').addEventListener('click', () => {
  if (counter <= 0) return;
  carouselSlide.style.transition = 'transform 0.5s ease';
  counter--;
  carouselSlide.style.transform = `translateX(-${counter * 100 / 3}%)`;
});

// Loop back to the beginning or end of carousel when reaching the last or first image
carouselSlide.addEventListener('transitionend', () => {
  if (carouselImages[counter].id === 'last-clone') {
    carouselSlide.style.transition = 'none';
    counter = carouselImages.length - 2;
    carouselSlide.style.transform = `translateX(-${counter * 100 / 3}%)`;
  }
  if (carouselImages[counter].id === 'first-clone') {
    carouselSlide.style.transition = 'none';
    counter = carouselImages.length - counter;
    carouselSlide.style.transform = `translateX(-${counter * 100 / 3}%)`;
  }
});
