const API_URL = "https://YOUR-RENDER-URL.onrender.com/generate";

const output = document.getElementById("output");

function typeText(text) {
  output.textContent = "";
  let i = 0;
  const interval = setInterval(() => {
    output.textContent += text[i];
    i++;
    if (i >= text.length) clearInterval(interval);
  }, 15);
}

function generateEmail() {
  fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      name: name.value,
      company: company.value,
      role: role.value,
      skills: skills.value,
      template_type: template.value
    })
  })
  .then(res => res.json())
  .then(data => typeText(data.email))
  .catch(() => output.textContent = "❌ Backend connection failed");
}

function copyEmail() {
  navigator.clipboard.writeText(output.textContent);
  alert("Email copied!");
}

function downloadPDF() {
  const blob = new Blob([output.textContent], { type: "text/plain" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "cold_email.txt";
  a.click();
}

document.getElementById("darkToggle").addEventListener("change", () => {
  document.body.classList.toggle("dark");
});
