<?php
// supply-distance.php

$errors = array();  // array to hold validation errors
$data = array();        // array to pass back data

// validate the variables ========
if (empty($_POST['string1']))
  $errors['string1'] = 'String1 is required.';

if (empty($_POST['string2']))
  $errors['string2'] = 'String2 is required.';

// return a response ==============

// response if there are errors
if ( ! empty($errors)) {

  // if there are items in our errors array, return those errors
  $data['success'] = false;
  $data['errors']  = $errors;
} else {

  // if there are no errors, return a message
  $data['success'] = true;

  // *******************************
  //
  //   calculate result here
  //
  // *******************************

  $data['answer'] = result;
}

// return all our data to an AJAX call
echo json_encode($data);