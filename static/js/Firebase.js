class Firebase {
    constructor(executibleFunction) {
        this.url = 'https://fir-basic-9a5d7.firebaseio.com/';
        this.xhttp = new XMLHttpRequest();
        this.postId = postId;
        this.xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                executibleFunction(JSON.parse(this.responseText));
            }
        };

    }


    post(url, jsObject) {
        this.xhttp.open("POST", this.url  + url + ".json", true);
        this.xhttp.setRequestHeader("Content-type", "application/json");
        this.xhttp.send(JSON.stringify(jsObject));
    }
    put(url, jsObject) {
        this.xhttp.open("PUT", this.url  + url + ".json", true);
        this.xhttp.setRequestHeader("Content-type", "application/json");
        this.xhttp.send(JSON.stringify(jsObject));
    }


    get(id) {
        this.xhttp.open("GET", this.url + "/" + id + ".json", true);
        this.xhttp.send();
    }
}