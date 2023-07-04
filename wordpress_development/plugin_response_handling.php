```php
<?php
/**
 * Plugin Name: AI Article Generator
 * Description: A plugin to generate and post AI-based articles.
 * Version: 1.0
 * Author: Your Name
 * Author URI: Your Website
 */

// Ensure WordPress is loaded
if (!defined('ABSPATH')) {
    exit;
}

// Define server address
define('SERVER_ADDRESS', 'your_server_address');

// Handle server response
function handle_server_response($response) {
    // Decode JSON response
    $response_data = json_decode($response);

    // Check if response is valid
    if (isset($response_data->status) && $response_data->status == 'success') {
        // Create new post with the generated article
        create_post($response_data->article_data);
    } else {
        // Log error message
        error_log('Error generating article: ' . $response_data->message);
    }
}

// Create new post
function create_post($article_data) {
    // Prepare post data
    $post_data = array(
        'post_title'    => wp_strip_all_tags($article_data->title),
        'post_content'  => $article_data->content,
        'post_status'   => 'publish',
        'post_author'   => 1,
        'post_category' => array(1),
        'tags_input'    => $article_data->tags
    );

    // Insert the post into the database
    wp_insert_post($post_data);
}

// Send request to server
function send_request() {
    // Prepare request data
    $request_data = array(
        'seed' => 'AI agents',
        'prompt' => 'The future of AI agents'
    );

    // Send POST request to server
    $response = wp_remote_post(SERVER_ADDRESS, array(
        'method' => 'POST',
        'body' => json_encode($request_data),
        'headers' => array('Content-Type' => 'application/json')
    ));

    // Check if request was successful
    if (is_wp_error($response)) {
        // Log error message
        error_log('Error sending request: ' . $response->get_error_message());
    } else {
        // Handle server response
        handle_server_response($response['body']);
    }
}

// Set up cron job to send request every hour
if (!wp_next_scheduled('send_request')) {
    wp_schedule_event(time(), 'hourly', 'send_request');
}

// Add action hook for cron job
add_action('send_request', 'send_request');
?>
```