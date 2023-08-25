<template>
  <ComponentLayout class="contact-section">
    <PopUpModal
      :modal-is-visible="modalIsVisible"
      @update:modal-is-visible="modalIsVisible = $event"
      ref="PopUpModal"
      class="sent"
    >
      <CheckIcon class="sent__check-icon" />
      <p class="sent__heading">¡Bien!</p>
      <p class="sent__paragraph">Su mensaje fue enviado exitosamente.</p>
    </PopUpModal>
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
      <img v-lazy="ContactIllustrationPath" alt="Contact via email" />
    </div>
  </ComponentLayout>
</template>

<script>
import ComponentLayout from "@/layouts/ComponentLayout.vue";
import PrimaryButton from "./PrimaryButton.vue";
import PopUpModal from "./PopUpModal.vue";
import ContactIllustration from "@/assets/contact.webp";
import { CheckIcon } from "@heroicons/vue/20/solid";
import db from "@/firebase/init.js";
import { collection, addDoc } from "firebase/firestore";

export default {
  name: "ContactSection",
  components: {
    ComponentLayout,
    PrimaryButton,
    PopUpModal,
    CheckIcon,
  },
  data() {
    return {
      ContactIllustrationPath: ContactIllustration,
      isFocusedName: false,
      isFocusedEmail: false,
      isFocusedMessage: false,
      inputValueName: "",
      inputValueEmail: "",
      inputValueMessage: "",
      modalIsVisible: false,
    };
  },
  methods: {
    async submitForm() {
      // "users" collection reference
      const colRef = collection(db, "users");

      // data to send
      const userData = {
        name: this.inputValueName,
        email: this.inputValueEmail,
        message: this.inputValueMessage,
      };

      // create document and return reference to it
      await addDoc(colRef, userData);

      // reset form field
      this.inputValueName = "";
      this.inputValueEmail = "";
      this.inputValueMessage = "";

      this.isFocusedName = false;
      this.isFocusedEmail = false;
      this.isFocusedMessage = false;

      this.$refs.PopUpModal.showPopUp();
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
  margin-top: 1.5rem;
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
.form-group > textarea:focus {
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

.sent {
  text-align: center;
}

.sent__check-icon {
  position: absolute;
  top: 0;
  transform: translateY(-50%);
  left: 0;
  right: 0;
  margin: 0 auto;
  width: 50px;
  background-color: var(--green);
  color: var(--white);
  border-radius: 50%;
  padding: 5px;
}

.sent__heading {
  font-size: calc(var(--font-size) * 1.5);
  font-weight: var(--font-bold);
  margin-top: 1rem;
}

.sent__paragraph {
  font-size: calc(var(--font-size) * 0.8);
  margin: 1rem 0;
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
    flex-basis: 40%;
    max-width: 500px;
  }
}
</style>
