const todoList = [{
    name:'Mohit Jaiswal',
    dueDate:'2025-05-26'
 }, {
        name:'Rishabh',
        dueDate:'2025-05-26'
}];

renderTodoList();
function renderTodoList () {
    let todoListHTML = '';

    for (let i = 0; i< todoList.length ; i++) {
        const todoObject = todoList[i];
        // const name = todoObject.name;
        // const dueDate = todoObject.dueDate;

        // shortcut for above two line
        const {name, dueDate} = todoObject;
        // generating the html
        const html = `
        <div>${name}</div>
        <div> ${dueDate} </div>
        <button onclick="
            todoList.splice(${i}, 1);
            renderTodoList();
        " class="delete-todo-button">Delete</button>
        `;
        todoListHTML += html 

    }
    // console.log(todoListHTML);

    document.querySelector('.js-todo-list')
        .innerHTML = todoListHTML;
}
function addTodo() {
    const inputElement = document.querySelector('.js-name-input');
    const name = inputElement.value;
    const dateInputElement = document.querySelector(".js-due-date-input");
    const dueDate = dateInputElement.value
    // console.log(name);
    todoList.push({
        // name: name,
        // dueDate: dueDate
        // If property name and variable name  are same then we use simply below one
        name,
        dueDate
    });
    // console.log(todoList);

    inputElement.value = '';


    renderTodoList();
}