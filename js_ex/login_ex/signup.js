const signupBtn = document.getElementById("signupBtn");

signupBtn.addEventListener("click", () => {

      const id = document.getElementById("signupId").value.trim();
      const pw = document.getElementById("signupPw").value.trim();

      if (!id || !pw) {
        alert("아이디와 비밀번호를 모두 입력하세요.");
        return;
      }

      localStorage.setItem("userId", id);
      localStorage.setItem("userPw", pw);

      alert("회원가입되었습니다! 로그인 화면으로 넘어갑니다.");

      window.location.href = "./signin.html";
    
}); 