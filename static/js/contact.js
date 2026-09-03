document.addEventListener("DOMContentLoaded", () => {

    const contactForm =
        document.getElementById("contactForm");

    const formMessage =
        document.getElementById("formMessage");


    // ==========================================
    // CHECK FORM
    // ==========================================

    if (!contactForm || !formMessage) {

        console.log(
            "Contact form elements not found."
        );

        return;
    }


    // ==========================================
    // FORM SUBMIT
    // ==========================================

    contactForm.addEventListener(
        "submit",
        async (event) => {

            event.preventDefault();


            // ==================================
            // GET FORM VALUES
            // ==================================

            const name =
                document
                    .getElementById("name")
                    .value
                    .trim();


            const email =
                document
                    .getElementById("email")
                    .value
                    .trim();


            const message =
                document
                    .getElementById("message")
                    .value
                    .trim();


            // ==================================
            // VALIDATION
            // ==================================

            if (!name) {

                formMessage.textContent =
                    "Please enter your name.";

                return;
            }


            if (!email) {

                formMessage.textContent =
                    "Please enter your email.";

                return;
            }


            if (!message) {

                formMessage.textContent =
                    "Please enter your message.";

                return;
            }


            // ==================================
            // EMAIL VALIDATION
            // ==================================

            const emailPattern =
                /^[^\s@]+@[^\s@]+\.[^\s@]+$/;


            if (!emailPattern.test(email)) {

                formMessage.textContent =
                    "Please enter a valid email.";

                return;
            }


            // ==================================
            // SENDING
            // ==================================

            formMessage.textContent =
                "Sending...";


            try {

                const response =
                    await fetch(
                        "/api/contact",
                        {
                            method: "POST",

                            headers: {
                                "Content-Type":
                                    "application/json"
                            },

                            body: JSON.stringify({
                                name: name,
                                email: email,
                                message: message
                            })
                        }
                    );


                const result =
                    await response.json();


                // ==================================
                // SUCCESS
                // ==================================

                if (
                    response.ok &&
                    result.success
                ) {

                    formMessage.textContent =
                        result.message;

                    contactForm.reset();

                }


                // ==================================
                // SERVER ERROR
                // ==================================

                else {

                    formMessage.textContent =
                        result.message ||
                        "Unable to send message.";

                }


            } catch (error) {

                console.error(
                    "Contact form error:",
                    error
                );


                formMessage.textContent =
                    "Something went wrong. Please try again.";

            }

        }
    );


    console.log(
        "Devfolio contact.js loaded successfully 📩"
    );

});