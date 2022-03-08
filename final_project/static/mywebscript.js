<<<<<<< HEAD
let translateToSpanish = ()=>{
=======
let translateToFrench = ()=>{
>>>>>>> f6cf6b8453eddb96910714c430cce8c33d7fa654
    textToTranslate = document.getElementById("textToTranslate").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("translated_text").innerHTML = xhttp.responseText;
        }
    };
<<<<<<< HEAD
    xhttp.open("GET", "englishToSpanish?textToTranslate"+"="+textToTranslate, true);
=======
    xhttp.open("GET", "englishToFrench?textToTranslate"+"="+textToTranslate, true);
>>>>>>> f6cf6b8453eddb96910714c430cce8c33d7fa654
    xhttp.send();
}

let translateToEnglish = ()=>{
    textToTranslate = document.getElementById("textToTranslate").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("translated_text").innerHTML = xhttp.responseText;
        }
    };
<<<<<<< HEAD
    xhttp.open("GET", "spanishToEnglish?textToTranslate"+"="+textToTranslate, true);
=======
    xhttp.open("GET", "frenchToEnglish?textToTranslate"+"="+textToTranslate, true);
>>>>>>> f6cf6b8453eddb96910714c430cce8c33d7fa654
    xhttp.send();
}

