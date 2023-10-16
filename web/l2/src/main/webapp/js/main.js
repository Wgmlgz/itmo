let canvas, ctx, form, table;
let old_values = [];

const validateForm = e => {
  console.log(form);
  const x = parseFloat(form.elements.x.value);
  const y = parseFloat(form.elements.y.value);
  const r = parseFloat(form.elements.r.value);

  if (
    isNaN(x) ||
    isNaN(y) ||
    isNaN(r) ||
    x < -5 ||
    x > 5 ||
    y < -5 ||
    y > 5 ||
    ![1, 2, 3, 4, 5].includes(r)
  ) {
    alert('Wrong Input');
    e.preventDefault();
  }
};

const setX = e => {
  const x = parseFloat(e.innerHTML);
  console.log(x);
  document.getElementById('x').value = x;

  const buttons = document.querySelectorAll('.btn');
  buttons.forEach(btn => {
    if (btn.innerHTML === String(x)) {
      btn.classList.add('btn-selected');
    } else {
      btn.classList.remove('btn-selected');
    }
  });
  updatePlot();
};

window.onload = () => {
  table = document.getElementById('result-table');
};

$(function () {
  function isNumeric(n) {
    return !isNaN(parseFloat(n)) && isFinite(n);
  }

  function validateX() {
    const X_MIN = -3;
    const X_MAX = +3;
    let xField = $('#x-textinput');
    let numX = xField.val().trim().replace(',', '.');

    xField.val(numX);
    if (isNumeric(numX) && numX > X_MIN && numX < X_MAX) {
      xField.removeClass('text-error');
      return true;
    } else {
      xField.addClass('text-error');
      return false;
    }
  }
  function validateR() {
    if ($('.r-radio').is(':checked')) {
      $('.rbox-label').removeClass('box-error');
      return true;
    } else {
      $('.rbox-label').addClass('box-error');
      return false;
    }
  }
  function validateY() {
    const Y_VALUES = ['-2', '-1.5', '-1', '-0.5', '0', '0.5', '1', '1.5', '2'];
    let selector = document.getElementById('y');
    let ySelector = $('#r-textinput');
    let numY = selector.options[selector.selectedIndex].text
      .trim()
      .replace(',', '.');
    if (isNumeric(numY) && (numY in Y_VALUES || (numY >= -2 && numY <= 2))) {
      ySelector.removeClass('text-error');
      return true;
    } else {
      ySelector.addClass('text-error');
      return false;
    }
  }
  function validateForm() {
    return validateX() & validateY() & validateR();
  }
});

const clearBtn = document.getElementById('resetBtn');
clearBtn.addEventListener('click', async e => {
  e.preventDefault();

  for (var i = 1; i < table.rows.length; ) {
    table.deleteRow(i);
  }
  const res = await fetch('clear');
  drawGraph();
});

const inputForm = document.getElementById('input-form');
inputForm.addEventListener('submit', async e => {
  try {
    const myFormData = new FormData(e.target);
    e.preventDefault();
    const res = await fetch(
      'checkArea?' + new URLSearchParams(myFormData).toString()
    );
    const { results } = await res.json();

    console.log(table);
    for (var i = 1; i < table.rows.length; ) {
      table.deleteRow(i);
    }
    results.forEach(({ x, y, r, currTime, execTime, hitResult }) => {
      const row = table.insertRow(-1);
      console.log(hitResult);
      row.insertCell(-1).innerHTML = String(x);
      row.insertCell(-1).innerHTML = String(y);
      row.insertCell(-1).innerHTML = String(r);
      row.insertCell(-1).innerHTML = String(currTime);
      row.insertCell(-1).innerHTML = String(execTime);
      row.insertCell(-1).innerHTML = hitResult ? '✅' : '❌';
    });
  } catch (e) {
    alert('invalid data ❌❌❌😱😱😱');
  }
});

document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('plot').addEventListener('click', drawPoint);
});
