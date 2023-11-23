function deletePlaylist() {
  if (confirm("플레이리스트를 삭제하시겠습니까?") == true) {
    //확인
    location.href = `delete/`;

  } else {
    //취소

    return false;
  }
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
