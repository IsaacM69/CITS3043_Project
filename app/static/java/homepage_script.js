
function openTab(evt, tabName) {
    var i, tab_content, tab_links;
    tab_content = document.getElementsByClassName("tab_content");
    for (i = 0; i < tab_content.length; i++) {
      tab_content[i].style.display = "none";
    }
    tab_links = document.getElementsByClassName("tab_links");
    for (i = 0; i < tab_links.length; i++) {
      tab_links[i].className = tab_links[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
  }

  document.onkeypress = (e) =>
  {
    if (e.key == '1')
    {
        openTab(event, 'tab1')
    }
    if (e.key == '2')
    {
        openTab(event, 'tab2')
    }
    if (e.key == '3')
    {
        openTab(event, 'tab3')

    }
    if (e.key == '4')
    {
        openTab(event, 'tab4')
    }

  }