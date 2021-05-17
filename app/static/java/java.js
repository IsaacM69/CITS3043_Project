
//i could probably do this in a loop but i have a smooth brain ¯\_(ツ)_/¯
//checks the marks for each test, actual answers are to be sent to db but this checker is just for 
//the results tab whilst we get the db working

function check_marks()
{
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
        document.getElementById("a5").style.color = "green";

    }
    else
    {
        document.getElementById("a5").style.color = "red";
    }

    document.getElementById("points").innerHTML = (amount_correct + " out of 5");

    document.getElementById("test").style.display = "none";
    document.getElementById("marks").style.display = "block";

}