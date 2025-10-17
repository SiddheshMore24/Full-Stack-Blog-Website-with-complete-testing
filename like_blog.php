<?php
session_start();
require 'db.php';

if (!isset($_SESSION['reader_id'])) {
    header("Location: login.php");
    exit();
}

$readerId = $_SESSION['reader_id'];
$blogId = isset($_POST['blog_id']) ? intval($_POST['blog_id']) : 0;

// -------------------------------
//  Black-Box Testing: Input Validation
// -------------------------------
if ($blogId <= 0) {
    // Invalid blog request
    header("Location: reader.php?error=invalid_blog");
    exit();
}

// -------------------------------
// White-Box Testing: Path Coverage
// Path 1 → Like already exists
// Path 2 → Like inserted successfully
// Path 3 → DB error
// -------------------------------
$stmt = $conn->prepare("SELECT * FROM likes WHERE blog_id = ? AND reader_id = ?");
$stmt->bind_param("ii", $blogId, $readerId);
$stmt->execute();
$result = $stmt->get_result();

if ($result->num_rows === 0) {
    // Equivalence Partitioning: Insert new like
    $insert = $conn->prepare("INSERT INTO likes (blog_id, reader_id) VALUES (?, ?)");
    $insert->bind_param("ii", $blogId, $readerId);
    if (!$insert->execute()) {
        // DB error handling
        header("Location: view_blog.php?id=" . $blogId . "&msg=db_error");
        exit();
    }
    $insert->close();
} else {
    // Like already exists
    header("Location: view_blog.php?id=" . $blogId . "&msg=already_liked");
    exit();
}

$stmt->close();

// Redirect back to blog
header("Location: view_blog.php?id=" . $blogId . "&msg=like_success");
exit();
