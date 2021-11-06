const stars = document.querySelector("#id_score");

if (stars) {
   const lab1 = Array.from(stars.querySelectorAll("label"));

   lab1.forEach((elem) => {
      let st = document.createElement("span");
      st.textContent = "\u{02605}";
      elem.appendChild(st);
   });

   const btn = document.querySelector("#paint");
   const rads = Array.from(stars.querySelectorAll("input[type=radio]"));
   const sps = Array.from(stars.querySelectorAll("input + span"));

   rads.forEach((item) => {
      item.addEventListener("change", () => {
         let score = 0;
         if (item.checked) {
            score = item.value;
            sps.forEach((item, i) => {
               if (i < score) {
                  item.classList.add("ok");
               } else {
                  item.classList.remove("ok");
               }
            });
         }
      });
   });
}
