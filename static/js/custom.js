// Attendre que la page soit complètement chargée
document.addEventListener("DOMContentLoaded", function () {
    // Cibler la page login
    const loginPage = document.querySelector(".login");

    if (loginPage) {
        // Appliquer un style de fond
        loginPage.style.background = "linear-gradient(135deg, #4a90e2, #50c9c3)";
        loginPage.style.height = "100vh";
        loginPage.style.display = "flex";
        loginPage.style.justifyContent = "center";
        loginPage.style.alignItems = "center";
        loginPage.style.fontFamily = "'Roboto', sans-serif";

        // Cibler la boîte de connexion
        const loginBox = document.querySelector(".login-box");
        if (loginBox) {
            loginBox.style.background = "#ffffff";
            loginBox.style.padding = "40px 30px";
            loginBox.style.borderRadius = "10px";
            loginBox.style.boxShadow = "0 4px 10px rgba(0, 0, 0, 0.1)";
            loginBox.style.width = "100%";
            loginBox.style.maxWidth = "400px";
            loginBox.style.textAlign = "center";
        }

        // Cibler le logo
        const logo = document.querySelector("img");
        if (logo) {
            logo.style.width = "120px";
            logo.style.height = "auto";
            logo.style.marginBottom = "20px";
        }

        // Cibler les champs de formulaire
        const inputs = document.querySelectorAll(".form-control");
        inputs.forEach((input) => {
            input.style.borderRadius = "5px";
            input.style.border = "1px solid #ced4da";
            input.style.padding = "10px 15px";
            input.style.marginBottom = "15px";
            input.style.fontSize = "14px";

            // Effet de focus
            input.addEventListener("focus", function () {
                input.style.borderColor = "#50c9c3";
                input.style.boxShadow = "0 0 5px rgba(80, 201, 195, 0.5)";
                input.style.outline = "none";
            });

            input.addEventListener("blur", function () {
                input.style.borderColor = "#ced4da";
                input.style.boxShadow = "none";
            });
        });

        // Cibler le bouton de connexion
        const loginButton = document.querySelector(".btn-primary");
        if (loginButton) {
            loginButton.style.background = "#4a90e2";
            loginButton.style.border = "none";
            loginButton.style.padding = "10px 20px";
            loginButton.style.fontSize = "16px";
            loginButton.style.fontWeight = "600";
            loginButton.style.color = "#ffffff";
            loginButton.style.borderRadius = "5px";
            loginButton.style.transition = "background 0.3s ease";

            // Effet hover
            loginButton.addEventListener("mouseover", function () {
                loginButton.style.background = "#357abd";
            });

            loginButton.addEventListener("mouseout", function () {
                loginButton.style.background = "#4a90e2";
            });
        }

        // Cibler les liens
        const links = document.querySelectorAll(".login a");
        links.forEach((link) => {
            link.style.color = "#4a90e2";
            link.style.textDecoration = "none";
            link.style.fontSize = "14px";

            link.addEventListener("mouseover", function () {
                link.style.textDecoration = "underline";
            });

            link.addEventListener("mouseout", function () {
                link.style.textDecoration = "none";
            });
        });
    }
});
console.log("Script custom.js chargé !");
