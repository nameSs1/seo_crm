const btns = document.querySelectorAll('button.show-project');


btns.forEach(b=>b.addEventListener('click', () => {
	b.setAttribute("pressed", true);
	let promise = getProjectInfo(b);
	promise.then(showProjectInfo);
}));


function showProjectInfo(data) {  // когда получаем инфу от сервера, добовляем строку в таблицу
	let rowProject = data[1].parentElement.parentElement.parentElement; // Получаем строку проекта в таблице
	let newRow = rowProject.insertAdjacentHTML("afterEnd", data[0]);  // вставляем полученый фрагмент html
}

