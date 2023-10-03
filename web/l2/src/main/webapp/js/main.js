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


// window.onload = () => {
//   canvas = document.getElementById('plot');
//   form = document.getElementById('form');
//   table = document.getElementById('table');
//   ctx = canvas.getContext('2d');
  
//   form.oninput = () => updatePlot();
//   form.onsubmit = async (e) => {
//     e.preventDefault();
//     const { x, y, r, result, timestamp, exec } = await fetch('check.php', {
//       method: 'post',
//       body: new FormData(form),
//     }).then((res) => res.json());
//     old_values.push({ x: Number(x), y: Number(y) });
//     row = table.insertRow(1);
//     row.insertCell(0).innerHTML = x;
//     row.insertCell(1).innerHTML = y;
//     row.insertCell(2).innerHTML = r;
//     row.insertCell(3).innerHTML = result;
//     row.insertCell(4).innerHTML = timestamp;
//     row.insertCell(5).innerHTML = exec;
//   };
//   updatePlot();
// };


$(function() {

        function isNumeric(n) {
            return !isNaN(parseFloat(n)) && isFinite(n);
        }

        function validateX() {
            const X_MIN = -2;
            const X_MAX = +2;
            let xField = $('#x-textinput');
            let numX = xField.val().trim().replace(',','.');

            xField.val(numX);
            if(isNumeric(numX) && numX > X_MIN && numX < X_MAX) {
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
            const Y_VALUES = ["-2","-1.5","-1","-0.5","0","0.5","1","1.5","2"];
            let selector = document.getElementById("y");
            let ySelector = $('#r-textinput');
            let numY = selector.options[selector.selectedIndex].text.trim().replace(',', '.');
            if(isNumeric(numY) && (numY in Y_VALUES || (numY >= -2 && numY <= 2))){
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


    }
);

const clearBtn = document.getElementById("resetBtn");
clearBtn.addEventListener("click", e => {
    e.preventDefault();
    const params = {'clear': true}
    window.location.replace("/lab2/process" + formatParams(params));
})

const submitBtn = document.getElementById("submitBtn");
function toggleSubmitBtn() {
    alert("Submit is working");
    submitBtn.disabled = !(xValid && yValid && rValid)
}

document.addEventListener('DOMContentLoaded', ()=> {
    document.getElementById("plot").addEventListener('click', drawPoint);
});

