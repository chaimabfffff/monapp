var ajouterArticleBtn = document.getElementById("ajouterArticleBtn");
var ajouterArticleModal = document.getElementById("ajouterArticleModal");
var closeBtn = document.getElementsByClassName("close")[0];

ajouterArticleBtn.onclick = function() {
ajouterArticleModal.style.display = "block";
}

// Fermer la modale lorsque l'utilisateur clique sur le bouton de fermeture
closeBtn.onclick = function() {
ajouterArticleModal.style.display = "none";
}

// Soumettre le formulaire d'ajout d'article
var ajouterArticleForm = document.getElementById("ajouterArticleForm");

ajouterArticleForm.addEventListener("submit", function(e) {
e.preventDefault();
// Récupérer les valeurs du formulaire
var titre = document.getElementById("titre").value;
var description = document.getElementById("description").value;
var date = document.getElementById("date").value;
// Effectuer les traitements nécessaires (par exemple, enregistrer les données dans une base de données)

// Fermer la modale après avoir ajouté l'article
ajouterArticleModal.style.display = "none";
});
