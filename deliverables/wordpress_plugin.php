```php
<?php
/**
 * Plugin Name: AI Article Generator
 * Plugin URI: https://www.yourwebsite.com/
 * Description: This is a custom WordPress plugin that communicates with an AI server to generate and post AI-based articles.
 * Version: 1.0
 * Author: Your Name
 * Author URI: https://www.yourwebsite.com/
 */

// Server address
$server_address = 'http://your-server-address.com';

// Plugin ID
$plugin_id = 'ai-article-generator';

// DOM Element IDs
$post_button = 'post_button';
$article_container = 'article_container';

// Message Names
$generate_article = 'generate_article';
$article_generated = 'article_generated';

// Function to send request to the server
function send_request($seed) {
    global $server_address, $generate_article;

    $request_data = array(
        'seed' => $seed,
        'prompt' => $generate_article
    );

    $response = wp_remote_post($server_address, array(
        'method' => 'POST',
        'body' => $request_data
    ));

    if (is_wp_error($response)) {
        $error_message = $response->get_error_message();
        echo "Something went wrong: $error_message";
    } else {
        return json_decode(wp_remote_retrieve_body($response), true);
    }
}

// Function to create a new post with the generated article
function create_post($article_data) {
    global $article_generated;

    $post_id = wp_insert_post(array(
        'post_title' => $article_data['title'],
        'post_content' => $article_data['content'],
        'post_status' => 'publish',
        'post_author' => 1,
        'tags_input' => $article_data['tags']
    ));

    if($post_id){
        echo "Post Created Successfully!";
    } else {
        echo "Post Creation Failed!";
    }
}

// Handle the click event of the post button
add_action('wp_ajax_generate_article', function() {
    global $post_button;

    $seed = $_POST['seed'];
    $response_data = send_request($seed);

    if ($response_data['status'] == 'success') {
        create_post($response_data['article_data']);
    } else {
        echo "Article Generation Failed!";
    }

    wp_die();
});

?>
```