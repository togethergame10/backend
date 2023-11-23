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

function deletePost() {
  if (confirm("게시글을 삭제하시겠습니까??") == true) {
    //확인

    document.removefrm.submit();
  } else {
    //취소

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
    tempInput.value = href;

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
    alert("링크가 클립보드에 복사되었습니다.");
  } else {
    // If the button is not inside an <a> element
    alert("링크를 복사할 수 없습니다.");
  }
}
