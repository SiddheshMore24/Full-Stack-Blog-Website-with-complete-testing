<?php
session_start();
require 'db.php';

if (!isset($_SESSION['admin_id'])) {
    header("Location: login.php");
    exit();
}

$adminId = $_SESSION['admin_id'];
$blogId = isset($_GET['id']) ? intval($_GET['id']) : 0;

$stmt = $conn->prepare("SELECT * FROM blog_table WHERE id = ? AND admin_id = ?");
$stmt->bind_param("ii", $blogId, $adminId);
$stmt->execute();
$result = $stmt->get_result();

if ($result->num_rows === 0) {
    echo "Blog not found or unauthorized access.";
    exit();
}

$blog = $result->fetch_assoc();
$feedback = null;

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $title = trim($_POST['title']);
    $subtitle = trim($_POST['subtitle']);
    $content = trim($_POST['content']);
    $image_url = trim($_POST['image_url']);
    $status = $_POST['status'];

    // -------------------------------
    //  Black-Box Testing: Boundary Value Analysis
    // Title must be 5–150 chars, Content >= 20 chars
    // -------------------------------
    if (strlen($title) < 5 || strlen($title) > 150) {
        $feedback = "invalid_title";
    } elseif (strlen($content) < 20) {
        $feedback = "invalid_content";
    }
    // -------------------------------
    //  Black-Box Testing: Equivalence Partitioning
    // If image URL provided → must be valid format
    // -------------------------------
    elseif (!empty($image_url) && !filter_var($image_url, FILTER_VALIDATE_URL)) {
        $feedback = "invalid_image";
    }
    // -------------------------------
    //  Error Guessing
    // Invalid status tampering
    // -------------------------------
    elseif (!in_array($status, ['draft','published'])) {
        $feedback = "invalid_status";
    } else {
        // -------------------------------
        //  White-Box Testing: Basis Path Testing
        // Path 1 → Blog updated successfully
        // Path 2 → DB error
        // -------------------------------
        $updateStmt = $conn->prepare("UPDATE blog_table SET title = ?, subtitle = ?, content = ?, image_url = ?, status = ? WHERE id = ? AND admin_id = ?");
        $updateStmt->bind_param("sssssii", $title, $subtitle, $content, $image_url, $status, $blogId, $adminId);

        if ($updateStmt->execute()) {
            header("Location: dashboard.php?msg=blog_updated");
            exit();
        } else {
            $feedback = "db_error";
        }
        $updateStmt->close();
    }
}

$stmt->close();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Edit Blog Post</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', sans-serif;
            margin: 0;
            padding: 0;
            min-height: 100vh;
            background-image: url('https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?auto=format&fit=crop&w=1920&q=80');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #e4e4e4;
        }

        .glass-card {
            background: rgba(20, 20, 20, 0.6);
            border-radius: 20px;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            padding: 2.5rem;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.6);
            animation: fadeInUp 0.7s ease;
            width: 100%;
            max-width: 720px;
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        h3 {
            font-weight: 600;
            text-align: center;
            margin-bottom: 30px;
            color: #ffffff;
        }

        .form-label {
            font-weight: 500;
            color: #d1d1d1;
        }

        .form-control,
        .form-select {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #ffffff;
            border-radius: 12px;
            padding: 10px 14px;
            backdrop-filter: blur(4px);
            -webkit-backdrop-filter: blur(4px);
            transition: background 0.3s, border 0.3s;
        }

        .form-control::placeholder {
            color: #ccc;
        }

        .form-control:focus,
        .form-select:focus {
            background: rgba(255, 255, 255, 0.12);
            border-color: #8f94fb;
            color: #fff;
            box-shadow: 0 0 0 0.25rem rgba(143, 148, 251, 0.3);
        }

        .form-select option {
            background-color: #1e1e2f;
            color: #ffffff;
        }

        .btn-info {
            border-radius: 12px;
            padding: 10px 22px;
            background: linear-gradient(135deg, #4e54c8, #8f94fb);
            border: none;
            font-weight: bold;
            color: white;
        }

        .btn-link {
            color: #bbb;
        }

        .btn-link:hover {
            color: #fff;
        }
    </style>
</head>
<body>
<div class="glass-card">
    <h3>✏️ Edit Blog Post</h3>

    <!-- 🔍 Feedback messages -->
    <?php if ($feedback === 'invalid_title'): ?>
        <div class="alert alert-warning text-center">⚠️ Title must be between 5 and 150 characters.</div>
    <?php elseif ($feedback === 'invalid_content'): ?>
        <div class="alert alert-warning text-center">⚠️ Content must be at least 20 characters long.</div>
    <?php elseif ($feedback === 'invalid_image'): ?>
        <div class="alert alert-warning text-center">⚠️ Please enter a valid Image URL.</div>
    <?php elseif ($feedback === 'invalid_status'): ?>
        <div class="alert alert-warning text-center">⚠️ Invalid status selected.</div>
    <?php elseif ($feedback === 'db_error'): ?>
        <div class="alert alert-danger text-center">❌ Something went wrong while updating the blog.</div>
    <?php endif; ?>

    <form method="POST">
        <div class="mb-3">
            <label class="form-label">Title</label>
            <input type="text" name="title" class="form-control" value="<?php echo htmlspecialchars($blog['title']); ?>" required>
        </div>

        <div class="mb-3">
            <label class="form-label">Subtitle</label>
            <input type="text" name="subtitle" class="form-control" value="<?php echo htmlspecialchars($blog['subtitle']); ?>">
        </div>

        <div class="mb-3">
            <label class="form-label">Content</label>
            <textarea name="content" class="form-control" rows="10" required><?php echo htmlspecialchars($blog['content']); ?></textarea>
        </div>

        <div class="mb-3">
            <label class="form-label">Image URL</label>
            <input type="text" name="image_url" class="form-control" value="<?php echo htmlspecialchars($blog['image_url']); ?>">
        </div>

        <div class="mb-4">
            <label class="form-label">Status</label>
            <select name="status" class="form-select">
                <option value="draft" <?php if ($blog['status'] === 'draft') echo 'selected'; ?>>Draft</option>
                <option value="published" <?php if ($blog['status'] === 'published') echo 'selected'; ?>>Published</option>
            </select>
        </div>

        <button type="submit" class="btn btn-info w-100">💾 Update Blog</button>
    </form>

    <div class="text-center mt-3">
        <a href="dashboard.php" class="btn btn-link text-decoration-none">← Back to Dashboard</a>
    </div>
</div>
</body>
</html>
