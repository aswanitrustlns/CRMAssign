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
    var table1 = $('#datatable').DataTable({
         responsive: true,
         paging: true,
         lengthChange: false ,
         ordering: true,
         info:true,
         fixedHeader: true,
         buttons: [ 'print','copy','csv'],
     });
 
    //table1 btns
    table1.buttons().container()
    .appendTo('#datatable-buttons_wrapper1 ');
    $('#datatable-buttons_wrapper1 .dt-buttons').find('.btn').eq(0).prepend('<img src="static/images/printer.png" class="me-1">');
    $('#datatable-buttons_wrapper1 .dt-buttons').find('.btn').eq(1).prepend('<img src="static/images/copy.png" class="me-1">');
    $('#datatable-buttons_wrapper1 .dt-buttons').find('.btn').eq(2).prepend('<img src="static/images/document-text.png" class="me-1">');
    $('#datatable-buttons_wrapper1').find('.btn').addClass('me-2 d-inline-block flex-shrink-0  my-1 bg-soft-gunmetal border-0');
    $('#datatable-buttons_wrapper1').find('.btn-group').addClass('flex-xl-nowrap');
    $('#datatable-buttons_wrapper1').find('.btn-group').removeClass('flex-wrap');
    $('#myinputsearch1').keyup(function(){
        table1.search($(this).val()).draw() ;
    })

   
   



   
    

    let flatpickerFromdate1=flatpickr('#Fromdate1', {
        "allowInput": true,
        dateFormat: "Y-m-d",//MMMM Do YYYY
        altFormat:"Y-m-d",
        mode: "single",
        enableTime: false,
        altInput: true, // Human Readable
    });

   
    let flatpickertodate1=flatpickr('#Todate1', {
        "allowInput": true,
        dateFormat: "Y-m-d",//MMMM Do YYYY
        altFormat:"Y-m-d",
        mode: "single",
        altInput: true, // Human Readable
    });
   
});

