function fMasc(objeto,mascara) {
    obj=objeto
    masc=mascara
    setTimeout("fMascEx()",1)
}

function fMascEx() {
    obj.value=masc(obj.value)
}

function mCPF(cpf){
    cpf=cpf.replace(/\D/g,"")
    cpf=cpf.replace(/(\d{3})(\d)/,"$1.$2")
    cpf=cpf.replace(/(\d{3})(\d)/,"$1.$2")
    cpf=cpf.replace(/(\d{3})(\d{1,2})$/,"$1-$2")
    return cpf
}

function mCNPJ(cnpj){
    cnpj=cnpj.replace(/\D/g,"")
    cnpj=cnpj.replace(/(\d{2})(\d)/,"$1.$2")
    cnpj=cnpj.replace(/(\d{3})(\d)/,"$1.$2")
    cnpj=cnpj.replace(/(\d{3})(\d)/,"$1/$2")
    cnpj=cnpj.replace(/(\d{4})(\d{1,2})$/,"$1-$2")
    return cnpj
}

function mPHONE(phone){
    phone=phone.replace(/\D/g,"")
    phone=phone.replace(/(\d{0})(\d)/,"$1($2")
    phone=phone.replace(/(\d{2})(\d)/,"$1) $2")
    phone=phone.replace(/(\d{5})(\d)/,"$1-$2")
    return phone
}

function mCEP(cep){
    cep=cep.replace(/\D/g,"")
    cep=cep.replace(/(\d{5})(\d)/,"$1-$2")
    return cep
}