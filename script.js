//Element References
const display = document.getElementById("display");
const historyBox = document.getElementById("historyBox");

//Display Functions
function append(value) {
  if (display.innerText === "0") {
    display.innerText = value;
  } else {
    display.innerText += value;
  }
}

function clearDisplay() {
  display.innerText = "0";
}

function deleteChar() {
  if (display.innerText.length > 1) {
    display.innerText = display.innerText.slice(0, -1);
  } else {
    display.innerText = "0";
  }
}

//Calculation
function calculate() {
  try {
    let expression = display.innerText.replace("%", "/100");
    let result = eval(expression);
    if (!Number.isInteger(result)) {
      result = result.toFixed(2);
    }
    const equation =
      display.innerText.replace(/([+\-*/])/g, " $1 ") + " = " + result;
    display.innerText = result;
    saveToHistory(equation);
  } catch {
    display.innerText = "Error";
  }
}

//History Functions
function saveToHistory(entry) {
  let history = JSON.parse(localStorage.getItem("calcHistory")) || [];
  history.push(entry);
  localStorage.setItem("calcHistory", JSON.stringify(history));
}

function showHistory() {
  let history = JSON.parse(localStorage.getItem("calcHistory")) || [];
  historyBox.innerHTML =
    history.length === 0
      ? "No History Found"
      : history
          .reverse()
          .map((h) => `<div>${h}</div>`)
          .join("");
}

function clearHistory() {
  localStorage.removeItem("calcHistory");
  historyBox.innerHTML = "History Cleaned";
}

//Keyboard Support
document.addEventListener("keydown", function (event) {
  const key = event.key;

  if (!isNaN(key) || key === ".") {
    append(key);
  } else if (["+", "-", "*", "/"].includes(key)) {
    append(key);
  } else if (key === "Enter" || key === "=") {
    calculate();
  } else if (key === "Backspace") {
    deleteChar();
  } else if (key.toLowerCase() === "c") {
    clearDisplay();
  } else if (key === "%") {
    append("%");
  }
});
