const drawGraph = function () {
  console.log('drawing');
  const canvas = document.getElementById('plot');
  const plot_canvas = document.getElementById('plot');

  const ctx = plot_canvas.getContext('2d');
  let canvWidth = plot_canvas.width;

  const x_element = document.getElementById('form:hiddenX');
  const x = Number.parseFloat(x_element.value);

  const y_element = document.getElementById('form:yInput');
  const y = Number.parseFloat(y_element.value);

  const r_element = document.getElementById('form:slider_input');
  let r = Number.parseFloat(r_element.value);

  if (r > 3) r = 3;
  if (r < 1) r = 1;

  console.log(x, y, r);

  if (!ctx) return;

  ctx.clearRect(0, 0, canvas.width, canvas.height);

  const scale = 100;
  const offset = 150;
  const fix = (t) => t * scale + offset;
  const fixY = (t) => -t * scale + offset;
  const fixS = (t) => t * scale;
  const line = (r_x, r_y, r_xx, r_yy) => {
    let x = fix(r_x);
    let y = fixY(r_y);
    let xx = fix(r_xx);
    let yy = fixY(r_yy);
    ctx.beginPath(); // Start a new path
    ctx.moveTo(x, y); // Move the pen to (30, 50)
    ctx.lineTo(xx, yy); // Draw a line to (150, 100)
    ctx.stroke(); // Render the path
  };

  ctx.fillStyle = 'rgb(50, 150, 255)';
  ctx.fillRect(fix(0), fixY(0), fixS(-1), fixS(-1));

  ctx.beginPath();
  ctx.moveTo(fix(0), fixY(0));
  ctx.arc(fix(0), fixY(0), fixS(0.5), Math.PI * -0.5, Math.PI * 0);
  ctx.closePath();
  ctx.fill();

  ctx.beginPath();
  ctx.moveTo(fix(0), fixY(0));
  ctx.lineTo(fix(-1), fixY(0));
  ctx.lineTo(fix(0), fixY(-1));
  ctx.fill();

  ctx.strokeStyle = '#000';
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
  ctx.fillText(`${r / 2}`, fix(0.1), fixY(0.5));
  ctx.fillText(`-${r / 2}`, fix(0.1), fixY(-0.5));
  ctx.fillText(`-${r}`, fix(0.1), fixY(-1));

  ctx.textBaseline = 'alphabetic';
  ctx.textAlign = 'center';

  ctx.fillText(`X`, fix(1.2), fixY(0.1));
  ctx.fillText(`${r}`, fix(1), fixY(0.1));
  ctx.fillText(`${r / 2}`, fix(0.5), fixY(0.1));
  ctx.fillText(`-${r / 2}`, fix(-0.5), fixY(0.1));
  ctx.fillText(`-${r}`, fix(-1), fixY(0.1));

  const table = document.getElementById('form:results').children[0].children[0];
  // .firstChild()?.firstChild();
  // console.log(table);
  // console.log([...table.rows]);
  const drawHit = (x, y, hit) => {
    if (hit) {
      ctx.fillStyle = '#55ff55';
    } else {
      ctx.fillStyle = '#ff5555';
    }

    ctx.fillRect(fix(x / r), fixY(y / r), 5, 5);
  };
  // drawHit(x, y, true);

  [...table.rows].slice(2).forEach((row) => {
    if (!row.cells[1]) return;
    // var row = table.rows[table.rows.length - 1];

    var x = parseFloat(row.cells[0].innerText);
    var y = parseFloat(row.cells[1].innerText);
    var r = parseFloat(row.cells[2].innerText);
    var hit = row.cells[3].innerText === '✅';
    // console.log(x, y, r, hit);

    drawHit(x, y, hit);
  });
};

// async function drawPoint(e) {
//   const r = $('input[name="r"]:checked').val();
//   if (r === undefined) {
//   } else {
//     const point = getCursorPosition(e);
//     point.x = ((point.x - 150) / 100) * r;
//     point.y = ((-point.y + 150) / 100) * r;

//     const params = { x: point.x.toFixed(2), y: point.y.toFixed(2), r: r };

//     const res = await fetch(
//       'checkArea?' + new URLSearchParams(params).toString()
//     );
//     const { results } = await res.json();

//     console.log(table);
//     for (var i = 1; i < table.rows.length; ) {
//       table.deleteRow(i);
//     }
//     results.forEach(({ x, y, r, currTime, execTime, hitResult }) => {
//       const row = table.insertRow(-1);
//       console.log(hitResult);
//       row.insertCell(-1).innerHTML = String(x);
//       row.insertCell(-1).innerHTML = String(y);
//       row.insertCell(-1).innerHTML = String(r);
//       row.insertCell(-1).innerHTML = String(currTime);
//       row.insertCell(-1).innerHTML = String(execTime);
//       row.insertCell(-1).innerHTML = hitResult ? '✅' : '❌';
//     });

//     drawGraph();
//   }
// }

function getCursorPosition(e) {
  console.log(e);
  let x;
  let y;
  const plot_canvas = document.getElementById('plot');
  console.log(plot_canvas.getBoundingClientRect());

  // if (e.pageX !== undefined && e.pageY !== undefined) {
  x = e.pageX;
  y = e.pageY;
  // } else {
  // x =
  //   e.clientX + document.body.scrollLeft + document.documentElement.scrollLeft;
  // y = e.clientY + document.body.scrollTop + document.documentElement.scrollTop;
  // }
  return {
    x: x - plot_canvas.getBoundingClientRect().left,
    y: y - plot_canvas.getBoundingClientRect().top,
  };
}
