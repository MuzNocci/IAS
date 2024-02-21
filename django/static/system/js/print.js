document.getElementById('btn_print').onclick = function() {
    var conteudo = document.getElementById('print').innerHTML,
        tela_impressao = window.open('about:Impressão');

    tela_impressao.document.write(conteudo);
    tela_impressao.window.print();
    tela_impressao.window.close();
};