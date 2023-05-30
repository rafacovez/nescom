<template>
  <ComponentLayout id="contactSection">
    <h3>Envíanos un correo</h3>
    <form action="">
      <div class="form-group">
        <label class="label-name" for="name" :class="{ focused: isFocusedName }"
          >Nombre:</label
        >
        <input
          class="input-name"
          type="text"
          id="name"
          name="name"
          autocomplete="off"
          required
          @focus="isFocusedName = true"
          @blur="isFocusedName = false"
        />
      </div>
      <div class="form-group">
        <label
          class="label-email"
          for="email"
          :class="{ focused: isFocusedEmail }"
          >Correo:</label
        >
        <input
          class="input-email"
          type="email"
          id="email"
          name="email"
          autocomplete="off"
          required
          @focus="isFocusedEmail = true"
          @blur="isFocusedEmail = false"
        />
      </div>
      <div class="form-group">
        <label
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
          @focus="isFocusedMessage = true"
          @blur="isFocusedMessage = false"
        ></textarea>
      </div>
      <PrimaryButton class="submit-button">
        <input type="submit" value="Enviar" />
      </PrimaryButton>
    </form>
  </ComponentLayout>
</template>

<script>
import ComponentLayout from "@/layouts/ComponentLayout.vue";
import PrimaryButton from "./PrimaryButton.vue";

export default {
  name: "ContactSection",
  components: {
    ComponentLayout,
    PrimaryButton,
  },
  data() {
    return {
      isFocusedName: false,
      isFocusedEmail: false,
      isFocusedMessage: false,
    };
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
textarea {
  outline: none;
  border: 1px solid var(--gray);
  background-color: var(--white);
  border-radius: 2px;
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
</style>
