const loginBtn = document.getElementById("loginBtn");

loginBtn.addEventListener("click", () => {
      const id = document.getElementById("loginId").value.trim();
      const pw = document.getElementById("loginPw").value.trim();

      const storedId = localStorage.getItem("userId");
      const storedPw = localStorage.getItem("userPw");

      if (id === storedId && pw === storedPw) {
        alert("로그인성공");
      } else {
        alert("로그인실패");
      }
    });