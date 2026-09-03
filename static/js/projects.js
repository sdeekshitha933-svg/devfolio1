document.addEventListener("DOMContentLoaded", () => {

    const projectCards =
        document.querySelectorAll(".project-card");


    // ==========================================
    // PROJECT HOVER EFFECT
    // ==========================================

    projectCards.forEach((card) => {

        card.addEventListener("mouseenter", () => {

            card.classList.add(
                "project-hover"
            );

        });


        card.addEventListener("mouseleave", () => {

            card.classList.remove(
                "project-hover"
            );

        });

    });


    // ==========================================
    // PROJECT IMAGE ERROR HANDLING
    // ==========================================

    const projectImages =
        document.querySelectorAll(
            ".project-image img"
        );


    projectImages.forEach((image) => {

        image.addEventListener(
            "error",
            () => {

                console.warn(
                    "Project image could not be loaded:",
                    image.src
                );

                image.style.display = "none";

            }
        );

    });


    console.log(
        `Projects loaded successfully: ${projectCards.length}`
    );

});