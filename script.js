function print1() {
  var combo = parseInt(document.getElementById('sceglicombo').value);
  var numero = Math.floor(Math.random() * combo) + 1;
  document.getElementById('log2').textContent = 'Hai generato la combo di:';
  document.getElementById('log').textContent = numero;

  var nomi = ["Jeb", "Cross", "Montante", "Gancio Destro", "Gancio Sinistro", "Gangio Destro americana", "Gancio Sinistro americana", "Teschio", "Full", "Mataleao"];

  function nomeCasuale() {
     var indiceCasuale = Math.floor(Math.random() * nomi.length);
     return nomi[indiceCasuale];
  }

  var combofinale = '';
  var combofinale = nomeCasuale();
  var numero = numero - 1;
  for (var i = 0; i < numero; i++) {
    var nome = nomeCasuale();
    var combofinale = combofinale + ', ' + nome;
  }
  document.getElementById('combo').textContent = combofinale;
}
