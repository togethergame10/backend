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

// 폼 제출 시
document.getElementById("gameForm").addEventListener("submit", function (event) {
    var form1 = document.getElementById('form1');
    var form2 = document.getElementById('gameForm');

    // form1의 모든 입력 요소를 가져와서 form2에 추가
    for (var i = 0; i < form1.elements.length; i++) {
        var element = form1.elements[i];
        if (element.type === 'text') {
            var clone = element.cloneNode(true);
            clone.type = "hidden";
            form2.appendChild(clone);
        }
    }

    input_situation = document.getElementById('situation');
    input_situation.value = document.querySelector("#group3 .option.selected").value;
    input_place = document.getElementById('place');
    input_place.value = document.querySelector("#group4 .option.selected").value;
    input_game_type = document.getElementById('game_type');
    input_game_type.value = document.querySelector("#group5 .option.selected").value;

    if (form2.checkValidity()) {
        form2.submit();
    } else {
        alert("에러 발생");
        event.preventDefault();
    }
});

// 파일 업로드 관련
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
