const noteInput = document.getElementById("noteInput");
const saveBtn = document.getElementById("saveBtn");
const loadBtn = document.getElementById("loadBtn");
const clearBtn = document.getElementById("clearBtn");
const status = document.getElementById("status");

const STORAGE_KEY = "memo";

saveBtn.addEventListener("click", ()=>{
  const text = noteInput.value.trim();
  localStorage.setItem(STORAGE_KEY, text);
  status.textContent = "메모가 저장되었습니다!";
});

loadBtn.addEventListener("click", ()=>{
  const saved = localStorage.getItem(STORAGE_KEY);
  if(saved) {
    noteInput.value = saved;
    status.textContent = "저장된 메모를 불러왔습니다!";
  } else {
    status.textContent = "저장된 메모가 없습니다.";
  }
});

clearBtn.addEventListener("click", ()=>{
  localStorage.removeItem(STORAGE_KEY);
  noteInput.value = "";
  status.textContent = "메모가 삭제되었습니다.";
})

window.addEventListener("DOMContentLoaded", () => {
  const saved = localStorage.getItem(STORAGE_KEY);
  if(saved) {
    noteInput.value = saved;
    status.textContent = "저장된 메모를 자동으로 불러왔습니다.";
  }
});