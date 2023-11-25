// 옵션 선택 시 실행될 함수
var groups = document.querySelectorAll(".select-options");
for (var i = 0; i < groups.length; i++) {
  groups[i].addEventListener("click", function (event) {
    var options = this.querySelectorAll(".option");
    for (var j = 0; j < options.length; j++) {
      options[j].classList.toggle("selected", false);
    }
    if (event.target.classList.contains("option")) {
      event.target.classList.toggle("selected", true);
    }
  });
}

document
  .getElementById("gameForm")
  .addEventListener("submit", function (event) {
    // 선택된 옵션 값 수집
    var selectedGroup1Min = document
      .getElementById("group1")
      .querySelector("input[type='text']").value;
    var selectedGroup1Max = document
      .getElementById("group1")
      .querySelectorAll("input[type='text']")[1].value;

    var selectedGroup2Min = document
      .getElementById("group2")
      .querySelector("input[type='text']").value;
    var selectedGroup2Max = document
      .getElementById("group2")
      .querySelectorAll("input[type='text']")[1].value;

    var selectedGroup3 = document.querySelector(
      "#group3 .option.selected"
    ).value;

    var selectedGroup4 = document.querySelector(
      "#group4 .option.selected"
    ).value;

    var selectedGroup5 = document.querySelector(
      "#group5 .option.selected"
    ).value;

    var selectedGroup6 = document.querySelector(
      "#group6 .option.selected"
    ).value;

    // 폼 데이터에 추가
    var formData = new FormData(document.getElementById("gameForm"));
    formData.append("selectedGroup1Min", selectedGroup1Min);
    formData.append("selectedGroup1Max", selectedGroup1Max);

    formData.append("selectedGroup2Min", selectedGroup2Min);
    formData.append("selectedGroup2Max", selectedGroup2Max);

    formData.append("selectedGroup3", selectedGroup3);
    formData.append("selectedGroup4", selectedGroup4);
    formData.append("selectedGroup5", selectedGroup5);
    formData.append("selectedGroup6", selectedGroup6);

    // 서버에 폼 데이터 전송
    fetch("{% url 'your_form_submission_url' %}", {
      method: "POST",
      body: formData,
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        // 서버 응답 처리
        console.log(data);
      })
      .catch((error) => {
        console.error("에러:", error);
      });

    // 기본 제출 동작 방지
    event.preventDefault();
  });

// Get the file input element
var fileInput = document.getElementById("file");

// Get the upload-name input element
var uploadNameInput = document.querySelector(".upload-name");

// Add a change event listener to the file input
fileInput.addEventListener("change", function () {
  // Get the selected file
  var selectedFile = fileInput.files[0];

  // Set the value of the upload-name input to the file name
  if (selectedFile) {
    uploadNameInput.value = selectedFile.name;
  } else {
    // If no file is selected, clear the upload-name input
    uploadNameInput.value = "";
  }
});

// Get the file input element
var fileInput = document.getElementById("file");

// Get the upload-name input element
var uploadNameInput = document.querySelector(".upload-name");

// Get the cancelFile button
var cancelFileButton = document.getElementById("cancelFile");

// Add a click event listener to the cancelFile button
cancelFileButton.addEventListener("click", function () {
  // Reset the file input by cloning and replacing it
  var newFileInput = fileInput.cloneNode(true);
  fileInput.parentNode.replaceChild(newFileInput, fileInput);

  // Clear the upload-name input
  uploadNameInput.value = "";
});
