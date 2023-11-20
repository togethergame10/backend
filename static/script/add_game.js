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
document.getElementById("gameForm").addEventListener("submit", function (event) {
  // 선택된 옵션 값 수집
  var selectedGroup1Min = document.getElementById("group1").querySelector("input[type='text']").value;
  var selectedGroup1Max = document.getElementById("group1").querySelectorAll("input[type='text']")[1].value;
  // 다른 select-buttons에서 필요한 경우 더 많은 변수 추가

  // 폼 데이터에 추가
  var formData = new FormData(document.getElementById("gameForm"));
  formData.append("selectedGroup1Min", selectedGroup1Min);
  formData.append("selectedGroup1Max", selectedGroup1Max);
  // 다른 select-buttons에서 필요한 경우 더 많은 변수 추가

  // 서버에 폼 데이터 전송
  fetch("{% url 'your_form_submission_url' %}", {
    method: "POST",
    body: formData,
  })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      // 서버 응답 처리
      console.log(data);
    })
    .catch(error => {
      console.error("에러:", error);
    });

  // 기본 제출 동작 방지
  event.preventDefault();
});
