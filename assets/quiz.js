// Reusable multiple-choice quiz.
// Markup: <div class="quiz"><div class="q" data-correct="2" data-why="Explanation">
//           <p>Question</p><button>A</button><button>B</button><button>C</button>
//         </div>...<p class="score"></p></div>
// First click locks the question (no retry: the first answer is the honest signal).
document.querySelectorAll(".quiz").forEach((quiz) => {
  const qs = quiz.querySelectorAll(".q");
  const score = quiz.querySelector(".score");
  let answered = 0, right = 0;
  qs.forEach((q) => {
    const buttons = q.querySelectorAll("button");
    const correct = Number(q.dataset.correct);
    const fb = document.createElement("div");
    fb.className = "feedback";
    q.appendChild(fb);
    buttons.forEach((b, i) => b.addEventListener("click", () => {
      buttons.forEach((x) => (x.disabled = true));
      buttons[correct].classList.add("right");
      const ok = i === correct;
      if (!ok) b.classList.add("wrong");
      fb.textContent = (ok ? "Correct. " : "Not quite. ") + (q.dataset.why || "");
      answered++; if (ok) right++;
      if (score) score.textContent = `${right} / ${answered} correct` + (answered === qs.length ? " — tell your teacher this score." : "");
    }));
  });
});
