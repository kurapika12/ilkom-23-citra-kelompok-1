// JavaScript untuk  upload file
const uploadArea = document.getElementById("uploadArea");
const fileInput = document.getElementById("image");
const fileInfo = document.getElementById("fileInfo");
const uploadForm = document.getElementById("uploadForm");
const submitBtn = document.querySelector(".submit-btn");

// 1. Hilangkan event click dari uploadArea
uploadArea.addEventListener("click", (e) => {
  // Biarkan hanya label yang menangani klik
  if (
    e.target === uploadArea ||
    e.target.classList.contains("upload-icon") ||
    e.target.tagName === "P"
  ) {
    fileInput.click();
  }
});

// 2. Pastikan label tidak memicu dua kali
const fileLabel = document.querySelector(".file-label");
fileLabel.addEventListener("click", (e) => {
  e.stopPropagation(); // Menghentikan event bubbling ke uploadArea
});

// 3. Handle perubahan file
fileInput.addEventListener("change", (e) => {
  if (fileInput.files.length) {
    fileInfo.textContent = `File dipilih: ${fileInput.files[0].name}`;
  }
});

// 4. Drag and drop functionality
uploadArea.addEventListener("dragover", (e) => {
  e.preventDefault();
  uploadArea.style.borderColor = "#4361ee";
  uploadArea.style.backgroundColor = "rgba(67, 97, 238, 0.05)";
});

uploadArea.addEventListener("dragleave", () => {
  uploadArea.style.borderColor = "#dee2e6";
  uploadArea.style.backgroundColor = "transparent";
});

uploadArea.addEventListener("drop", (e) => {
  e.preventDefault();
  uploadArea.style.borderColor = "#dee2e6";
  uploadArea.style.backgroundColor = "transparent";

  if (e.dataTransfer.files.length) {
    fileInput.files = e.dataTransfer.files;
    fileInfo.textContent = `File dipilih: ${e.dataTransfer.files[0].name}`;
  }
});

// 5. Cegah double submit
uploadForm.addEventListener("submit", function (e) {
  submitBtn.disabled = true;
  submitBtn.textContent = "Memproses...";
});
