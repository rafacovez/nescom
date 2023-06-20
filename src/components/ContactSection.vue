<template>
  <ComponentLayout class="contact-section">
    <div class="contact-section__text">
      <h3>Envíanos un correo</h3>
      <form ref="form" @submit.prevent="submitForm">
        <div class="form-group">
          <label
            v-show="!inputValueName"
            class="label-name"
            for="name"
            :class="{ focused: isFocusedName }"
            >Nombre:</label
          >
          <input
            class="input-name"
            type="text"
            id="name"
            name="user_name"
            autocomplete="off"
            required
            v-model="inputValueName"
            @focus="isFocusedName = true"
            @blur="isFocusedName = false"
          />
        </div>
        <div class="form-group">
          <label
            v-show="!inputValueEmail"
            class="label-email"
            for="email"
            :class="{ focused: isFocusedEmail }"
            >Correo:</label
          >
          <input
            class="input-email"
            type="email"
            id="email"
            name="user_email"
            autocomplete="off"
            required
            v-model="inputValueEmail"
            @focus="isFocusedEmail = true"
            @blur="isFocusedEmail = false"
          />
        </div>
        <div class="form-group">
          <label
            v-show="!inputValueMessage"
            class="label-message"
            for="message"
            :class="{ focused: isFocusedMessage }"
            >Mensaje:</label
          >
          <textarea
            class="input-message"
            id="message"
            name="message"
            autocomplete="off"
            required
            v-model="inputValueMessage"
            @focus="isFocusedMessage = true"
            @blur="isFocusedMessage = false"
          ></textarea>
        </div>
        <PrimaryButton class="submit-button">
          <input type="submit" value="Enviar" />
        </PrimaryButton>
      </form>
    </div>
    <div class="contact-section__illustration">
      <BusinessIllustration />
    </div>
  </ComponentLayout>
</template>

<script>
import ComponentLayout from "@/layouts/ComponentLayout.vue";
import PrimaryButton from "./PrimaryButton.vue";
import BusinessIllustration from "../assets/illustrations/BusinessIllustration.vue";
import emailjs from "emailjs-com";

export default {
  name: "ContactSection",
  components: {
    ComponentLayout,
    PrimaryButton,
    BusinessIllustration,
  },
  data() {
    return {
      isFocusedName: false,
      isFocusedEmail: false,
      isFocusedMessage: false,
      inputValueName: "",
      inputValueEmail: "",
      inputValueMessage: "",
    };
  },
  methods: {
    submitForm() {
      emailjs
        .sendForm(
          process.env.VUE_APP_EMAILJS_SERVICE_ID,
          process.env.VUE_APP_EMAILJS_TEMPLATE_ID,
          this.$refs.form,
          process.env.VUE_APP_EMAILJS_USER_ID,
          {
            name: this.inputValueName,
            email: this.inputValueEmail,
            message: this.inputValueMessage,
          }
        )
        .then(
          (result) => {
            console.log("SUCCESS!", result.text);
          },
          (error) => {
            console.log("FAILED...", error.text);
          }
        );

      // Reset form field
      this.inputValueName = "";
      this.inputValueEmail = "";
      this.inputValueMessage = "";

      this.isFocusedName = false;
      this.isFocusedEmail = false;
      this.isFocusedMessage = false;
    },
  },
};
</script>

<style>
form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin: 2rem 0;
}

.form-group {
  position: relative;
  background-color: var(--white);
}

.form-group > label {
  color: var(--gray);
  font-weight: var(--font-bold);
  position: absolute;
  inset: 0;
  pointer-events: none;
  transition: all ease-out 0.2s;
}

.form-group > * {
  width: 100%;
  font-size: calc(var(--font-size) * 0.8);
  padding: 1rem;
  margin: 1.5rem 0 0 0;
}

.form-group > input,
.form-group > textarea {
  outline: none;
  border: 1px solid var(--gray);
  background-color: var(--white);
  border-radius: var(--border-radius-sm);
  touch-action: manipulation;
}

.form-group > input:focus,
textarea:focus {
  border: 1px solid blue;
}

.form-group > label.focused {
  padding: 0;
  margin: 0;
  color: var(--black);
  font-size: calc(var(--font-size) * 0.9);
}

.submit-button {
  margin: 1.5rem 0 0 0;
}

.submit-button > input {
  background: none;
  border: none;
  color: var(--white);
  pointer-events: none;
}

.contact-section__illustration {
  display: none;
}

@media only screen and (min-width: 1080px) {
  .contact-section {
    display: flex;
    flex-direction: row-reverse;
    justify-content: space-between;
    align-items: center;
    gap: 8rem;
  }

  .contact-section__text {
    flex-basis: 70%;
  }

  .contact-section__illustration {
    display: block;
    flex-basis: 30%;
    max-width: 250px;
  }
}
</style>
