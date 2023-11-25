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

  // Optional: You can add more functionality to handle form submission and playlist creation
  document
    .getElementById("playlistForm")
    .addEventListener("submit", function (e) {
      e.preventDefault();
      // Add logic to create a new playlist here
      // You can use JavaScript to send a request to the server or update the UI as needed
      // After creating the playlist, you may want to close the modal
      modal.style.display = "none";
    });
});

function deletePost(pk) {
  if (confirm("게시글을 삭제하시겠습니까??") == true) {
    //확인
    event.preventDefault();
    //document.removefrm.submit();

    location.href = `delete/${pk}`;
  } else {
    //취소
    event.preventDefault();
    return false;
  }
}

function copyLink(button) {
  // Get the closest <a> ancestor of the clicked button
  var listItem = button.closest("a");

  if (listItem) {
    // Get the href attribute of the <a> element
    var href = listItem.getAttribute("href");

    // Create a temporary input element to copy the text
    var tempInput = document.createElement("input");
    tempInput.value = "http://127.0.0.1:8000" + href;

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
    event.preventDefault();
    alert("링크가 클립보드에 복사되었습니다.");
  } else {
    // If the button is not inside an <a> element
    event.preventDefault();
    alert("링크를 복사할 수 없습니다.");
  }
}

function cancelAttachment() {
  // Reset the file input value to clear the selected file
  document.getElementById("thumbnailInput").value = "";
}

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
