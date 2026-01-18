const API_URL = "https://cold-email-generator-z0n5.onrender.com/";

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
  .then(data => {
    document.getElementById("output").textContent = data.email;
  })
  .catch(() => {
    document.getElementById("output").textContent =
      "Error connecting to backend";
  });
}
