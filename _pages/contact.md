---
layout: default
title: "Contact Us"
permalink: /contact/
---

<link rel="stylesheet" href="{{ '/assets/css/form.css' | relative_url }}">
<link rel="stylesheet" href="{{ '/assets/css/contact.css' | relative_url }}">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<div class="contact-page">
  <div class="contact-page__inner">
    <header class="contact-page__hero">
      <p class="contact-page__eyebrow">Contact</p>
      <h1>Tell us about your event</h1>
      <p class="contact-page__intro">
        Whether you are planning a wedding, private party, or event, send over a few details
        and we’ll point you in the right direction.
      </p>
    </header>

    <section class="contact-page__guidance" aria-label="What to include in your enquiry">
      <div class="contact-page__guidance-grid">
        <article class="contact-page__guidance-card">
          <h2>Date and venue</h2>
          <p>
            Let us know when the event is happening and where it will take place.
            That helps us advise on the right setup and timings.
          </p>
        </article>

        <article class="contact-page__guidance-card">
          <h2>Type of event</h2>
          <p>
            Weddings, private parties, corporate events, and celebrations all need slightly different
            music, so it helps to know the shape of the day.
          </p>
        </article>

        <article class="contact-page__guidance-card">
          <h2>Atmosphere and timing</h2>
          <p>
            If you already know the sort of feel you want, or which part of the day you need music for,
            include that too and we can point you in the right direction.
          </p>
        </article>
      </div>
    </section>
  </div>

  <section id="contact-us" class="contact-section contact-section--page">
    <div class="container">
      <h2 class="section-title">Enquiry form</h2>
      <p class="section-subtitle">
        Share the basics and we’ll come back with the best option for your plans.
      </p>

      <form id="contact-form" novalidate>
        <input type="text" name="from_name" placeholder="Your Name" required />

        <select name="event_type" id="event_type" required style="display:none">
          <option value="" disabled selected>Type of Event</option>
          <option value="Wedding">Wedding</option>
          <option value="Birthday">Birthday</option>
          <option value="Corporate Event">Corporate Event</option>
          <option value="Charity Event">Charity Event</option>
          <option value="Other">Other</option>
        </select>

        <div
          class="custom-select-wrapper"
          tabindex="0"
          aria-haspopup="listbox"
          aria-expanded="false"
          role="combobox"
          aria-owns="custom-select-list"
          aria-label="Type of Event"
        >
          <div id="custom-select-selected" class="custom-select-selected">Type of Event</div>
          <ul
            id="custom-select-list"
            class="custom-select-list"
            role="listbox"
            tabindex="-1"
            aria-activedescendant=""
          >
            <li role="option" data-value="Wedding" tabindex="0">Wedding</li>
            <li role="option" data-value="Birthday" tabindex="0">Birthday</li>
            <li role="option" data-value="Corporate Event" tabindex="0">Corporate Event</li>
            <li role="option" data-value="Charity Event" tabindex="0">Charity Event</li>
            <li role="option" data-value="Other" tabindex="0">Other</li>
          </ul>
        </div>

        <input
          type="text"
          name="event_date"
          placeholder="Date of Event (dd/mm/yyyy)"
          required
          pattern="\d{1,2}/\d{1,2}/\d{4}"
          title="Enter date as dd/mm/yyyy"
        />

        <input
          type="email"
          name="from_email"
          placeholder="Your Email Address"
          required
        />

        <textarea
          name="message"
          placeholder="Tell us about your event..."
          required
        ></textarea>

        <input
          type="text"
          name="website"
          style="display:none"
          tabindex="-1"
          autocomplete="off"
        />

        <button type="submit">Send Enquiry</button>
      </form>

      <div id="thank-you" style="display:none" class="thank-you-message">
        <h3>Thank you</h3>
        <p>Your enquiry has been sent. We’ll be in touch soon.</p>
      </div>
    </div>
  </section>

  <div class="contact-page__inner">
    <section class="contact-page__secondary">
      <div class="contact-page__secondary-inner">
        <p class="contact-page__secondary-eyebrow">Prefer email?</p>
        <p class="contact-page__secondary-text">
          You can also reach us directly at
          <a href="mailto:events@solostudios.uk">events@solostudios.uk</a>.
        </p>
      </div>
    </section>
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>
<script>
  emailjs.init("brJTI5NcxOOq3ZeV3");

  const wrapper = document.querySelector(".custom-select-wrapper");
  const selected = document.getElementById("custom-select-selected");
  const list = document.getElementById("custom-select-list");
  const nativeSelect = document.getElementById("event_type");
  const options = list.querySelectorAll("li");

  wrapper.addEventListener("click", () => {
    const expanded = wrapper.getAttribute("aria-expanded") === "true";
    wrapper.setAttribute("aria-expanded", !expanded);
    list.style.display = expanded ? "none" : "block";
  });

  options.forEach((option) => {
    option.addEventListener("click", () => {
      selected.textContent = option.textContent;
      nativeSelect.value = option.dataset.value;
      options.forEach((opt) => opt.setAttribute("aria-selected", "false"));
      option.setAttribute("aria-selected", "true");
      wrapper.setAttribute("aria-expanded", "false");
      list.style.display = "none";
    });
  });

  document.addEventListener("click", (e) => {
    if (!wrapper.contains(e.target)) {
      wrapper.setAttribute("aria-expanded", "false");
      list.style.display = "none";
    }
  });

  document.getElementById("contact-form").addEventListener("submit", function (e) {
    e.preventDefault();

    if (this.website.value) {
      console.log("Honeypot triggered - not sending");
      return;
    }

    if (!nativeSelect.value) {
      alert("Please select the type of event.");
      return;
    }

    this.subject = `${nativeSelect.value} ${this.event_date.value}`;

    emailjs
      .sendForm("service_pdrbr2j", "template_iw7f4ro", this)
      .then(() => {
        this.style.display = "none";
        document.querySelector("#contact-us .thank-you-message").style.display = "block";
      })
      .catch((error) => {
        console.error("EmailJS error:", error);
        alert("Error sending message. Please try again later.");
      });
  });
</script>
