<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>I hate php</title>
  <link rel="stylesheet" href="styles.css">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap" rel="stylesheet">
  <script src="index.js" defer></script>

</head>

<body>
  <div class="content">
    <div class="header">
      <h1>
        Мацюк Владимир Николаевич, P3215
      </h1>
      <h3>
        вариант 371371
      </h3>
    </div>
    <!-- <img src="task.png" alt="task"> -->
    <canvas width="400px" height="400px" id=canvas></canvas>
    <!-- <iframe src="https://www.desmos.com/calculator/rqarvlfnuo?embed" width="500" height="500"
      style="border: 1px solid #ccc" frameborder=0></iframe> -->

    <div class="dotted-spaced"><br /></div>

    <form method="post" class="ig" id="form">
      <div class="ig">
        <div class="ct">
          <label for="x">X:</label>
          <input value=0 readonly id="x" type="number" min="-5" max="5" step="1" name="x" />
        </div>
        <div class="ct">
          <button type="button" onclick="setX(this)">-5</button>
          <button type="button" onclick="setX(this)">-4</button>
          <button type="button" onclick="setX(this)">-3</button>
          <button type="button" onclick="setX(this)">-2</button>
          <button type="button" onclick="setX(this)">-1</button>
          <button type="button" onclick="setX(this)">0</button>
          <button type="button" onclick="setX(this)">1</button>
          <button type="button" onclick="setX(this)">2</button>
          <button type="button" onclick="setX(this)">3</button>
        </div>
      </div>
      <div class="ig">
        <div class="ct">
          <label for="y">Y:</label>
          <input value=0 type="number" id="y" name="y" step="any" min="-5" max="5" required>
        </div>
      </div>

      <div class="ig">
        <div class="ct">
          <label for="r">R:</label>
          <span>
            <input type="radio" name="r" value="1" id="huey1" checked />
            <label for="huey1">1</label>
            <input type="radio" name="r" value="2" id="huey2" />
            <label for="huey2">2</label>
            <input type="radio" name="r" value="3" id="huey3" />
            <label for="huey3">3</label>
            <input type="radio" name="r" value="4" id="huey4" />
            <label for="huey4">4</label>
            <input type="radio" name="r" value="5" id="huey5" />
            <label for="huey5">5</label>
          </span>
        </div>
      </div>
      <button type="submit">Check </button>
    </form>

    <br />
    <div class="dotted-spaced"><br /></div>

    <table id="table">
      <tr>
        <th>X</th>
        <th>Y</th>
        <th>R</th>
        <th>Result</th>
        <th>Time</th>
        <th>Exec</th>
      </tr>
    </table>
</body>

</html>