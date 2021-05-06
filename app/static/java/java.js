
//i could probably do this in a loop but i have a smooth brain ¯\_(ツ)_/¯
function check_marks()
{
    alert("checking")
    let amount_correct = 0;
    let rbs = document.querySelectorAll('input[name="q1"]');
    let selectedValue;
    for (const rb of rbs) {
        if (rb.checked) {
            selectedValue = rb.value;
            break;
        }
    }
    if (selectedValue == "yes")
    {
        amount_correct++;
        alert("correct")
        document.getElementById("a1").style.color = "green";

    }
    else
    {
        document.getElementById("a1").style.color = "red";
    }

    rbs = document.querySelectorAll('input[name="q2"]');
    for (const rb of rbs) {
        if (rb.checked) {
            selectedValue = rb.value;
            break;
        }
    }
    if (selectedValue == "yes")
    {
        amount_correct++;
        alert("correct")
        document.getElementById("a2").style.color = "green";

    }
    else
    {
        document.getElementById("a2").style.color = "red";
    }

    rbs = document.querySelectorAll('input[name="q3"]');
    for (const rb of rbs) {
        if (rb.checked) {
            selectedValue = rb.value;
            break;
        }
    }
    if (selectedValue == "no")
    {
        amount_correct++;
        document.getElementById("a3").style.color = "green";

    }
    else
    {
        document.getElementById("a3").style.color = "red";
    }

    rbs = document.querySelectorAll('input[name="q4"]');
    for (const rb of rbs) {
        if (rb.checked) {
            selectedValue = rb.value;
            break;
        }
    }
    if (selectedValue == "2s")
    {
        amount_correct++;
        alert("correct")
        document.getElementById("a4").style.color = "green";

    }
    else
    {
        document.getElementById("a4").style.color = "red";
    }
    rbs = document.querySelectorAll('input[name="q5"]');
    for (const rb of rbs) {
        if (rb.checked) {
            selectedValue = rb.value;
            break;
        }
    }
    if (selectedValue == "no")
    {
        amount_correct++;
        alert("correct")
        document.getElementById("a5").style.color = "green";

    }
    else
    {
        document.getElementById("a5").style.color = "red";
    }

    document.getElementById("points").innerHTML = (amount_correct + " out of 5");
    alert(amount_correct)

    document.getElementById("test").style.display = "none";
    document.getElementById("marks").style.display = "block";

}