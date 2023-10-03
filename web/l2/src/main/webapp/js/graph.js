const drawGraph = function () {
  const canvas = document.getElementById('plot');
  const plot_canvas = document.getElementById('plot');

  const ctx = plot_canvas.getContext('2d');
  let canvWidth = plot_canvas.width;
  console.log(form);
  const table = document.getElementById('result-table');
  var row = table.rows[table.rows.length - 1];
  var x = parseFloat(row.cells[0].innerText);
  var y = parseFloat(row.cells[1].innerText);
  var r = parseFloat(row.cells[2].innerText);

  console.log(x, y, r);
  /** @type {HTMLCanvasElement} */

  // const ctx = canvas.getContext("2d");
  if (!ctx) return;

  ctx.clearRect(0, 0, canvas.width, canvas.height);

  const scale = 100;
  const offset = 150;
  const fix = (t) => t * scale + offset;
  const fixY = (t) => -t * scale + offset;
  const fixS = (t) => t * scale;
  const line = (r_x, r_y, r_xx, r_yy) => {
    // console.log(r_x, r_y, r_xx, r_yy);

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
  ctx.fillRect(fix(0), fixY(0), fixS(0.5), fixS(-1));

  ctx.beginPath();
  ctx.moveTo(fix(0), fixY(0));
  ctx.arc(fix(0), fixY(0), fixS(0.5), Math.PI * 0, Math.PI / 2);
  ctx.closePath();
  ctx.fill();

  ctx.beginPath();
  ctx.moveTo(fix(0), fixY(0));
  ctx.lineTo(fix(-1), fixY(0));
  ctx.lineTo(fix(0), fixY(-1));
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

  [...table.rows].forEach((row) => {
    console.log(row)
    // var row = table.rows[table.rows.length - 1];
    var x = parseFloat(row.cells[0].innerText);
    var y = parseFloat(row.cells[1].innerText);
    var r = parseFloat(row.cells[2].innerText);
    var hit = (row.cells[5].innerText) === 'true';
    console.log(x, y, r, hit)

    if (hit) {
        ctx.fillStyle = '#55ff55';
    } else {
        ctx.fillStyle = '#ff5555';
    }

    ctx.fillRect(fix(x / r), fixY(y / r), 5, 5);
  });

  //   ctx.fillStyle = '#006600';
  //   old_values.forEach(({ x, y }) => {
  //     ctx.fillRect(fix(x / r), fixY(y / r), 5, 5);
  //   });
};

document.addEventListener('DOMContentLoaded', function () {
  var errorMessageText = document.getElementById('error-Table');
  var url = window.location.pathname;
  if (url !== '/lab2/') {
    window.history.replaceState(
      { errorMessage: errorMessageText.innerText },
      document.title,
      window.location.host + '/lab2/'
    );
  }

  errorMessageText.innerText = history.state.errorMessage;

  const table = document.getElementById('result-table');
  var row = table.rows[table.rows.length - 1];
  var x = parseFloat(row.cells[0].innerText);
  var y = parseFloat(row.cells[1].innerText);
  var r = parseFloat(row.cells[2].innerText);

  const plot_canvas = document.getElementById('plot');

  const plot_context = plot_canvas.getContext('2d');
  let canvWidth = plot_canvas.width;
  plot_context.strokeStyle = '#ffffff';
  plot_context.beginPath();
  // plot_context.moveTo(canvWidth/2, canvWidth/2);
  plot_context.arc(
    canvWidth / 2 + 100 * (x / r),
    canvWidth / 2 - 100 * (y / r),
    10,
    0,
    2 * Math.PI
  );
  // plot_context.lineTo(canvWidth/2, canvWidth/2);
  plot_context.fillStyle = '#ff2ff2';
  plot_context.fill();
  plot_context.closePath();
  console.log('plot finished');
});

function drawPoint(e) {
  const r = $('input[name="r"]:checked').val();
  if (r === undefined) {
    // document.querySelector('#error-log').textContent = "Choose r!";
  } else {
    const point = getCursorPosition(e);
    const plot_canvas = document.getElementById('plot');
    const plot_context = plot_canvas.getContext('2d');
    plot_context.beginPath();
    plot_context.rect(point.x, point.y, 5, 5);
    point.x = ((point.x - 150) / 100) * r;
    point.y = ((-point.y + 150) / 100) * r;
    plot_context.fillStyle = 'green';
    plot_context.fill();

    const params = { x: point.x.toFixed(2), y: point.y.toFixed(2), r: r };
    window.location.replace('/lab2/process' + formatParams(params));

    // $.ajax({
    //     type: "GET",
    //     url: "/process",
    //     data:
    //         {
    //             x: point.x.toFixed(2),
    //             y: point.y.toFixed(2),
    //             r: r
    //         },
    //     success: data => {
    //
    //
    //     },
    //     error: (jqXHR, textStatus, errorThrown) =>
    //         document.querySelector('#error-log').innerHTML = "Ошибка HTTP: " + jqXHR.status + "(" + errorThrown + ")",
    //     dataType: "html"
    // });
  }
}

function getCursorPosition(e) {
  let x;
  let y;
  const plot_canvas = document.getElementById('plot');
  if (e.pageX !== undefined && e.pageY !== undefined) {
    x = e.pageX;
    y = e.pageY;
  } else {
    x =
      e.clientX +
      document.body.scrollLeft +
      document.documentElement.scrollLeft;
    y =
      e.clientY + document.body.scrollTop + document.documentElement.scrollTop;
  }
  return {
    x: x - plot_canvas.getBoundingClientRect().left,
    y: y - plot_canvas.getBoundingClientRect().top,
  };
}

function formatParams(params) {
  return (
    '?' +
    Object.keys(params)
      .map(function (key) {
        return key + '=' + encodeURIComponent(params[key]);
      })
      .join('&')
  );
}
