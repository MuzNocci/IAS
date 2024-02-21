$(function(){

    $("#buscar_cep").click(function(){
    
      var cep = $("#zipcode").val().replace(/\D/g, '');
  
      if (cep != "") {
  
          var validacep = /^[0-9]{8}$/;
  
          if(validacep.test(cep)) {
  
          $.getJSON("//viacep.com.br/ws/"+ cep +"/json/?callback=?", function(dados) {
  
                    if (!("erro" in dados)) {
                        $("#address").val(dados.logradouro);
                        $("#district").val(dados.bairro);
                        $("#city").val(dados.localidade);
                        $("#state").val(dados.uf);
                        $("#country").val("Brasil");
                    } else {
                        $("#address").val("");
                        $("#district").val("");
                        $("#city").val("");
                        $("#state").val("");
                        $("#country").val("");
                    }
              });
          }
          else {
              console.log("Formato de CEP inválido.");
          }
      }
    });
  });