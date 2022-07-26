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
let div1 = document.getElementById("div1");
let div2 = document.getElementById("div2");
function showhideForm(showform) {
   if (showform == "Event") {
      div1.style.display = 'block';
      div2.style.display = 'none';
   }
   else if (showform == "Content") {
      div2.style.display = 'block';
      div1.style.display = 'none';
   }
   else if (showform == "All") {
      div2.style.display = 'block';
      div1.style.display = 'block';
   }
}
let div3 = document.getElementById("div3");
let div4 = document.getElementById("div4");
let div5 = document.getElementById("div5");

function showhideTechForm(showform1) {
   if (showform1 == "gd") {
      div3.style.display = 'block';
      div4.style.display = 'none';
      div5.style.display = 'none';
   }
   else if (showform1 == "webd") {
      div4.style.display = 'block';
      div3.style.display = 'none';
      div5.style.display = 'none';
   }
   else if (showform1 == "video") {
      div4.style.display = 'none';
      div3.style.display = 'none';
      div5.style.display = 'block';
   }
}
//timer

// const myTime = document.querySelector('h1');
const myTime = document.getElementById('countdown');
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
function update(progressBar, value) {
   value = Math.round(value);
   progressBar.querySelector(".progressfill").style.width = `${value}%`;
   progressBar.querySelector(".progresstext").textContent = `${value}%`;
}
