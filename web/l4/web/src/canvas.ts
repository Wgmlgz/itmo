export const drawGraph = (
  x: number,
  y: number,
  r: number,
  results: { x: number; y: number; r: number; hit: boolean }[]
) => {
  console.log('drawing')
  const canvas = document.getElementById('canvas') as HTMLCanvasElement

  if (!canvas) throw new Error('No canvas?')

  const ctx = canvas.getContext('2d')

  if (r > 3) r = 3
  if (r < 1) r = 1

  console.log(x, y, r)

  if (!ctx) return

  ctx.clearRect(0, 0, canvas.width, canvas.height)

  const scale = 100
  const offset = 150
  const fix = (t: number) => t * scale + offset
  const fixY = (t: number) => -t * scale + offset
  const fixS = (t: number) => t * scale
  const line = (r_x: number, r_y: number, r_xx: number, r_yy: number) => {
    const x = fix(r_x)
    const y = fixY(r_y)
    const xx = fix(r_xx)
    const yy = fixY(r_yy)
    ctx.beginPath() // Start a new path
    ctx.moveTo(x, y) // Move the pen to (30, 50)
    ctx.lineTo(xx, yy) // Draw a line to (150, 100)
    ctx.stroke() // Render the path
  }

  ctx.fillStyle = '#fff'
  ctx.fillRect(0, 0, canvas.width, canvas.height)

  ctx.fillStyle = 'rgb(50, 150, 255)'
  ctx.fillRect(fix(0), fixY(0), fixS(1), fixS(-1))

  ctx.beginPath()
  ctx.moveTo(fix(0), fixY(0))
  ctx.arc(fix(0), fixY(0), fixS(0.5), Math.PI * 0.5, Math.PI * -1)
  ctx.closePath()
  ctx.fill()

  ctx.beginPath()
  ctx.moveTo(fix(0), fixY(0))
  ctx.lineTo(fix(-0.5), fixY(0))
  ctx.lineTo(fix(0), fixY(1))
  ctx.fill()

  ctx.strokeStyle = '#000'
  ctx.fillStyle = '#000'
  line(-1.2, 0, 1.2, 0)
  line(1.2, 0, 1.15, 0.02)
  line(1.2, 0, 1.15, -0.02)

  line(0, -1.2, 0, 1.2)
  line(0, 1.2, 0.02, 1.15)
  line(0, 1.2, -0.02, 1.15)

  line(0.02, -1, -0.02, -1)
  line(0.02, -0.5, -0.02, -0.5)
  line(0.02, 0.5, -0.02, 0.5)
  line(0.02, 1, -0.02, 1)

  line(-1, 0.02, -1, -0.02)
  line(-0.5, 0.02, -0.5, -0.02)
  line(0.5, 0.02, 0.5, -0.02)
  line(1, 0.02, 1, -0.02)

  ctx.font = '20px serif'
  ctx.textBaseline = 'middle'
  ctx.textAlign = 'start'

  ctx.fillText(`Y`, fix(0.1), fixY(1.2))
  ctx.fillText(`${r}`, fix(0.1), fixY(1))
  ctx.fillText(`${r / 2}`, fix(0.1), fixY(0.5))
  ctx.fillText(`-${r / 2}`, fix(0.1), fixY(-0.5))
  ctx.fillText(`-${r}`, fix(0.1), fixY(-1))

  ctx.textBaseline = 'alphabetic'
  ctx.textAlign = 'center'

  ctx.fillText(`X`, fix(1.2), fixY(0.1))
  ctx.fillText(`${r}`, fix(1), fixY(0.1))
  ctx.fillText(`${r / 2}`, fix(0.5), fixY(0.1))
  ctx.fillText(`-${r / 2}`, fix(-0.5), fixY(0.1))
  ctx.fillText(`-${r}`, fix(-1), fixY(0.1))

  // .firstChild()?.firstChild();
  // console.log(table);
  // console.log([...table.rows]);
  const drawHit = (x: number, y: number, hit: boolean) => {
    if (hit) {
      ctx.fillStyle = '#55ff55'
    } else {
      ctx.fillStyle = '#ff5555'
    }

    ctx.fillRect(fix(x / r), fixY(y / r), 5, 5)
  }
  // drawHit(x, y, true);

  results.forEach(({ x, y, r, hit }) => {
    drawHit(x, y, hit)
  })
}

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

export const getCursorPosition = (e: any) => {
  console.log(e)
  const canvas = document.getElementById('canvas') as HTMLCanvasElement
  console.log(canvas?.getBoundingClientRect())

  // const canvas = document.getElementById("canvas");
  const rect = canvas.getBoundingClientRect()
  const x = e.clientX - rect.left
  const y = e.clientY - rect.top

  return { x, y }

  // if (e.pageX !== undefined && e.pageY !== undefined) {
  // let x = e.pageX
  // let y = e.pageY
  // } else {
  // const x =
  //   e.clientX + document.body.scrollLeft + document.documentElement.scrollLeft;
  // const y = e.clientY + document.body.scrollTop + document.documentElement.scrollTop;
  // }
  // return {
  // x: x - canvas?.getBoundingClientRect()?.left || 0,
  // y: y - canvas?.getBoundingClientRect()?.top || 0
  // }
}
