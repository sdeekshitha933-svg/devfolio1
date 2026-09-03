document.addEventListener("DOMContentLoaded", () => {

    const navLinks = document.querySelectorAll(".nav-link");
    const sections = document.querySelectorAll("section[id]");


    // ==========================================
    // SMOOTH NAVIGATION
    // ==========================================

    navLinks.forEach((link) => {

        link.addEventListener("click", (event) => {

            const href = link.getAttribute("href");

            if (!href || !href.includes("#")) {
                return;
            }

            const hash = href.substring(
                href.indexOf("#")
            );

            const target = document.querySelector(hash);

            if (!target) {
                return;
            }

            event.preventDefault();

            navLinks.forEach((item) => {
                item.classList.remove("active");
            });

            link.classList.add("active");

            target.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });

            history.replaceState(
                null,
                "",
                hash
            );
        });

    });


    // ==========================================
    // ACTIVE NAVIGATION WHILE SCROLLING
    // ==========================================

    if (sections.length > 0) {

        const observer = new IntersectionObserver(
            (entries) => {

                entries.forEach((entry) => {

                    if (!entry.isIntersecting) {
                        return;
                    }

                    const currentId =
                        entry.target.getAttribute("id");


                    navLinks.forEach((link) => {

                        const href =
                            link.getAttribute("href");

                        link.classList.remove("active");


                        if (
                            href &&
                            href.endsWith(
                                `#${currentId}`
                            )
                        ) {

                            link.classList.add("active");

                        }

                    });

                });

            },
            {
                threshold: 0.35
            }
        );


        sections.forEach((section) => {
            observer.observe(section);
        });

    }


    console.log(
        "Devfolio main.js loaded successfully 🚀"
    );

});