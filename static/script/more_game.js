function toggleLike() {
  var likeButton = document.getElementById("likeButton");
  var likeImage = likeButton.querySelector("img");

  // Check the current state of the like button
  var isLiked = likeImage.src.includes("like.png");

  // Toggle the image source based on the current state
  likeImage.src = isLiked ? "../img/likefull.png" : "../img/like.png";
}

function deletePost() {
  if (confirm("게시글을 삭제하시겠습니까??") == true) {
    //확인
    window.location.href = "{% url 'game:delete' pk=target_game.pk %}";

    document.removefrm.submit();
  } else {
    //취소

    return false;
  }
}

function openModal() {
  var modal = document.getElementById("myModal");
  modal.style.display = "flex"; // 모달 표시
}

function closeModal() {
  var modal = document.getElementById("myModal");
  modal.style.display = "none"; // Hide the modal
}

function toggleButtonText(playlistId) {
  var button = document.getElementById(playlistId).nextElementSibling; // 형제 요소인 button
  var buttonText = button.innerText;

  // 텍스트를 변경하고 원래대로 되돌리기
  if (buttonText === "선택") {
    button.innerText = "취소";
    button.style.cssText = "background-color:rgba(122, 159, 118, 1)";
  } else {
    button.innerText = "선택";
    button.style.cssText = "background-color:rgba(187, 215, 184, 1))";
  }
}
