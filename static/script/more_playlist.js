function deletePlaylist() {
  if (confirm("플레이리스트를 삭제하시겠습니까?") == true) {
    //확인
    location.href = `delete/`;

  } else {
    //취소

    return false;
  }
}

function collectPlaylist(collected) {
    location.href = `collect/`;
}

function deleteElement(pk) {
  if (confirm("플레이리스트 목록에서 삭제하시겠습니까?") == true) {
    //확인
    event.preventDefault();
    location.href = `remove_game/${pk}`;
  } else {
    //취소
    event.preventDefault();
    return false;
  }
}



function pageLink() {
  // Get the current URL
  var currentURL = window.location.href;

  // Create a temporary input element to copy the text
  var tempInput = document.createElement("input");
  tempInput.value = currentURL;

  // Append the input element to the body
  document.body.appendChild(tempInput);

  // Select the text in the input element
  tempInput.select();
  tempInput.setSelectionRange(0, 99999); /* For mobile devices */

  // Copy the text to the clipboard
  document.execCommand("copy");

  // Remove the temporary input element
  document.body.removeChild(tempInput);

  // Optionally, provide some feedback to the user
  alert("현재 페이지 주소가 클립보드에 복사되었습니다.");
}

document.addEventListener("DOMContentLoaded", function () {
  // Get the modal
  var modal = document.getElementById("myModal");

  // Get the button that opens the modal
  var btn = document.querySelector(".create-playlist button");

  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("close")[0];

  // When the user clicks the button, open the modal
  btn.onclick = function () {
    modal.style.display = "block";
  };

  // When the user clicks on <span> (x), close the modal
  span.onclick = function () {
    modal.style.display = "none";
  };

  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function (event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  };


});

function cancelAttachment() {
  // Reset the file input value to clear the selected file
  var thumbnailInput = document.getElementById("thumbnailInput");
  if (thumbnailInput) {
    thumbnailInput.value = "";
  }
}

document.addEventListener("DOMContentLoaded", function () {
  var fileInput = document.getElementById("file");
  var uploadNameInput = document.querySelector(".upload-name");
  var cancelFileButton = document.getElementById("cancelFile");

  // Add a change event listener to the file input
  if (fileInput) {
    fileInput.addEventListener("change", function () {
      var selectedFile = fileInput.files[0];
      if (selectedFile) {
        uploadNameInput.value = selectedFile.name;
      } else {
        uploadNameInput.value = "";
      }
    });
  }

  // Add a click event listener to the cancelFile button
  if (cancelFileButton) {
    cancelFileButton.addEventListener("click", function () {
      // Reset the file input by cloning and replacing it
      if (fileInput) {
        var newFileInput = fileInput.cloneNode(true);
        fileInput.parentNode.replaceChild(newFileInput, fileInput);

        // Clear the upload-name input
        uploadNameInput.value = "";
      }
    });
  }
});

function toggleButtonText() {
  var button = document.getElementById('addButton');
  if (button.textContent === '내 Playlist에 추가하기') {
    button.textContent = '추가됨! (재클릭 시 취소)';
  } else {
    button.textContent = '내 Playlist에 추가하기';
  }
}