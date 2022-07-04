// add row
var currentItem =1;

$("#addEducation").click(function () {
  
  
  currentItem++;
  var html = '';
  html += '<div> <label for="first_name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Degree</label> <input type="text" name="degree' +currentItem+ ' " class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="{{resume.education.degree}}" required> </div>';
  html += '<div> <label for="last_name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Major</label> <input type="text" name="major' +currentItem+ ' " class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="{{resume.education.major}}" required> </div>';
  html += '<div> <label for="company" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Start Date</label> <input type="text" name="start' +currentItem+ ' " class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="2018" required> </div>';
  html += ' <div> <label for="phone" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">End Date</label> <input type="text" name="end' +currentItem+ ' " class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="2022" required> </div>';
  html += '<div> <label for="website" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">University</label> <input type="text" name="university' +currentItem+ ' " class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="{{resume.education.university}}" required> </div>';
  html += '<div> <label for="visitors" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Wilaya</label> <input type="text" name="wilaya' +currentItem+ ' " class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="{{resume.education.wilaya}}" required> </div>';
  html += '<input name="education_count" type="hidden" value=" '+currentItem+' ">';
    




  $('#newEducation').append(html);
});

// remove row
$(document).on('click', '#removeRow', function () {
  $(this).closest('#drug-list-item').remove();
});


function setEventId(event_id){
document.querySelector("#event_id").innerHTML = event_id;
}