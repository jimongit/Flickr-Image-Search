 let paginationCount = numofpages;
 let nxtCounter = 0;
 let preCounter = 0;
    alert('hey');
      if(paginationCount <= 5)
    {
     document.getElementById("next").className = "page-item disabled";
     let x = 5 - paginationCount;
     for(i=x; i <= 5; i++){
     document.getElementById("l"+i).className = "page-item disabled";
      
    }
    }     
            
           let paginate = paginationCount >= 5 ? 5 : paginationCount;
                  
           for (let i=1; i <= paginate; i++) {
             let el = document.getElementById("link" + i);
              el.setAttribute("data",(numofpages - paginationCount)+i);  
              
           }
           
           if(paginationCount >=5){
            paginationCount-=5;
           }
          
 paginationCount+=5;
function next() {    
       
      
    document.getElementById("prev").className = "page-item";
       
    if(paginationCount <= 5)
    {
     document.getElementById("next").className = "page-item disabled";
     let x = 5 - paginationCount;
     for(i=x; i <= 5; i++){
     document.getElementById("l"+i).className = "page-item disabled";
      
    }
    } 
    
    if(paginationCount >=5){
        paginationCount-=5;
       }
            
           let paginate = paginationCount >= 5 ? 5 : paginationCount;
                  
           for (let i=1; i <= paginate; i++) {
             let el = document.getElementById("link" + i);
              el.setAttribute("data",(numofpages - paginationCount)+i);  
              
           }
      
           if(document.getElementById("link5").getAttribute("data")==numofpages){
            document.getElementById("next").className = "page-item disabled";
          
        }
        ajx('#link1');
    }
      
    
       function prev(){       
        
        document.getElementById("next").className = "page-item";
        if(paginationCount <= 5)
        {
          document.getElementById("prev").className = "page-item disabled";
         let x = 5 - paginationCount;
         for(i=x; i <= 5; i++){
          document.getElementById("l"+i).className = "page-item";
          
         }
        }
        if(paginationCount >=5){
            paginationCount += 5;
         }

        let paginate = paginationCount >= 5 ? 5 : paginationCount;
        for (let i = 1 ; i <= paginate; i++) {
       let el = document.getElementById("link" + i);
       let y = numofpages-paginationCount;
      
       el.setAttribute("data",y+i);  
      
     }
    if(document.getElementById("link1").getAttribute("data")=="1"){
        document.getElementById("prev").className = "page-item disabled";
    }
    
    ajx('#link5');  
}


function ajx(id){ 
  
    let pageNumber = $(id).attr("data");
    let rst; 
   $.ajax({
      
        type: "GET",
        url: "/ajax/",
        data: {search: $("#searchkey").val(),pageNumber:pageNumber},          
        async: false,  
        success:function(data) {
           rst = data; 
        }
        
       
  });
        alert(rst[0]);
          let result="";
          
          for(let i=0; i<rst.length;i++){                 
          result += "<div class=\"col-lg-3 col-md-4 col-xs-6 thumb\"><a href=\"" + rst[i] + "\" class=\"fancybox\" rel=\"ligthbox\"><img src=\"" + rst[i] +"\" class=\"zoom img-fluid\" alt=\"\"></a></div>";
              
        } 
        alert(result);
        $('#rst').html(result);           
        
  alert(id);
  
}


