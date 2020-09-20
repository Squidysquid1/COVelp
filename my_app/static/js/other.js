function showForm() {
  form = document.getElementById('form');
  form.style.display = 'block';
}

function hideForm() {
  form = document.getElementById('form')
  form.style.display = 'none';
}

function reviewForm() {
  form = document.getElementById('form').elements

  form[0]

  for (var i = 0; i < form.length; i++) {
    form[i]
  }

}

busySlider = document.getElementById('busy-slide')
busySlider.oninput = function() {
  document.getElementById('busy-val').innerHTML = this.value;
}

sDSlider = document.getElementById('sdScore-slide')
sDSlider.oninput = function() {
  document.getElementById('sdScore-val').innerHTML = this.value;
}

maskScoreSlider = document.getElementById('maskScore-slide')
maskScoreSlider.oninput = function() {
  document.getElementById('maskScore-val').innerHTML = this.value;
}
