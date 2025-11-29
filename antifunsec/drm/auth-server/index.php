<?php

$url = explode("?", $_SERVER['REQUEST_URI'])[0];

function purchase() {
    $key = uniqid(true);
    file_put_contents("keys.txt", $key . PHP_EOL, FILE_APPEND | LOCK_EX);
    echo "Registration key: <code>" .$key. "</code>";
}

function check() {
    $key = $_GET['key'];
    $keys = explode(PHP_EOL, file_get_contents("keys.txt"));
    if (in_array($key, $keys) and $key !== "") {
        echo "OK";
    } else {
        echo "INVALID";
    }
}

if ($url === "/purchase") {
    purchase();
} elseif ($url === "/check") {
    check();
} else {
    echo "404 Not Found";
}