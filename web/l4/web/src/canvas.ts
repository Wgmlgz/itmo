export const drawGraph = (
  x: number,
  y: number,
  r: number,
  results: { x: number; y: number; r: number; hit: boolean }[]
) => {
  const canvas = document.getElementById('canvas') as HTMLCanvasElement

  if (!canvas) throw new Error('No canvas?')

  const ctx = canvas.getContext('2d')

  if (r > 3) r = 3
  if (r < 1) r = 1

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

  const drawHit = (x: number, y: number, hit: boolean) => {
    if (hit) {
      ctx.fillStyle = '#55ff55'
    } else {
      ctx.fillStyle = '#ff5555'
    }

    ctx.fillRect(fix(x / r), fixY(y / r), 5, 5)
  }

  results.forEach(({ x, y, r, hit }) => {
    drawHit(x, y, hit)
  })
}

export const getCursorPosition = (e: any) => {
  const canvas = document.getElementById('canvas') as HTMLCanvasElement

  const rect = canvas.getBoundingClientRect()
  const x = e.clientX - rect.left
  const y = e.clientY - rect.top

  return { x, y }
}
