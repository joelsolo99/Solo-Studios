function initialiseReviewCarousels() {
  const carousels = document.querySelectorAll("[data-reviews-carousel]");

  carousels.forEach((carousel) => {
    if (carousel.dataset.carouselInitialised === "true") {
      return;
    }

    const viewport = carousel.querySelector("[data-review-viewport]");
    const previousButton = carousel.querySelector("[data-review-prev]");
    const nextButton = carousel.querySelector("[data-review-next]");

    if (!viewport || !previousButton || !nextButton) {
      return;
    }

    carousel.dataset.carouselInitialised = "true";

    const getScrollAmount = () => {
      const firstCard = viewport.querySelector(".review-card");
      const track = viewport.querySelector(".reviews-carousel__track");

      if (!firstCard || !track) {
        return viewport.clientWidth;
      }

      const trackStyles = window.getComputedStyle(track);
      const gap = parseFloat(trackStyles.columnGap || trackStyles.gap) || 16;

      return firstCard.offsetWidth + gap;
    };

    previousButton.addEventListener("click", () => {
      viewport.scrollBy({
        left: -getScrollAmount(),
        behavior: "smooth",
      });
    });

    nextButton.addEventListener("click", () => {
      viewport.scrollBy({
        left: getScrollAmount(),
        behavior: "smooth",
      });
    });
  });
}

function initialiseExpandableReviews() {
  const reviewCards = document.querySelectorAll(".review-card");

  reviewCards.forEach((card) => {
    if (card.dataset.expandInitialised === "true") {
      return;
    }

    card.dataset.expandInitialised = "true";
    card.setAttribute("tabindex", "0");
    card.setAttribute("role", "button");
    card.setAttribute("aria-expanded", "false");

    const toggleCard = () => {
      const isExpanded = card.classList.toggle("is-expanded");
      card.setAttribute("aria-expanded", isExpanded ? "true" : "false");
    };

    card.addEventListener("click", (event) => {
      if (event.target.closest("a")) {
        return;
      }

      toggleCard();
    });

    card.addEventListener("keydown", (event) => {
      if (event.target.closest("a")) {
        return;
      }

      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        toggleCard();
      }
    });
  });
}

document.addEventListener("DOMContentLoaded", () => {
  initialiseReviewCarousels();
  initialiseExpandableReviews();
});