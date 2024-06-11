<template>
  <ComponentLayout class="contact-section">
    <PopUpModal
      :modal-is-visible="modalIsVisible"
      @update:modal-is-visible="modalIsVisible = $event"
      ref="PopUpModal"
      class="sent"
    >
      <font-awesome-icon
        v-if="formWasSuccessful"
        icon="fas fa-check"
        class="sent__check-icon sent__check-icon--success"
      />
      <font-awesome-icon
        v-else
        icon="fas fa-exclamation"
        class="sent__check-icon sent__check-icon--error"
      />
      <div class="sent__wrapper">
        <img
          src="https://nescommedia.s3.us-east-2.amazonaws.com/brand/sent-message.webp"
          :alt="altText"
        />
        <p class="sent__heading">{{ heading }}</p>
        <p class="sent__paragraph">{{ paragraph }}</p>
      </div>
    </PopUpModal>
    <div class="contact-section__text">
      <h3 class="contact-section__heading">Envíanos un correo</h3>
      <form ref="form" @submit.prevent="sendEmail">
        <InputComponent
          :inputName="'Nombre'"
          :isRequired="true"
          :inputValue="inputValueName"
          @update:inputValue="(value) => (inputValueName = value)"
          :isFocused="isFocusedName"
          @update:isFocused="(value) => (isFocusedName = value)"
        />
        <InputComponent
          :inputName="'Correo'"
          :isRequired="true"
          :inputValue="inputValueEmail"
          @update:inputValue="(value) => (inputValueEmail = value)"
          :isFocused="isFocusedEmail"
          @update:isFocused="(value) => (isFocusedEmail = value)"
        />
        <InputComponent
          :inputName="'Mensaje'"
          :isRequired="true"
          :isTextarea="true"
          :inputValue="inputValueMessage"
          @update:inputValue="(value) => (inputValueMessage = value)"
          :isFocused="isFocusedMessage"
          @update:isFocused="(value) => (isFocusedMessage = value)"
        />
        <CheckboxComponent
          ref="checkboxComponent"
          :isChecked="isChecked"
          @update:checked="updateChecked"
          :checkboxText="'Acepto recibir actualizaciones sobre nuevo contenido a mi dirección de correo electrónico.'"
        />
        <CustomButton :isPrimary="true">
          <input class="submit-button" type="submit" value="Enviar" />
        </CustomButton>
      </form>
    </div>
    <div class="contact-section__illustration">
      <img
        src="https://nescommedia.s3.us-east-2.amazonaws.com/brand/contact.webp"
        alt="Contact via email"
      />
    </div>
  </ComponentLayout>
</template>

<script>
import ComponentLayout from "@/layouts/ComponentLayout.vue";
import CustomButton from "./CustomButton.vue";
import PopUpModal from "./PopUpModal.vue";
import CheckboxComponent from "./CheckboxComponent.vue";
import InputComponent from "./InputComponent.vue";
import axios from "axios";
import axiosInstance from "@/axios-instance";

export default {
  name: "ContactSection",
  data() {
    return {
      isFocusedName: false,
      isFocusedEmail: false,
      isFocusedMessage: false,
      inputValueName: "",
      inputValueEmail: "",
      inputValueMessage: "",
      modalIsVisible: false,
      formWasSuccessful: false,
      isChecked: true,
    };
  },
  components: {
    ComponentLayout,
    InputComponent,
    CustomButton,
    PopUpModal,
    CheckboxComponent,
  },
  computed: {
    iconClass() {
      return this.formWasSuccessful
        ? "sent__check-icon sent__check-icon--success"
        : "sent__check-icon sent__check-icon--error";
    },
    altText() {
      return this.formWasSuccessful ? "Message sent" : "Error sending message";
    },
    heading() {
      return this.formWasSuccessful ? "¡Bien!" : "¡Oh, oh...!";
    },
    paragraph() {
      return this.formWasSuccessful
        ? "Su mensaje fue enviado exitosamente."
        : "Lo sentimos, pero hubo un error al enviar su correo. Por favor, vuelva a intentarlo más tarde.";
    },
  },
  methods: {
    updateChecked(newValue) {
      this.isChecked = newValue;
    },

    // sendEmail() {
    //   // Construct the request body
    //   const requestBody = {
    //     displayName: this.inputValueName,
    //     email: this.inputValueEmail,
    //     message: this.inputValueMessage,
    //     receiveEmails: this.isChecked,
    //     role: "notify",
    //   };

    //   Promise.all([
    //     // Sending email
    //     fetch(`${process.env.VUE_APP_URL}/api/emails`, {
    //       method: "POST",
    //       headers: {
    //         "Content-Type": "application/json",
    //       },
    //       body: JSON.stringify(requestBody),
    //     }),

    //     // Creating user if checked
    //     this.isChecked
    //       ? fetch(`${process.env.VUE_APP_URL}/api/users/createOrUpdateUser`, {
    //           method: "POST",
    //           headers: {
    //             "Content-Type": "application/json",
    //           },
    //           body: JSON.stringify(requestBody),
    //         })
    //       : Promise.resolve({ ok: true }), // Resolve immediately if not creating a user
    //   ])
    //     .then(([emailResponse, userResponse]) => {
    //       if (!emailResponse.ok) throw new Error("Failed to send email");

    //       // Check user creation response, log errors but do not throw for duplicate user
    //       if (!userResponse.ok && userResponse.status !== 409) {
    //         console.error(
    //           "Failed to create user, status:",
    //           userResponse.status
    //         );
    //         // You might want to handle other non-critical errors differently here
    //       } else if (userResponse.status === 409) {
    //         console.error("Duplicate user found");
    //       }

    //       // Reset form fields
    //       this.inputValueName = "";
    //       this.inputValueEmail = "";
    //       this.inputValueMessage = "";
    //       this.isFocusedName = false;
    //       this.isFocusedEmail = false;
    //       this.isFocusedMessage = false;

    //       // Show success modal
    //       this.formWasSuccessful = true; // Set to true if email sent successfully
    //       this.modalIsVisible = true;
    //     })
    //     .catch((error) => {
    //       console.error("Operation failed:", error);
    //       this.formWasSuccessful = false;
    //       this.modalIsVisible = true;
    //     })
    //     .finally(() => {
    //       // Show modal in any case
    //       this.$refs.PopUpModal.showPopUp();
    //     });
    // },
    async sendEmail() {
      // Construct the request body
      const requestBody = {
        displayName: this.inputValueName,
        email: this.inputValueEmail,
        message: this.inputValueMessage,
        receiveEmails: this.isChecked,
        role: "notify",
      };

      try {
        const emailRequest = axiosInstance.post("/api/emails", requestBody);
        const userRequest = this.isChecked
          ? axiosInstance.post("/api/users/createOrUpdateUser", requestBody)
          : Promise.resolve({ status: 200 });

        const [emailResponse, userResponse] = await axios.all([
          emailRequest,
          userRequest,
        ]);

        if (emailResponse.status !== 200)
          throw new Error("Failed to send email");

        if (userResponse.status !== 200 && userResponse.status !== 409) {
          console.error("Failed to create user, status:", userResponse.status);
        } else if (userResponse.status === 409) {
          console.error("Duplicate user found");
        }

        // Reset form fields
        this.inputValueName = "";
        this.inputValueEmail = "";
        this.inputValueMessage = "";
        this.isFocusedName = false;
        this.isFocusedEmail = false;
        this.isFocusedMessage = false;

        // Show success modal
        this.formWasSuccessful = true;
        this.modalIsVisible = true;
      } catch (error) {
        console.error("Operation failed:", error);
        this.formWasSuccessful = false;
        this.modalIsVisible = true;
      } finally {
        // Show modal in any case
        this.$refs.PopUpModal.showPopUp();
      }
    },
  },
};
</script>

<style>
form {
  display: flex;
  gap: 1rem;
  flex-direction: column;
}

.contact-section__heading {
  margin-bottom: 2rem;
}

.submit-button {
  background: none;
  border: none;
  color: inherit;
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
  height: 50px;
  width: 50px;
  color: var(--white);
  border-radius: 50%;
  padding: 5px;
}

.sent__check-icon--success {
  background-color: var(--green);
}

.sent__check-icon--error {
  background-color: var(--red);
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
