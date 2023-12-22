let canvas, ctx, form, table;
let old_values = [];

const validateForm = (e) => {
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

const setX = (e) => {
  const x = parseFloat(e.innerHTML);
  console.log(x);
  document.getElementById('x').value = x;

  const buttons = document.querySelectorAll('.btn');
  buttons.forEach((btn) => {
    if (btn.innerHTML === String(x)) {
      btn.classList.add('btn-selected');
    } else {
      btn.classList.remove('btn-selected');
    }
  });
  updatePlot();
};

const updatePlot = () => {
  console.log(form);
  const x = parseFloat(form.elements.x.value);
  const y = parseFloat(form.elements.y.value);
  const r = parseFloat(form.elements.r.value);
  /** @type {HTMLCanvasElement} */

  // const ctx = canvas.getContext("2d");
  if (!ctx) return;

  ctx.clearRect(0, 0, canvas.width, canvas.height);

  const scale = 130;
  const offset = 200;
  const fix = (t) => t * scale + offset;
  const fixY = (t) => -t * scale + offset;
  const fixS = (t) => t * scale;
  const line = (r_x, r_y, r_xx, r_yy) => {
    console.log(r_x, r_y, r_xx, r_yy);

    let x = fix(r_x);
    let y = fixY(r_y);
    let xx = fix(r_xx);
    let yy = fixY(r_yy);
    // [y, yy] = [y, yy].map(t => t *= -1)
    // console.log(x, y, xx, yy)
    // ([x, y, xx, yy] = [x, y, xx, yy].map(t => t * 200 + 250))
    ctx.beginPath(); // Start a new path
    ctx.moveTo(x, y); // Move the pen to (30, 50)
    ctx.lineTo(xx, yy); // Draw a line to (150, 100)
    ctx.stroke(); // Render the path
  };

  ctx.fillStyle = 'rgb(50, 150, 255)';
  ctx.fillRect(fix(0), fixY(0), fixS(1), fixS(1));

  ctx.beginPath();
  ctx.moveTo(fix(0), fixY(0));
  ctx.arc(fix(0), fixY(0), fixS(0.5), Math.PI / 2, Math.PI);
  ctx.closePath();
  ctx.fill();

  ctx.beginPath();
  ctx.moveTo(fix(0), fixY(0));
  ctx.lineTo(fix(-1), fixY(0));
  ctx.lineTo(fix(0), fixY(1));
  ctx.fill();

  ctx.fillStyle = '#000';
  line(-1.2, 0, 1.2, 0);
  line(1.2, 0, 1.15, 0.02);
  line(1.2, 0, 1.15, -0.02);

  line(0, -1.2, 0, 1.2);
  line(0, 1.2, 0.02, 1.15);
  line(0, 1.2, -0.02, 1.15);

  line(0.02, -1, -0.02, -1);
  line(0.02, -0.5, -0.02, -0.5);
  line(0.02, 0.5, -0.02, 0.5);
  line(0.02, 1, -0.02, 1);

  line(-1, 0.02, -1, -0.02);
  line(-0.5, 0.02, -0.5, -0.02);
  line(0.5, 0.02, 0.5, -0.02);
  line(1, 0.02, 1, -0.02);

  ctx.font = '20px serif';
  ctx.textBaseline = 'middle';
  ctx.textAlign = 'start';

  ctx.fillText(`Y`, fix(0.1), fixY(1.2));
  ctx.fillText(`${r}`, fix(0.1), fixY(1));
  ctx.fillText(`${r}`, fix(0.1), fixY(0.5));
  ctx.fillText(`-${r / 2}`, fix(0.1), fixY(-0.5));
  ctx.fillText(`-${r}`, fix(0.1), fixY(-1));

  ctx.textBaseline = 'alphabetic';
  ctx.textAlign = 'center';

  ctx.fillText(`X`, fix(1.2), fixY(0.1));
  ctx.fillText(`${r}`, fix(1), fixY(0.1));
  ctx.fillText(`${r / 2}`, fix(0.5), fixY(0.1));
  ctx.fillText(`-${r / 2}`, fix(-0.5), fixY(0.1));
  ctx.fillText(`-${r}`, fix(-1), fixY(0.1));

  

  ctx.fillStyle = '#006600';
  old_values.forEach(({ x, y }) => {
    ctx.fillRect(fix(x / r), fixY(y / r), 5, 5);
  });


  ctx.fillStyle = '#ff5555';

  ctx.fillRect(fix(x / r), fixY(y / r), 5, 5);
};

window.onload = () => {
  canvas = document.getElementById('canvas');
  form = document.getElementById('form');
  table = document.getElementById('table');
  ctx = canvas.getContext('2d');

  form.oninput = () => updatePlot();
  form.onsubmit = async (e) => {
    e.preventDefault();
    const { x, y, r, result, timestamp, exec } = await fetch('check.php', {
      method: 'post',
      body: new FormData(form),
    }).then((res) => res.json());
    old_values.push({ x: Number(x), y: Number(y) });
    row = table.insertRow(1);
    row.insertCell(0).innerHTML = x;
    row.insertCell(1).innerHTML = y;
    row.insertCell(2).innerHTML = r;
    row.insertCell(3).innerHTML = result;
    row.insertCell(4).innerHTML = timestamp;
    row.insertCell(5).innerHTML = exec;
  };
  updatePlot();
};
