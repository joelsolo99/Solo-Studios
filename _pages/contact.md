---
layout: default
title: "Contact Us"
permalink: /contact/
---

<link rel="stylesheet" href="{{ '/assets/css/form.css' | relative_url }}">
<link rel="stylesheet" href="{{ '/assets/css/contact.css' | relative_url }}">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<main class="contact-page">

  <section class="contact-hero-section">

    <div class="contact-hero-section__media" aria-hidden="true">
      <video
        autoplay
        muted
        loop
        playsinline
        class="contact-hero-section__video"
      >
        <source
          src="{{ '/assets/video/services-loop.mp4' | relative_url }}"
          type="video/mp4"
        >
        Your browser does not support the video tag.
      </video>

      <div class="contact-hero-section__overlay"></div>
    </div>

    <div class="contact-hero-section__inner">
      <div class="contact-hero-section__copy">

        <p class="contact-hero-section__eyebrow">
          Plan your event
        </p>

        <h1>
          Tell us what you’re planning
        </h1>

        <p class="contact-hero-section__intro">
          Whether you are booking live sax, a DJ set, or the full party atmosphere,
          send over a few details and we’ll help you find the right fit.
        </p>

        <div
          class="contact-hero-section__badges"
          aria-label="Popular enquiry types"
        >
          <span>Weddings</span>
          <span>Private parties</span>
          <span>Corporate events</span>
          <span>Power Hour</span>
        </div>

      </div>
    </div>

  </section>


  <section class="contact-planner-section" id="contact-us">

    <div class="contact-planner-section__inner">

      <div class="contact-planner-section__content">

        <p class="contact-planner-section__eyebrow">
          Quick enquiry
        </p>

        <h2>
          Check availability
        </h2>

        <p>
          Share the basics about your event and we’ll come back with the best option
          for your plans.
        </p>


        <div
          class="contact-planner-section__details"
          aria-label="What to include in your enquiry"
        >

          <div class="contact-detail-card">
            <span class="contact-detail-card__label">01</span>

            <h3>
              Date and venue
            </h3>

            <p>
              Let us know when and where the event is happening so we can check
              availability and advise on setup.
            </p>
          </div>


          <div class="contact-detail-card">
            <span class="contact-detail-card__label">02</span>

            <h3>
              Event style
            </h3>

            <p>
              Tell us whether it is a wedding, party, corporate event,
              charity event, or something else.
            </p>
          </div>


          <div class="contact-detail-card">
            <span class="contact-detail-card__label">03</span>

            <h3>
              Atmosphere
            </h3>

            <p>
              If you know the kind of energy you want, relaxed, polished,
              Ibiza-style, or full dancefloor, include that too.
            </p>
          </div>

          <div class="contact-detail-card">
            <span class="contact-detail-card__label">04</span>

            <h3>
              We'll guide you through the rest
            </h3>

            <p>
              Every event is different. We'll use the information you provide to suggest the most suitable setup and package.
            </p>
          </div>

        </div>

      </div>


      <div class="contact-form-panel">

        <div class="contact-form-panel__header">

          <p class="contact-form-panel__eyebrow">
            Start here
          </p>

          <h2>
            Enquiry form
          </h2>

          <p>
            Tell us a little about the day and we’ll reply as soon as possible.
          </p>

        </div>


        <form id="contact-form" class="contact-form" novalidate>

          <input
            type="text"
            name="from_name"
            placeholder="Your Name"
            required
          >


          <select
            name="event_type"
            id="event_type"
            required
            style="display:none"
          >
            <option value="" disabled selected>
              Type of Event
            </option>

            <option value="Wedding">Wedding</option>
            <option value="Birthday">Birthday</option>
            <option value="Private Party">Private Party</option>
            <option value="Corporate Event">Corporate Event</option>
            <option value="Charity Event">Charity Event</option>
            <option value="Power Hour">Power Hour</option>
            <option value="Other">Other</option>
          </select>


          <div
            class="custom-select-wrapper"
            tabindex="0"
            aria-haspopup="listbox"
            aria-expanded="false"
            role="combobox"
            aria-label="Type of Event"
          >

            <div
              id="custom-select-selected"
              class="custom-select-selected"
            >
              Type of Event
            </div>


            <ul
              id="custom-select-list"
              class="custom-select-list"
              role="listbox"
            >

              <li role="option" data-value="Wedding">
                Wedding
              </li>

              <li role="option" data-value="Birthday">
                Birthday
              </li>

              <li role="option" data-value="Private Party">
                Private Party
              </li>

              <li role="option" data-value="Corporate Event">
                Corporate Event
              </li>

              <li role="option" data-value="Charity Event">
                Charity Event
              </li>

              <li role="option" data-value="Power Hour">
                Power Hour
              </li>

              <li role="option" data-value="Other">
                Other
              </li>

            </ul>

          </div>


          <input
            type="text"
            name="event_date"
            placeholder="Date of Event, if known"
          >


          <input
            type="text"
            name="location"
            placeholder="Event Location or Venue"
          >


          <input
            type="email"
            name="from_email"
            placeholder="Your Email Address"
            required
          >


          <textarea
            name="message"
            placeholder="Tell us about your event..."
            required
          ></textarea>


          <input
            type="hidden"
            name="subject"
            value="Contact page enquiry"
          >


          <input
            type="text"
            name="website"
            style="display:none"
            tabindex="-1"
            autocomplete="off"
          >


          <button type="submit">
            Send Enquiry
          </button>

        </form>
        <div
          id="thank-you"
          class="thank-you-message"
          style="display:none"
        >
          <h3>
            Thank you
          </h3>

          <p>
            Your enquiry has been sent. We’ll be in touch soon.
          </p>
        </div>

      </div>

    </div>

  </section>


  <section class="contact-direct-section">

    <div class="contact-direct-section__inner">

      <div class="contact-direct-section__copy">

        <p class="contact-direct-section__eyebrow">
          Prefer email?
        </p>

        <h2>
          Contact Solo Studios directly
        </h2>

        <p>
          If you’d rather send a message from your own inbox, email us with your
          date, venue, and event type.
        </p>

      </div>


      <a
        href="mailto:events@solostudios.uk"
        class="contact-direct-section__link"
      >
        events@solostudios.uk
      </a>

    </div>

  </section>

</main>


<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>


<script>
document.addEventListener("DOMContentLoaded", () => {

  emailjs.init("brJTI5NcxOOq3ZeV3");


  const wrapper = document.querySelector(".custom-select-wrapper");
  const selected = document.getElementById("custom-select-selected");
  const list = document.getElementById("custom-select-list");
  const nativeSelect = document.getElementById("event_type");
  const contactForm = document.getElementById("contact-form");


  if (wrapper && selected && list && nativeSelect) {

    const options = list.querySelectorAll("li");


    function closeSelect() {
      wrapper.setAttribute("aria-expanded", "false");
      list.style.display = "none";
    }


    function openSelect() {
      wrapper.setAttribute("aria-expanded", "true");
      list.style.display = "block";
    }


    wrapper.addEventListener("click", () => {

      const expanded =
        wrapper.getAttribute("aria-expanded") === "true";

      expanded ? closeSelect() : openSelect();

    });


    wrapper.addEventListener("keydown", (event) => {

      if (event.key === "Enter" || event.key === " ") {

        event.preventDefault();

        const expanded =
          wrapper.getAttribute("aria-expanded") === "true";

        expanded ? closeSelect() : openSelect();

      }


      if (event.key === "Escape") {
        closeSelect();
      }

    });


    options.forEach((option) => {


      option.addEventListener("click", (event) => {

        event.stopPropagation();


        selected.textContent = option.textContent;

        nativeSelect.value = option.dataset.value;


        options.forEach((opt) =>
          opt.setAttribute("aria-selected", "false")
        );


        option.setAttribute(
          "aria-selected",
          "true"
        );


        closeSelect();

      });


      option.addEventListener("keydown", (event) => {

        if (event.key === "Enter" || event.key === " ") {

          event.preventDefault();

          option.click();

        }

      });


    });


    document.addEventListener("click", (event) => {

      if (!wrapper.contains(event.target)) {
        closeSelect();
      }

    });

  }



  function setSubmitState(form, isSending) {

    const submitButton =
      form.querySelector('button[type="submit"]');


    if (!submitButton) return;


    if (isSending) {

      submitButton.dataset.originalText =
        submitButton.textContent.trim();

      submitButton.disabled = true;

      submitButton.textContent =
        "Sending...";

    } else {

      submitButton.disabled = false;

      submitButton.textContent =
        submitButton.dataset.originalText ||
        "Send Enquiry";

    }

  }



  function getFieldValue(form, fieldName) {

    const field =
      form.querySelector(`[name="${fieldName}"]`);


    return field
      ? field.value.trim()
      : "";

  }



  if (contactForm) {

    contactForm.addEventListener("submit", function(event) {

      event.preventDefault();


      const honeypot =
        this.querySelector('input[name="website"]');


      if (honeypot && honeypot.value) {

        console.log(
          "Honeypot triggered - not sending"
        );

        return;

      }



      if (!nativeSelect || !nativeSelect.value) {

        alert(
          "Please select the type of event."
        );

        return;

      }



      const subjectField =
        this.querySelector('input[name="subject"]');


      const eventType =
        getFieldValue(
          this,
          "event_type"
        );


      const eventDate =
        getFieldValue(
          this,
          "event_date"
        );


      const location =
        getFieldValue(
          this,
          "location"
        );



      if (subjectField) {

        subjectField.value =
          [
            eventType,
            eventDate,
            location
          ]
          .filter(Boolean)
          .join(" - ");

      }



      setSubmitState(
        this,
        true
      );



      emailjs
        .sendForm(
          "service_pdrbr2j",
          "template_iw7f4ro",
          this
        )

        .then(() => {

          this.style.display = "none";


          const thankYouMessage =
            document.querySelector(
              "#contact-us .thank-you-message"
            );


          if (thankYouMessage) {

            thankYouMessage.style.display =
              "block";

          }

        })


        .catch((error) => {

          console.error(
            "EmailJS error:",
            error
          );


          alert(
            "Error sending message. Please try again later."
          );


          setSubmitState(
            this,
            false
          );

        });

    });

  }

});
</script>

