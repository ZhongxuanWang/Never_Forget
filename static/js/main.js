function submit(operation, id) {
    alert("{{ task.id }}");
    // {#    var declarations are globally scoped or function scoped while let and const are block scoped.
    //     var variables can be updated and re-declared within its scope; let variables can be updated but not
    //     re-declared; const variables can neither be updated nor re-declared.#}
    // const maxtime = "" + document.getElementById('maxtime').value;
    const cont = document.getElementById('content').value;
    const date = document.getElementById('date').value;
    const e_war = document.getElementById('email_warning').checked ? 1 : 0;
    if (cont === '' || date === '') {
        alert("You must input valid content and date (within 100 years).")
    } else {
        const xhr = new XMLHttpRequest();
        xhr.open("POST", '/' + operation + '/{{ task.id }}/' + cont + "/" + date + "/" + e_war, false);
        xhr.send();
        location.reload();
    }


}

// function submit() {
//     const maxtime = "" + document.getElementById('maxtime').value;
//     const cont = document.getElementById('content').value;
//     const date = document.getElementById('date').value;
//     if (cont === '' || date === '' || date > maxtime) {
//         alert("You must input valid content and date (within 100 years).")
//     } else {
//         const xhr = new XMLHttpRequest();
//         xhr.open("POST", '/addTask/' + cont + "/" + date, false);
//         xhr.send();
//         location.reload();
//     }
// }
