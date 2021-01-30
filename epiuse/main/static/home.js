document.addEventListener("DOMContentLoaded",function(){

    let form = document.querySelector("#search-form");
    let name_form = document.querySelector("#name-search-form");
    form.addEventListener("submit",(e)=>{
        e.preventDefault();
        console.log("Submitted Form");
        emp_dob = form.emp_dob.value;
        // #emp_num,emp_relation,emp_role,emp_name,emp_surname,emp_dob,emp_salary
        if(validate_date(emp_dob)){
            var url = "/search_query/";
            fetch(url,{
                method:"POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken":csrftoken,
                },
                body:JSON.stringify({"emp_dob":emp_dob})
            }).then((response)=>{
                    return response.json();
            }).then((data)=>{
                    console.log("Success: ",data);
                    perform_search_update(data);
                    // window.location.href = "{% url '/'/ %}"
            });
        }else{
            alert("Please verify that your age is correct");
        }
        
    });
    name_form.addEventListener("submit",(e)=>{
        e.preventDefault();
        console.log("Submitted Form");
        name = name_form.name.value;
        // #emp_num,emp_relation,emp_role,emp_name,emp_surname,emp_dob,emp_salary
        if(validate_name(name)){
            var url = "/search_name/";
            fetch(url,{
                method:"POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken":csrftoken,
                },
                body:JSON.stringify({"name":name})
            }).then((response)=>{
                    return response.json();
            }).then((data)=>{
                    console.log("Success: ",data);
                    perform_search_update(data);
                    // window.location.href = "{% url '/'/ %}"
            });
        }else{
            alert("Please verify that your age is correct");
        }
        
    });
    

    function perform_search_update(data){
        document.getElementById("search-list").innerHTML = "";
        let div =  document.getElementById("search");
        console.log(div.getElementsByTagName("h1").length);

        
        if(data.length > 0){
            let h1 = document.createElement("h1");
            h1.appendChild(document.createTextNode("Search Results"));
            let search_div = document.querySelector("#search");
            let search_list = document.querySelector("#search-list");
            // search_div.appendChild(h1);
            search_div.appendChild(search_list);
            for(let i =0;i < data.length;i++){
                console.log(data[i]);
                console.log(data[i]['fields']);
                let li = document.createElement("li");
                let string = `Employee ID: ${data[i]['pk']} - ${data[i]['fields']['emp_name']} ${data[i]['fields']['emp_surname']} is Epiuse\'s ${data[i]['fields']['emp_role']}`;
                // li.appendChild(document.createTextNode(data[i]['fields']['emp_name']));
                li.appendChild(document.createTextNode(string));
                search_list.appendChild(li);
                // <h1>Employee</h1>
                // <ul>
                // {% for employee in employees %}
                // <li></li>
            }
        }else{
            alert("User does not exist in database");
        }
    }

    function validate_name(data) {
        let re = "^[^0-9]+$";
        let patt = new RegExp(re);
        return patt.test(data);
    }
    function validate_date(date) {
        let re = "^[0-9]{4}-(1[0-2]|0[1-9])-(3[01]|[12][0-9]|0[1-9])$";
        let patt = new RegExp(re);
        date_of_year = parseInt(date.substring(0,4));
        age = 2020 - date_of_year;
        return patt.test(date) && age >=16;
    }

});