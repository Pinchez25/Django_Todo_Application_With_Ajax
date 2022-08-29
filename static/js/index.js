const todo_links = Array.from(document.querySelectorAll(".todo-link"));
const search = document.getElementById("search_todo");
const todoList = document.getElementById("list-todos");
const root_url = "http://localhost:8000";


let complete = () => {
    $(document).on('click', '.todo-link', (e) => {
        e.preventDefault();
        const todoId = e.target.dataset.todo;

        $.ajax({
            type: "POST",
            url: "/complete_todo/",
            data: {
                todo_id: todoId,
                csrfmiddlewaretoken: csrftoken,
            },
            success: (res) => {
                console.log(res);
                e.target.classList.add("complete");
                console.log(e.target);
            },
            error: (err) => {
                console.log(err);
            },
        });
    })
}
complete()


let getTodos = () => {
    fetch("/todos/")
        .then((response) => response.json())
        .then((data) => {
            todos = data.todos;
            todos.forEach((result) => {
                todoList.innerHTML += "";
                todoList.innerHTML += `
            <li>
                        <p class="todo-link" data-todo=${result.id}>
                            ${result.title}&nbsp;&nbsp; <span class="text-info">${result.created}</span>
                        </p>
                    </li>
                    <div class="card-footer">
                        <p>
                            <a href="${root_url}/update-todo/${result.id}/" class="text-success text-decoration-none">Update</a>
                            <a href="${root_url}/todo/${result.id}/" class="text-decoration-none">View</a>
                        </p>
                        
                    </div>
                    <hr class='text-black-50'>
            `;
            });
        })
        .catch((err) => console.log(err));
};



search.addEventListener("keyup", (e) => {
    e.preventDefault();
    todoList.innerHTML = "";
    $.ajax({
        type: "GET",
        url: "/search/",
        data: {
            todo: e.target.value,
        },
        success: (res) => {
        
            results = res.todo_search;
            results.forEach((result) => {
                todoList.innerHTML += `
                <li>
                            <p class="todo-link" data-todo=${result.id}>
                                ${result.title}&nbsp;&nbsp; <span class="text-info">${result.created}</span>
                            </p>
                       </li>
                        <div class="card-footer">
                            <p>
                                <a href="${root_url}/update-todo/${result.id}/" class="text-success">Update</a>
                                <a href="${root_url}/todo/${result.id}/">View</a>
                            </p>
                            
                        </div>
                        <hr class='text-black-50'>
                `;

            });

        },
        error: (err) => {
            console.log(err);
        },
    });
});

getTodos()


