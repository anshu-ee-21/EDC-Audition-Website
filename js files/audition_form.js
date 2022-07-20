const loginText = document.querySelector(".title-text .login");
const loginForm = document.querySelector("form.login");
const loginBtn = document.querySelector("label.login");
const signupBtn = document.querySelector("label.signup");
const signupLink = document.querySelector("form .signup-link a");
signupBtn.onclick = (() => {
   loginForm.style.marginLeft = "-50%";
   loginText.style.marginLeft = "-50%";
});
loginBtn.onclick = (() => {
   loginForm.style.marginLeft = "0%";
   loginText.style.marginLeft = "0%";
});
signupLink.onclick = (() => {
   signupBtn.click();
   return false;
});

function showhideForm(showform) {
   if (showform == "Event") {
      document.getElementById("div1").style.display = 'block';
      document.getElementById("div2").style.display = 'none';
   }
   else if (showform == "Content") {
      document.getElementById("div2").style.display = 'block';
      document.getElementById("div1").style.display = 'none';
   }
   else if (showform == "All") {
      document.getElementById("div2").style.display = 'block';
      document.getElementById("div1").style.display = 'block';
   }
}

function showhideTechForm(showform1) {
   if (showform1 == "gd") {
      document.getElementById("div3").style.display = 'block';
      document.getElementById("div4").style.display = 'none';
      document.getElementById("div5").style.display = 'none';
   }
   else if (showform1 == "webd") {
      document.getElementById("div4").style.display = 'block';
      document.getElementById("div3").style.display = 'none';
      document.getElementById("div5").style.display = 'none';
   }
   else if (showform1 == "video") {
      document.getElementById("div4").style.display = 'none';
      document.getElementById("div3").style.display = 'none';
      document.getElementById("div5").style.display = 'block';
   }
}
//timer

const myTime = document.querySelector('h1');
// const myTime = document.getElementById('countdown');
let timeSecond = 3600;
const countDown = setInterval(() => {
   timeSecond--;
   displayTime(timeSecond);
   if (timeSecond <= 0) {
      clearInterval(countDown);
      myTime.innerHTML = "The Time is Up";
   }
}, 1000);
const bars = document.querySelector(".progress");
        function update(progressBar, value){
            value = Math.round(value);
            progressBar.querySelector(".progressfill").style.width = `${value}%`;
            progressBar.querySelector(".progresstext").textContent = `${value}%`;
        }
