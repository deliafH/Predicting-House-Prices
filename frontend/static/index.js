const enter_btn = document.getElementById("btn")
const desc_textarea1 = document.getElementById('input1')
const desc_textarea2 = document.getElementById('input2')
const desc_textarea3 = document.getElementById('input3')
const desc_textarea4 = document.getElementById('input4')
const desc_textarea5 = document.getElementById('input5')
const desc_textarea6 = document.getElementById('input6')
const desc_textarea7 = document.getElementById('input7')
const desc_textarea8 = document.getElementById('input8')
const desc_textarea9 = document.getElementById('input9')
const csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0]
const spiner = document.getElementById('spiner')
const output = document.getElementById("output")

const server_url = `${window.location.protocol}//${window.location.host}`

enter_btn.onclick = async function () {
    val1 = desc_textarea1.value
    val2 = desc_textarea2.value
    val3 = desc_textarea3.value
    val4 = desc_textarea4.value
    val5 = desc_textarea5.value
    val6 = desc_textarea6.value
    val7 = desc_textarea7.value
    val8 = desc_textarea8.value
    val9 = desc_textarea9.value
    token = csrf_token.value
    spiner.style.display = "flex"

    await $.ajax({
        type: "POST",
        url: server_url,
        headers: {
            "X-CSRFToken": token
        },
        data: {
            "value1": val1,
            "value2": val2,
            "value3": val3,
            "value4": val4,
            "value5": val5,
            "value6": val6,
            "value7": val7,
            "value8": val8,
            "value9": val9,
        },
        success: function (result) {
            output.value= result['answer']
        },
        dataType: "json"
    });
    spiner.style.display = "none"
    output.style.display = "flex"
}