```php
<?php
/*
Plugin Name: AI Article Generator
Description: A plugin to generate and post AI-based articles.
Version: 1.0
Author: AI Developer
*/

// Server address
$server_address = "http://your-server-address.com";

// Unique identifier for the plugin
$plugin_id = "ai_article_generator";

// Function to send a request to the server
function send_request() {
    global $server_address;
    global $plugin_id;

    // Prepare the request data
    $request_data = array(
        'seed' => 'AI agents',
        'prompt' => 'The future of AI agents'
    );

    // Prepare the request headers
    $headers = array(
        'Content-Type' => 'application/json',
        'Plugin-ID' => $plugin_id
    );

    // Prepare the request arguments
    $args = array(
        'method' => 'POST',
        'headers' => $headers,
        'body' => json_encode($request_data)
    );

    // Send the request to the server
    $response = wp_remote_post($server_address . '/generate_article', $args);

    // Check for errors
    if (is_wp_error($response)) {
        $error_message = $response->get_error_message();
        echo "Something went wrong: $error_message";
    } else {
        echo 'Request sent successfully.';
    }
}

// Hook the 'send_request' function to the 'init' action
add_action('init', 'send_request');
?>
```