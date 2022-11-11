/*
Template Name: Minia - Admin & Dashboard Template
Author: Themesbrand
Website: https://themesbrand.com/
Contact: themesbrand@gmail.com
File: Datatables Js File
*/
//.DataTable.datetime('D MMM YYYY');

$(document).ready(function () {
    //const simpleUserActivity = new SimpleBar(document.getElementById('useractivity'));
    //const  simpleUploadDocumentsDetails  = new SimpleBar(document.getElementById('uploaddocumentsdetails'));
     //table1
   
    var input = document.getElementById('choosefile');
    //nput.type = 'file';
    input.onchange = e => { 
    var file = e.target.files[0]; 
    $('#choosetext').text( file.name);
    }
   
});

