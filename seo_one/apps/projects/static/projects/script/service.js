function getProjectInfo(titleProject) {
    const promise = axios.get(`http://127.0.0.1:8000/projects/Lesha/${titleProject.firstChild.data}`);
    return promise.then((response) => {
    	return [response.data, titleProject];
    });
}