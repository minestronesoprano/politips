const chosen_candidate = document.querySelectorAll(".candidate_option");

for(i = 0; i < chosen_candidate.length;i++) {
  chosen_candidate[i].addEventListener('click', (e) => {
    console.log("You clicked");
    var choice = e.currentTarget.id;
    console.log(choice);
  });
}
