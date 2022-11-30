window.addEventListener("load", function ()
{
    //get click elements
    let clickButtonElement = document.getElementById("click_button");
    let clickCounterElement = document.getElementById("click_counter");

    //counter value
    let counter = 0;

    //button click function
    let clickButtonFunction = function ()
    {
        //increment counter
        counter++;

        //update click counter text
        clickCounterElement.innerHTML = counter;
    };
    
    //attach click function to button
    clickButtonElement.addEventListener("click", clickButtonFunction);
});