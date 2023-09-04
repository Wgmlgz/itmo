<?php
$rustart = getrusage();
date_default_timezone_set('Europe/Moscow');


// init
$x = $_POST['x'] ?? null;
$y = $_POST['y'] ?? null;
$r = $_POST['r'] ?? null;

// Validation
$valid = !(
  !is_numeric($x) || !is_numeric($y) || !is_numeric($r) ||
  !in_array($x, [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) ||
  $y < -5 || $y > 5 ||
  !in_array($r, [1, 2, 3, 4, 5])
);

// check
$result = $valid ?
  ((($x > 0 && $y > 0) && false) ||
    (($x > 0 && $y <= 0) && (($x <= $r && $y <= $r))) ||
    (($x <= 0 && $y > 0) && ($y - $x <= $r)) ||
    (($x <= 0 && $y <= 0) && ($x ** 2 + $y ** 2 <= ($r / 2) ** 2))
    ? "In" : "Out")
  : "Invalid data";


// Script end
function rutime($ru, $rus, $index)
{
  return ($ru["ru_$index.tv_sec"] * 1000000 + intval($ru["ru_$index.tv_usec"]))
    - ($rus["ru_$index.tv_sec"] * 1000000 + intval($rus["ru_$index.tv_usec"]));
}

$ru = getrusage();

$data = array(
  'x' => $x,
  'y' => $y,
  'r' => $r,
  'result' => $result,
  'timestamp' => date('H:i:s'),
  'exec' => rutime($ru, $rustart, "utime") . "usec"
);
header('Content-Type: application/json; charset=utf-8');
echo json_encode($data);
?>