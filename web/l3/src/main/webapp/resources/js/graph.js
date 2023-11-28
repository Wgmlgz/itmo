let calculator;

window.onload = function () {
  let rValue = parseFloat(document.getElementById('form:slider_input').value);
  let Y = document.getElementById('form:yInput');
  document.getElementById('form:slider_input').value = rValue;

  document.getElementById('plot').addEventListener('click', function (evt) {
    handleDesmosClick(evt);
  });

  Y.addEventListener('input', () => {
    if (!/^-?\d*\.?\d*$/g.test(Y.value))
      Y.value = (Y.value.match(/(^-|\d*\.?\d)/g) || []).join('');
  });
  //   setInterval(() => {
  drawGraph();
  //   }, 100);
};

function updateR() {
  console.log('Function updateR called!');
  // let rValue = parseFloat(document.getElementById('form:slider_input').value);
  // document.getElementById('form:slider_input').value = rValue;
  // console.log('Updated R value:', rValue);
  drawGraph();
}

function drawPointOnDesmos() {
  drawGraph();
  let lastCheckedPointX = parseFloat(
    document.getElementById('form:hiddenX').value
  );
  let lastCheckedPointY = parseFloat(
    document.getElementById('form:yInput').value
  );

  console.log(lastCheckedPointX, lastCheckedPointY);
  if (
    lastCheckedPointX < -4 ||
    lastCheckedPointX > 4 ||
    lastCheckedPointY < -5 ||
    lastCheckedPointY > 5
  ) {
    alert('Validation Failed, check coordinates!');
  }
}

function checkPoint() {
  executeCheckPoint();
}

function handleDesmosClick(e) {
  console.log(e);

  let { x, y } = getCursorPosition(e);
  const r = Number.parseFloat(
    document.getElementById('form:slider_input').value
  );

  x = ((x - 150) / 100) * r;
  y = ((-y + 300) / 100) * r;
  x = Math.round(x * 100) / 100;
  y = Math.round(y * 100) / 100;

  document.getElementById('form:hiddenX').value = x;
  document.getElementById('form:yInput').value = y;
  console.log(x, y, r);
  checkPoint();
}
